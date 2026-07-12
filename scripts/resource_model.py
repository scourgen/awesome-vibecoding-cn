from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import yaml

ALLOWED_CATEGORIES = frozenset(
    {"skills", "repos", "tools", "companies", "articles", "tutorials", "community", "research"}
)
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
TRACKING_PARAMETERS = frozenset({"urlsource", "fbclid", "gclid"})


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


def _parse_date(value: date | str | None) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, date):
        return value
    return date.fromisoformat(value)


def load_resources(path: Path) -> list[Resource]:
    document = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return [
        Resource(
            id=item.get("id", ""),
            title_zh=item.get("title_zh", ""),
            title_original=item.get("title_original", ""),
            url=item.get("url", ""),
            category=item.get("category", ""),
            source=item.get("source", ""),
            published_at=_parse_date(item.get("published_at")),
            added_at=_parse_date(item.get("added_at")) or date.min,
            language=item.get("language", ""),
            summary_zh=item.get("summary_zh", ""),
            tags=tuple(item.get("tags", ())),
            featured=item.get("featured", False),
            _missing_fields=tuple(field for field in REQUIRED_FIELDS if field not in item),
        )
        for item in document.get("resources", [])
    ]


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
    today = date.today()
    for index, resource in enumerate(resources, start=1):
        label = resource.id or f"resource #{index}"
        errors.extend(f"{label}: missing field: {name}" for name in resource._missing_fields)

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

        if resource.category not in ALLOWED_CATEGORIES:
            errors.append(f"{label}: unknown category: {resource.category!r}")

        summary = resource.summary_zh.strip()
        if not summary:
            errors.append(f"{label}: empty summary")
        elif not summary.endswith(("。", ".")):
            errors.append(f"{label}: summary must end with a Chinese or English period")

        normalized = _normalized_url(resource.url)
        if normalized in urls:
            errors.append(
                f"duplicate URL: {resource.id!r} and {urls[normalized]!r} normalize to {normalized}"
            )
        else:
            urls[normalized] = resource.id
    return errors
