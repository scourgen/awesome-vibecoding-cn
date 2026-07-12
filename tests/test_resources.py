from dataclasses import replace
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

from scripts import resource_model
from scripts.resource_model import Resource, load_resources, validate_resources
from scripts import validate


def make_resource(**changes: object) -> Resource:
    resource = Resource(
        id="example",
        title_zh="示例资源",
        title_original="Example",
        url="https://example.com/post",
        category="articles",
        source="Example",
        published_at=date(2026, 1, 1),
        added_at=date(2026, 7, 13),
        language="en",
        summary_zh="这是一条用于测试目录校验行为的有效中文摘要，能够覆盖字符长度、内容类型和句号结尾等要求。",
        tags=("example",),
        featured=False,
    )
    return replace(resource, **changes)


def test_seed_resources_are_valid() -> None:
    resources = load_resources(Path("data/resources.yaml"))
    assert len(resources) >= 1
    assert validate_resources(resources) == []


def test_seed_summaries_are_40_to_120_unicode_code_points() -> None:
    resources = load_resources(Path("data/resources.yaml"))

    assert all(40 <= len(resource.summary_zh.strip()) <= 120 for resource in resources)


def test_v1_has_broad_coverage() -> None:
    resources = load_resources(Path("data/resources.yaml"))
    required = {
        "skills",
        "repos",
        "tools",
        "companies",
        "articles",
        "tutorials",
        "community",
        "research",
    }
    assert required <= {item.category for item in resources}
    assert len(resources) >= 80
    assert sum(item.language == "zh" for item in resources) >= 20
    assert sum(item.featured for item in resources) >= 12


def test_metr_publication_date_matches_arxiv_submission() -> None:
    resources = load_resources(Path("data/resources.yaml"))
    metr = next(item for item in resources if item.id == "metr-productivity")

    assert metr.published_at == date(2025, 7, 12)


def test_duplicate_urls_are_rejected(tmp_path: Path) -> None:
    data = tmp_path / "resources.yaml"
    data.write_text(
        """resources:
  - &item
    id: one
    title_zh: 示例资源
    title_original: Example
    url: https://example.com/post?utm_source=test
    category: articles
    source: Example
    published_at: 2026-01-01
    added_at: 2026-07-13
    language: en
    summary_zh: 这是一个用于验证重复链接检测的示例资源。
    tags: [example]
    featured: false
  - <<: *item
    id: two
    url: https://example.com/post#section
""",
        encoding="utf-8",
    )
    errors = validate_resources(load_resources(data))
    assert any("duplicate URL" in error for error in errors)


def test_missing_fields_are_reported(tmp_path: Path) -> None:
    data = tmp_path / "resources.yaml"
    data.write_text(
        """resources:
  - id: incomplete
    url: https://example.com/incomplete
""",
        encoding="utf-8",
    )

    errors = validate_resources(load_resources(data))

    assert any("missing field: title_zh" in error for error in errors)
    assert any("missing field: added_at" in error for error in errors)


def test_non_https_urls_are_rejected() -> None:
    errors = validate_resources([make_resource(url="http://example.com/post")])
    assert any("HTTPS" in error for error in errors)


def test_urls_without_a_hostname_are_rejected() -> None:
    errors = validate_resources([make_resource(url="https:///post")])
    assert any("hostname" in error for error in errors)


def test_future_dates_are_rejected() -> None:
    tomorrow = resource_model._catalog_today() + timedelta(days=1)
    errors = validate_resources([make_resource(published_at=tomorrow, added_at=tomorrow)])
    assert any("future published_at" in error for error in errors)
    assert any("future added_at" in error for error in errors)


def test_catalog_today_uses_maintainer_timezone() -> None:
    utc_evening = datetime(2026, 7, 12, 18, 53, tzinfo=timezone.utc)

    assert resource_model._catalog_today(utc_evening) == date(2026, 7, 13)


def test_duplicate_ids_are_rejected() -> None:
    errors = validate_resources(
        [make_resource(), make_resource(url="https://example.com/another")]
    )
    assert any("duplicate ID" in error for error in errors)


def test_url_normalization_removes_tracking_and_trailing_slash() -> None:
    errors = validate_resources(
        [
            make_resource(url="https://EXAMPLE.com/post/?urlSource=feed&keep=yes"),
            make_resource(id="another", url="https://example.com/post?keep=yes#section"),
        ]
    )
    assert any("duplicate URL" in error for error in errors)


def test_url_normalization_removes_common_click_identifiers() -> None:
    errors = validate_resources(
        [
            make_resource(url="https://example.com/post?gclid=google&fbclid=facebook"),
            make_resource(id="another", url="https://example.com/post"),
        ]
    )
    assert any("duplicate URL" in error for error in errors)


def test_new_categories_are_allowed() -> None:
    assert validate_resources([make_resource(category="case-studies")]) == []


