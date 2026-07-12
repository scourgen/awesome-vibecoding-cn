from __future__ import annotations

import argparse
import os
import re
import tempfile
from datetime import date
from pathlib import Path
from typing import Sequence

from scripts.resource_model import CatalogFormatError, Resource, load_resources, validate_resources

START_MARKER = "<!-- AWESOME-VIBE:START -->"
END_MARKER = "<!-- AWESOME-VIBE:END -->"
README_PATH = Path("README.md")
DATA_PATH = Path("data/resources.yaml")
RECENT_LIMIT = 10

CATEGORY_LABELS = {
    "skills": "Agent 技能",
    "repos": "开源项目",
    "tools": "工具",
    "companies": "公司与产品",
    "articles": "文章",
    "tutorials": "教程",
    "community": "社区",
    "research": "研究",
}


def _sort_key(resource: Resource) -> tuple[int, int, int, str, str, str]:
    published = resource.published_at or date.min
    return (
        -int(resource.featured),
        -published.toordinal(),
        -resource.added_at.toordinal(),
        resource.title_zh,
        resource.id,
        resource.url,
    )


def _category_sort_key(category: str) -> tuple[int, int, str, str]:
    known_categories = tuple(CATEGORY_LABELS)
    if category in CATEGORY_LABELS:
        return (0, known_categories.index(category), "", "")
    return (1, len(known_categories), category.casefold(), category)


def _category_label(category: str) -> str:
    if category in CATEGORY_LABELS:
        return CATEGORY_LABELS[category]
    readable = re.sub(r"[^0-9A-Za-z\u3400-\u9fff]+", " ", category).strip()
    return readable.title() or "其他"


def _heading_anchor(label: str) -> str:
    anchor = re.sub(r"[^\w\- ]", "", label.casefold())
    return re.sub(r" +", "-", anchor.strip())


def _render_resource(resource: Resource) -> str:
    source = resource.source
    if resource.published_at is not None:
        source = f"{source} · {resource.published_at.isoformat()}"
    marker = "⭐ **精选** " if resource.featured else ""
    return f"- {marker}[{resource.title_zh}]({resource.url}) — {resource.summary_zh}（{source}）"


def render_resources(resources: list[Resource]) -> str:
    last_updated = max((resource.added_at for resource in resources), default=None)
    updated_label = last_updated.isoformat() if last_updated is not None else "暂无资源"
    metadata = [
        f"**最后更新时间：{updated_label}**",
        "",
        "收录原则：公开可核验的原始 URL、中文摘要、人工审核。",
    ]
    categories = sorted({resource.category for resource in resources}, key=_category_sort_key)
    directory = ["## 分类目录", ""]
    directory.extend(
        f"- [{_category_label(category)}](#{_heading_anchor(_category_label(category))})"
        for category in categories
    )

    recent_resources = sorted(
        (resource for resource in resources if resource.published_at is not None),
        key=lambda resource: (
            -resource.published_at.toordinal(),
            resource.title_zh,
            resource.id,
            resource.url,
        ),
    )[:RECENT_LIMIT]
    recent = ["## 最近更新", "", *(_render_resource(resource) for resource in recent_resources)]

    sections: list[str] = []
    for category in categories:
        category_resources = sorted(
            (resource for resource in resources if resource.category == category), key=_sort_key
        )
        label = _category_label(category)
        lines = [f"## {label}", ""]
        lines.extend(_render_resource(resource) for resource in category_resources)
        sections.append("\n".join(lines))
    return "\n\n".join(
        ["\n".join(metadata), "\n".join(directory), "\n".join(recent), *sections]
    ) + "\n"


def replace_generated_section(readme: str, rendered: str) -> str:
    if readme.count(START_MARKER) != 1 or readme.count(END_MARKER) != 1:
        raise ValueError("README must contain exactly one generated-section marker pair")
    start = readme.index(START_MARKER)
    end = readme.index(END_MARKER, start) + len(END_MARKER)
    if end <= start:
        raise ValueError("README generated-section markers are out of order")
    replacement = f"{START_MARKER}\n{rendered.rstrip()}\n{END_MARKER}"
    return readme[:start] + replacement + readme[end:]


def _atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False, newline=""
    ) as temporary:
        temporary.write(content)
        temporary_path = Path(temporary.name)
    try:
        os.replace(temporary_path, path)
    finally:
        temporary_path.unlink(missing_ok=True)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render structured resources into README.md")
    parser.add_argument("--check", action="store_true", help="fail if README.md is out of sync")
    args = parser.parse_args(argv)

    try:
        resources = load_resources(DATA_PATH)
        errors = validate_resources(resources)
        if errors:
            for error in errors:
                print(error)
            return 1
        current = README_PATH.read_text(encoding="utf-8")
    except (CatalogFormatError, OSError) as error:
        print(f"Catalog error: {error}")
        return 1
    expected = replace_generated_section(current, render_resources(resources))
    if args.check:
        if current != expected:
            print("README.md is out of sync; run python -m scripts.build_readme")
            return 1
        return 0

    if current != expected:
        _atomic_write(README_PATH, expected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
