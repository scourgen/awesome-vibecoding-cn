from dataclasses import replace
from datetime import date
from pathlib import Path

from scripts import build_readme
from scripts.build_readme import render_resources, replace_generated_section
from scripts.resource_model import load_resources


def test_render_is_deterministic() -> None:
    resources = load_resources(Path("data/resources.yaml"))
    assert render_resources(resources) == render_resources(list(reversed(resources)))


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
        "- [Claude Code 开源仓库](https://github.com/anthropics/claude-code) — "
        "Anthropic 的终端编程代理仓库，包含安装说明、使用入口与问题反馈渠道。"
        "（Anthropic）"
    ) in rendered
    assert (
        "- [有日期资源](https://example.com/dated) — "
        "Anthropic 的终端编程代理仓库，包含安装说明、使用入口与问题反馈渠道。"
        "（Anthropic · 2026-01-02）"
    ) in rendered
    assert rendered.index("Claude Code 开源仓库") < rendered.index("有日期资源")


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
