from dataclasses import replace
from datetime import date, timedelta
from pathlib import Path

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
        summary_zh="这是一条有效的中文摘要。",
        tags=("example",),
        featured=False,
    )
    return replace(resource, **changes)


def test_seed_resources_are_valid() -> None:
    resources = load_resources(Path("data/resources.yaml"))
    assert len(resources) >= 1
    assert validate_resources(resources) == []


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
    tomorrow = date.today() + timedelta(days=1)
    errors = validate_resources([make_resource(published_at=tomorrow, added_at=tomorrow)])
    assert any("future published_at" in error for error in errors)
    assert any("future added_at" in error for error in errors)


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


def test_unknown_categories_are_rejected() -> None:
    errors = validate_resources([make_resource(category="unknown")])
    assert any("unknown category" in error for error in errors)


def test_empty_summaries_are_rejected() -> None:
    errors = validate_resources([make_resource(summary_zh="  ")])
    assert any("empty summary" in error for error in errors)


def test_summaries_must_end_with_a_period() -> None:
    errors = validate_resources([make_resource(summary_zh="缺少结尾句号")])
    assert any("period" in error for error in errors)


def test_validate_cli_fails_for_invalid_data(tmp_path: Path, monkeypatch) -> None:
    data = tmp_path / "resources.yaml"
    data.write_text("resources:\n  - id: incomplete\n", encoding="utf-8")
    monkeypatch.setattr(validate, "DATA_PATH", data)

    assert validate.main([]) == 1
