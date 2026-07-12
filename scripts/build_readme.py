from __future__ import annotations

import argparse
import os
import re
import tempfile
from datetime import date
from pathlib import Path
from typing import Sequence

from scripts.resource_model import Resource, load_resources

START_MARKER = "<!-- AWESOME-VIBE:START -->"
END_MARKER = "<!-- AWESOME-VIBE:END -->"
README_PATH = Path("README.md")
DATA_PATH = Path("data/resources.yaml")

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


def render_resources(resources: list[Resource]) -> str:
    sections: list[str] = []
    for category in sorted({resource.category for resource in resources}, key=_category_sort_key):
        category_resources = sorted(
            (resource for resource in resources if resource.category == category), key=_sort_key
        )
        label = _category_label(category)
        lines = [f"## {label}", ""]
        for resource in category_resources:
            source = resource.source
            if resource.published_at is not None:
                source = f"{source} · {resource.published_at.isoformat()}"
            lines.append(
                f"- [{resource.title_zh}]({resource.url}) — {resource.summary_zh}（{source}）"
            )
        sections.append("\n".join(lines))
    return "\n\n".join(sections) + "\n"


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

    current = README_PATH.read_text(encoding="utf-8")
    expected = replace_generated_section(current, render_resources(load_resources(DATA_PATH)))
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