def test_titles_must_be_nonempty_and_contain_cjk() -> None:
    empty_errors = validate_resources([make_resource(title_zh="  ")])
    english_errors = validate_resources([make_resource(title_zh="English only")])

    assert any("empty title_zh" in error for error in empty_errors)
    assert any("title_zh must contain CJK" in error for error in english_errors)


def test_empty_summaries_are_rejected() -> None:
    errors = validate_resources([make_resource(summary_zh="  ")])
    assert any("empty summary" in error for error in errors)


def test_summaries_must_contain_cjk() -> None:
    errors = validate_resources([make_resource(summary_zh="English only.")])
    assert any("summary_zh must contain CJK" in error for error in errors)


def test_summaries_must_end_with_a_period() -> None:
    errors = validate_resources([make_resource(summary_zh="缺少结尾句号")])
    assert any("period" in error for error in errors)


def test_summaries_must_be_at_least_40_unicode_code_points() -> None:
    summary = "中" * 38 + "。"

    errors = validate_resources([make_resource(summary_zh=summary)])

    assert any("at least 40 Unicode code points" in error for error in errors)


def test_summaries_must_not_exceed_120_unicode_code_points() -> None:
    summary = "中" * 120 + "。"

    errors = validate_resources([make_resource(summary_zh=summary)])

    assert any("at most 120 Unicode code points" in error for error in errors)


def test_malformed_yaml_raises_actionable_catalog_error(tmp_path: Path) -> None:
    data = tmp_path / "resources.yaml"
    data.write_text("resources: [\n", encoding="utf-8")

    with pytest.raises(resource_model.CatalogFormatError, match="invalid YAML"):
        load_resources(data)


@pytest.mark.parametrize(
    ("content", "message"),
    [
        ("- not-a-mapping\n", "top level must be a mapping"),
        ("resources: {}\n", "resources must be a list"),
    ],
)
def test_catalog_container_types_are_checked(
    tmp_path: Path, content: str, message: str
) -> None:
    data = tmp_path / "resources.yaml"
    data.write_text(content, encoding="utf-8")

    with pytest.raises(resource_model.CatalogFormatError, match=message):
        load_resources(data)


def test_non_mapping_resource_is_reported_without_crashing(tmp_path: Path) -> None:
    data = tmp_path / "resources.yaml"
    data.write_text("resources:\n  - not-a-mapping\n", encoding="utf-8")

    errors = validate_resources(load_resources(data))

    assert any("resource #1: entry must be a mapping" in error for error in errors)


@pytest.mark.parametrize(
    ("field", "yaml_value", "message"),
    [
        ("id", "123", "id must be a non-empty string"),
        ("title_original", "''", "title_original must be a non-empty string"),
        ("source", "[]", "source must be a non-empty string"),
        ("tags", "example", "tags must be a non-empty list of strings"),
        ("tags", "[example, 2]", "tags must be a non-empty list of strings"),
        ("featured", "'false'", "featured must be a boolean"),
        ("published_at", "not-a-date", "published_at must be a valid YYYY-MM-DD date"),
        ("added_at", "not-a-date", "added_at must be a valid YYYY-MM-DD date"),
    ],
)
def test_invalid_field_types_are_reported(
    tmp_path: Path, field: str, yaml_value: str, message: str
) -> None:
    data = tmp_path / "resources.yaml"
    values = {
        "id": "example",
        "title_zh": "示例资源",
        "title_original": "Example",
        "url": "https://example.com/post",
        "category": "articles",
        "source": "Example",
        "published_at": "2026-01-01",
        "added_at": "2026-07-13",
        "language": "en",
        "summary_zh": "这是一条用于测试目录字段类型检查的中文摘要，能够确保异常输入被安全报告。",
        "tags": "[example]",
        "featured": "false",
    }
    values[field] = yaml_value
    body = "\n".join(f"    {name}: {value}" for name, value in values.items())
    data.write_text(f"resources:\n  -\n{body}\n", encoding="utf-8")

    errors = validate_resources(load_resources(data))

    assert any(message in error for error in errors)


def test_validate_cli_fails_for_invalid_data(
    tmp_path: Path, monkeypatch, capsys: pytest.CaptureFixture[str]
) -> None:
    data = tmp_path / "resources.yaml"
    data.write_text("resources:\n  - id: incomplete\n", encoding="utf-8")
    monkeypatch.setattr(validate, "DATA_PATH", data)

    assert validate.main([]) == 1
    assert "Traceback" not in capsys.readouterr().out


def test_validate_cli_reports_malformed_yaml_without_traceback(
    tmp_path: Path, monkeypatch, capsys: pytest.CaptureFixture[str]
) -> None:
    data = tmp_path / "resources.yaml"
    data.write_text("resources: [\n", encoding="utf-8")
    monkeypatch.setattr(validate, "DATA_PATH", data)

    assert validate.main([]) == 1
    output = capsys.readouterr().out
    assert "invalid YAML" in output
    assert "Traceback" not in output
