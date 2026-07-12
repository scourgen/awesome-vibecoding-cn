# Final review fix report

Date: 2026-07-13
Implementation commit: `32e276a` (`fix: harden catalog validation and metadata`)

## Findings mapping

1. Summary length
   - `validate_resources` now measures `len(summary_zh.strip())`, which is Python's Unicode code point count, and enforces the inclusive 40–120 range.
   - Tests cover the lower bound, upper bound, and all seed data.
   - Expanded all 63 summaries that were below 40 code points while retaining the original factual attribution and adding category-appropriate scope/use context.
   - Updated `AGENTS.md`, `CONTRIBUTING.md`, and `docs/content-guidelines.md` to state the exact counting rule.
   - Regenerated `README.md` from `data/resources.yaml`.

2. Schema and safe CLI behavior
   - Added `CatalogFormatError` for malformed YAML and invalid catalog containers.
   - Added `Resource._schema_errors` and safe coercion defaults so non-mapping entries, wrong field types, and invalid dates are reported rather than rendered or allowed to raise tracebacks.
   - Enforced non-empty strings for `id`, `title_zh`, `title_original`, `url`, `category`, `source`, `language`, and `summary_zh`; non-empty string lists for `tags`; exact booleans for `featured`; optional valid `published_at`; and required valid `added_at`.
   - `scripts.validate` and `scripts.build_readme` now catch catalog/IO errors and exit 1 with actionable messages. README generation validates the complete catalog before rendering.
   - Kept categories open-ended; the existing new-category test remains green.

3. README generated metadata
   - Added a generated `最后更新时间` derived deterministically from `max(added_at)`.
   - Added the generated collection principle line: public, verifiable original URLs; Chinese summaries; human review.
   - Empty catalogs render `暂无资源` without guessing a date.
   - Added deterministic metadata and empty-catalog tests, then regenerated `README.md`.

## TDD evidence

RED test command:

```powershell
python -m pytest -q tests/test_resources.py tests/test_readme.py
```

The first collection attempt exposed the intentionally missing `CatalogFormatError` import; the test was rewired to reference the wished-for API at runtime. The resulting behavioral RED run produced:

```text
19 failed, 24 passed in 1.46s
```

Failures matched the requested missing behavior: summary limits, YAML/container/entry/schema safety, CLI traceback prevention, README metadata, and invalid-data render prevention.

GREEN test command:

```powershell
python -m pytest -q tests/test_resources.py tests/test_readme.py
```

Result:

```text
43 passed in 1.21s
```

## Summary audit

Command audited all loaded resources using `len(summary_zh.strip())` and the required terminal period.

```text
summaries=88 min=40 max=75 noncompliant=0
```

## Final verification

- Repeated `python -m scripts.build_readme` twice and compared the full `git diff -- README.md` strings byte-for-byte at the PowerShell string level: stable (`24866` diff characters at that point).
- `python -m scripts.build_readme --check`: exit 0.
- `python -m scripts.validate`: `Validated 88 resources`.
- `python -m pytest -q`: `43 passed in 1.13s`.
- `python -m ruff check .`: `All checks passed!`.
- `git diff --check`: exit 0.
- Official Lychee `0.24.2`, `--verbose --no-progress --retry-wait-time 2 './**/*.md'`: `112 Total`, `100 Unique`, `94 OK`, `0 Errors`, `18 Excluded`, `7 Redirects`.

The initial Lychee scan had two transient Vercel connection failures. The required retry succeeded with zero errors; no link or ignore-list changes were made.
