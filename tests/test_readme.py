from dataclasses import replace
from datetime import date, timedelta
from pathlib import Path

from scripts import build_readme
from scripts.build_readme import render_resources, replace_generated_section
from scripts.resource_model import load_resources


def test_render_is_deterministic() -> None:
    resource = load_resources(Path("data/resources.yaml"))[0]
    new_category = replace(
        resource,
        id="case-study",
        title_zh="案例研究",
        url="https://example.com/case-study",
        category="case-studies",
        featured=False,
    )
    resources = [resource, new_category]

    assert render_resources(resources) == render_resources(list(reversed(resources)))
    assert "## Case Studies" in render_resources(resources)
    assert "[案例研究](https://example.com/case-study)" in render_resources(resources)


def test_render_includes_clickable_directory_for_known_and_open_categories() -> None:
    resource = load_resources(Path("data/resources.yaml"))[0]
    skill = replace(resource, id="skill", category="skills")
    case_study = replace(
        resource,
        id="case-study",
        title_zh="案例研究",
        url="https://example.com/case-study",
        category="case-studies",
    )

    rendered = render_resources([case_study, skill])

    assert "## 分类目录" in rendered
    assert "- [Agent 技能](#agent-技能)" in rendered
    assert "- [Case Studies](#case-studies)" in rendered


def test_render_includes_deterministic_catalog_metadata() -> None:
    resource = load_resources(Path("data/resources.yaml"))[0]
    older = replace(resource, id="older", added_at=date(2026, 7, 1))
    newer = replace(resource, id="newer", added_at=date(2026, 7, 12))

    rendered = render_resources([newer, older])

    assert "**最后更新时间：2026-07-12**" in rendered
    assert "收录原则：公开可核验的原始 URL、中文摘要、人工审核。" in rendered


def test_render_empty_catalog_has_explicit_metadata_and_no_date_guess() -> None:
    rendered = render_resources([])

    assert "**最后更新时间：暂无资源**" in rendered
    assert "收录原则：公开可核验的原始 URL、中文摘要、人工审核。" in rendered
    assert "## 分类目录" in rendered
    assert "## 最近更新" in rendered


def test_render_recent_updates_uses_ten_latest_known_dates() -> None:
    resource = load_resources(Path("data/resources.yaml"))[0]
    dated = [
        replace(
            resource,
            id=f"dated-{offset}",
            title_zh=f"日期资源 {offset}",
            url=f"https://example.com/dated-{offset}",
            published_at=date(2026, 1, 1) + timedelta(days=offset),
            featured=False,
        )
        for offset in range(12)
    ]
    unknown = replace(
        resource,
        id="unknown",
        title_zh="未知日期资源",
        url="https://example.com/unknown",
        published_at=None,
        featured=False,
    )

    rendered = render_resources([unknown, *reversed(dated)])
    recent = rendered.split("## 最近更新\n", 1)[1].split("\n## ", 1)[0]

    assert recent.count("\n-") == 10
    assert recent.index("日期资源 11") < recent.index("日期资源 10")
    assert "[日期资源 2](" in recent
    assert "[日期资源 1](" not in recent
    assert "[日期资源 0](" not in recent
    assert "未知日期资源" not in recent


def test_render_marks_featured_resources_explicitly() -> None:
    resource = load_resources(Path("data/resources.yaml"))[0]
    regular = replace(
        resource,
        id="regular",
        title_zh="普通资源",
        url="https://example.com/regular",
        featured=False,
    )

    rendered = render_resources([regular, resource])

    assert "- ⭐ **精选** [Claude Code 开源仓库]" in rendered
    assert "- [普通资源]" in rendered
    assert "- ⭐ **精选** [普通资源]" not in rendered


def test_readme_is_in_sync() -> None:
    expected = replace_generated_section(
        Path("README.md").read_text(encoding="utf-8"),
        render_resources(load_resources(Path("data/resources.yaml"))),
    )
    assert expected == Path("README.md").read_text(encoding="utf-8")


def test_render_formats_known_and_unknown_publication_dates() -> None:
    resource = load_resources(Path("data/resources.yaml"))[0]
    dated = replace(
        resource,
        id="dated",
        title_zh="有日期资源",
        url="https://example.com/dated",
        published_at=date(2026, 1, 2),
        featured=False,
    )

    rendered = render_resources([dated, resource])

    assert (
        "- ⭐ **精选** [Claude Code 开源仓库](https://github.com/anthropics/claude-code) — "
        "Anthropic 的终端编程代理仓库，包含安装说明、使用入口与问题反馈渠道，"
        "便于读者核对其功能范围、配置方式与适用场景。"
        "（Anthropic）"
    ) in rendered
    assert (
        "- [有日期资源](https://example.com/dated) — "
        "Anthropic 的终端编程代理仓库，包含安装说明、使用入口与问题反馈渠道，"
        "便于读者核对其功能范围、配置方式与适用场景。"
        "（Anthropic · 2026-01-02）"
    ) in rendered
    tools_section = rendered.split("## 工具\n", 1)[1]
    assert tools_section.index("Claude Code 开源仓库") < tools_section.index("有日期资源")


def test_check_mode_detects_and_default_mode_repairs_drift(tmp_path: Path, monkeypatch) -> None:
    readme = tmp_path / "README.md"
    readme.write_text(
        "# Catalog\n\n<!-- AWESOME-VIBE:START -->\n<!-- AWESOME-VIBE:END -->\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(build_readme, "README_PATH", readme)
    monkeypatch.setattr(build_readme, "DATA_PATH", Path("data/resources.yaml"))

    assert build_readme.main(["--check"]) == 1
    assert build_readme.main([]) == 0
    assert build_readme.main(["--check"]) == 0


def test_build_cli_rejects_invalid_catalog_without_rendering(
    tmp_path: Path, monkeypatch, capsys
) -> None:
    readme = tmp_path / "README.md"
    data = tmp_path / "resources.yaml"
    original = "# Catalog\n\n<!-- AWESOME-VIBE:START -->\nold\n<!-- AWESOME-VIBE:END -->\n"
    readme.write_text(original, encoding="utf-8")
    data.write_text(
        "resources:\n  - id: 123\n    featured: 'false'\n    tags: example\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(build_readme, "README_PATH", readme)
    monkeypatch.setattr(build_readme, "DATA_PATH", data)

    assert build_readme.main([]) == 1
    output = capsys.readouterr().out
    assert "id must be a non-empty string" in output
    assert "Traceback" not in output
    assert readme.read_text(encoding="utf-8") == original
