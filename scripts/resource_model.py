from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from zoneinfo import ZoneInfo

import yaml

REQUIRED_FIELDS = (
    "id",
    "title_zh",
    "title_original",
    "url",
    "category",
    "source",
    "added_at",
    "language",
    "summary_zh",
    "tags",
    "featured",
)
STRING_FIELDS = (
    "id",
    "title_zh",
    "title_original",
    "url",
    "category",
    "source",
    "language",
    "summary_zh",
)
TRACKING_PARAMETERS = frozenset({"urlsource", "fbclid", "gclid"})
CATALOG_TIMEZONE = ZoneInfo("Asia/Shanghai")


class CatalogFormatError(ValueError):
    """Raised when a catalog cannot be interpreted as a resource list."""


def _catalog_today(now: datetime | None = None) -> date:
    current = now or datetime.now(CATALOG_TIMEZONE)
    return current.astimezone(CATALOG_TIMEZONE).date()


def _contains_cjk(value: str) -> bool:
    return any(
        "\u3400" <= character <= "\u4dbf"
        or "\u4e00" <= character <= "\u9fff"
        or "\uf900" <= character <= "\ufaff"
        for character in value
    )


@dataclass(frozen=True, slots=True)
class Resource:
    id: str
    title_zh: str
    title_original: str
    url: str
    category: str
    source: str
    published_at: date | None
    added_at: date
    language: str
    summary_zh: str
    tags: tuple[str, ...]
    featured: bool
    _missing_fields: tuple[str, ...] = field(default=(), repr=False, compare=False)
    _schema_errors: tuple[str, ...] = field(default=(), repr=False, compare=False)


def _parse_date(
    value: object, field_name: str, *, optional: bool, errors: list[str]
) -> date | None:
    if value is None or value == "":
        if not optional:
            errors.append(f"{field_name} must be a valid YYYY-MM-DD date")
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            pass
    errors.append(f"{field_name} must be a valid YYYY-MM-DD date")
    return None


def _string_field(item: dict[object, object], name: str, errors: list[str]) -> str:
    value = item.get(name, "")
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{name} must be a non-empty string")
        return ""
    return value


def _resource_from_item(raw_item: object) -> Resource:
    schema_errors: list[str] = []
    if not isinstance(raw_item, dict):
        schema_errors.append("entry must be a mapping")
        item: dict[object, object] = {}
    else:
        item = raw_item

    strings = {name: _string_field(item, name, schema_errors) for name in STRING_FIELDS}
    published_at = _parse_date(
        item.get("published_at"), "published_at", optional=True, errors=schema_errors
    )
    added_at = _parse_date(
        item.get("added_at"), "added_at", optional=False, errors=schema_errors
    )

    raw_tags = item.get("tags")
    if (
        not isinstance(raw_tags, list)
        or not raw_tags
        or any(not isinstance(tag, str) or not tag.strip() for tag in raw_tags)
    ):
        schema_errors.append("tags must be a non-empty list of strings")
        tags: tuple[str, ...] = ()
    else:
        tags = tuple(raw_tags)

    raw_featured = item.get("featured")
    if not isinstance(raw_featured, bool):
        schema_errors.append("featured must be a boolean")
        featured = False
    else:
        featured = raw_featured

    return Resource(
        **strings,
        published_at=published_at,
        added_at=added_at or date.min,
        tags=tags,
        featured=featured,
        _missing_fields=tuple(name for name in REQUIRED_FIELDS if name not in item),
        _schema_errors=tuple(schema_errors),
    )


def load_resources(path: Path) -> list[Resource]:
    try:
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        raise CatalogFormatError(f"{path}: invalid YAML: {error.problem or error}") from error

    if document is None:
        document = {}
    if not isinstance(document, dict):
        raise CatalogFormatError(f"{path}: top level must be a mapping")
    raw_resources = document.get("resources", [])
    if not isinstance(raw_resources, list):
        raise CatalogFormatError(f"{path}: resources must be a list")
    return [_resource_from_item(item) for item in raw_resources]


def _normalized_url(url: str) -> str:
    parts = urlsplit(url)
    query = urlencode(
        [
            (key, value)
            for key, value in parse_qsl(parts.query, keep_blank_values=True)
            if not key.lower().startswith("utm_") and key.lower() not in TRACKING_PARAMETERS
        ]
    )
    path = parts.path.rstrip("/")
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, query, ""))


def validate_resources(resources: list[Resource]) -> list[str]:
    errors: list[str] = []
    ids: dict[str, int] = {}
    urls: dict[str, str] = {}
    today = _catalog_today()
    for index, resource in enumerate(resources, start=1):
        label = resource.id or f"resource #{index}"
        errors.extend(f"{label}: missing field: {name}" for name in resource._missing_fields)
        errors.extend(f"{label}: {message}" for message in resource._schema_errors)

        if resource.id in ids:
            errors.append(f"duplicate ID: {resource.id!r} at resources {ids[resource.id]} and {index}")
        else:
            ids[resource.id] = index

        parts = urlsplit(resource.url)
        if parts.scheme.lower() != "https":
            errors.append(f"{label}: URL must use HTTPS")
        if not parts.hostname:
            errors.append(f"{label}: URL must include a hostname")

        if resource.published_at is not None and resource.published_at > today:
            errors.append(f"{label}: future published_at: {resource.published_at.isoformat()}")
        if resource.added_at > today:
            errors.append(f"{label}: future added_at: {resource.added_at.isoformat()}")

        title = resource.title_zh.strip()
        if not title:
            errors.append(f"{label}: empty title_zh")
        elif not _contains_cjk(title):
            errors.append(f"{label}: title_zh must contain CJK characters")

        summary = resource.summary_zh.strip()
        if not summary:
            errors.append(f"{label}: empty summary")
        else:
            if not _contains_cjk(summary):
                errors.append(f"{label}: summary_zh must contain CJK characters")
            if len(summary) < 40:
                errors.append(f"{label}: summary must contain at least 40 Unicode code points")
            if len(summary) > 120:
                errors.append(f"{label}: summary must contain at most 120 Unicode code points")
            if not summary.endswith(("。", ".")):
                errors.append(f"{label}: summary must end with a Chinese or English period")

        normalized = _normalized_url(resource.url)
        if normalized in urls:
            errors.append(
                f"duplicate URL: {resource.id!r} and {urls[normalized]!r} normalize to {normalized}"
            )
        else:
            urls[normalized] = resource.id
    return errors
