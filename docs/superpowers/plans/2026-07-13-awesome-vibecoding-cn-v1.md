# Awesome Vibe Coding 中文资源库 V1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 建立一个以中文 README 为公开入口、以结构化数据为事实来源、可由 Agent 持续检索和扩充内容的 Vibe Coding 资源库第一版。

**Architecture:** `data/resources.yaml` 保存规范化资源，`scripts/build_readme.py` 通过稳定标记更新 README 的资源区，`scripts/validate.py` 检查 schema、URL、日期、ID 和重复项。首版人工核验的内容写入 YAML，项目文档和 `AGENTS.md` 定义开放式发现与发布流程，GitHub Actions 只做质量检查。

**Tech Stack:** Python 3.11+、PyYAML、pytest、Ruff、Markdown、GitHub Actions、Lychee

## Global Constraints

- `README.md` 是 GitHub 首页的中文主入口，不能退化为只含链接的跳转页。
- 来源和分类是种子集合而非白名单；发现新优质内容时允许扩充来源与分类。
- 每条资源必须有可核验原始 URL、中文标题和独立撰写的中文摘要。
- 不绕过登录墙或反爬，不保存账号凭据、Cookie、付费内容或非公开个人信息。
- 生成脚本不调用外部模型，重复运行必须不产生 diff。
- GitHub Actions 只验证内容，不自动采集或发布。

---

### Task 1: 数据模型、验证器与 README 生成器

**Files:**
- Create: `pyproject.toml`
- Create: `data/resources.yaml`
- Create: `scripts/__init__.py`
- Create: `scripts/resource_model.py`
- Create: `scripts/validate.py`
- Create: `scripts/build_readme.py`
- Create: `tests/test_resources.py`
- Create: `tests/test_readme.py`
- Modify: `README.md`

**Interfaces:**
- Produces: `load_resources(path: Path) -> list[Resource]`
- Produces: `validate_resources(resources: list[Resource]) -> list[str]`
- Produces: `render_resources(resources: list[Resource]) -> str`
- Produces CLI: `python -m scripts.validate`
- Produces CLI: `python -m scripts.build_readme --check`

- [ ] **Step 1: 写失败的数据验证测试**

```python
from pathlib import Path

from scripts.resource_model import load_resources, validate_resources


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
```

- [ ] **Step 2: 运行测试确认因模块不存在而失败**

Run: `python -m pytest tests/test_resources.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'scripts.resource_model'`.

- [ ] **Step 3: 实现不可变资源模型、YAML 加载和完整验证**

```python
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
```

验证器必须报告缺失字段、非 HTTPS URL、无主机名、未来日期、重复 ID、规范化后的重复 URL、缺少中文字符的中文标题/摘要、空摘要和摘要末尾缺少中文或英文句号。分类是开放字段：已知分类使用固定中文标签和首页顺序，新分类使用安全可读的回退标题并按名称确定性排序，不能被拒绝或在渲染时丢弃。规范化规则移除 URL fragment、移除 `utm_*`/`urlSource` 等追踪参数、统一主机名小写并移除尾部 `/`。

- [ ] **Step 4: 写失败的确定性渲染与同步测试**

```python
def test_render_is_deterministic() -> None:
    resources = load_resources(Path("data/resources.yaml"))
    assert render_resources(resources) == render_resources(list(reversed(resources)))


def test_readme_is_in_sync() -> None:
    expected = replace_generated_section(
        Path("README.md").read_text(encoding="utf-8"),
        render_resources(load_resources(Path("data/resources.yaml"))),
    )
    assert expected == Path("README.md").read_text(encoding="utf-8")
```

- [ ] **Step 5: 实现 README 稳定标记渲染**

README 使用 `<!-- AWESOME-VIBE:START -->` 与 `<!-- AWESOME-VIBE:END -->`。资源按 `featured`、`published_at`、`added_at`、`title_zh` 确定性排序，按分类生成二级标题与 Markdown 列表。每项格式为：

```markdown
- [中文标题](原始URL) — 中文摘要（来源 · YYYY-MM-DD）
```

未知发布日期只显示来源，不虚构日期。`--check` 在 README 不同步时退出码为 1，默认模式原子化更新 README。

- [ ] **Step 6: 配置项目工具并运行验证**

`pyproject.toml` 配置 Python `>=3.11`、PyYAML、pytest、Ruff，Ruff 行宽 100。运行：

```powershell
python -m pip install -e ".[dev]"
python -m pytest -q
python -m ruff check .
python -m scripts.validate
python -m scripts.build_readme --check
```

Expected: all commands exit 0.

- [ ] **Step 7: 提交基础内容引擎**

```powershell
git add pyproject.toml data scripts tests README.md
git commit -m "feat: add structured resource catalog"
```

### Task 2: 第一版丰富内容目录

**Files:**
- Modify: `data/resources.yaml`
- Modify: `README.md`
- Test: `tests/test_resources.py`

**Interfaces:**
- Consumes: Task 1 的资源 schema 和生成 CLI
- Produces: 足够丰富、可核验并可在 README 直接浏览的首版目录

- [ ] **Step 1: 加入首版丰富度失败测试**

```python
def test_v1_has_broad_coverage() -> None:
    resources = load_resources(Path("data/resources.yaml"))
    required = {"skills", "repos", "tools", "companies", "articles", "tutorials", "community", "research"}
    assert required <= {item.category for item in resources}
    assert len(resources) >= 80
    assert sum(item.language == "zh" for item in resources) >= 20
    assert sum(item.featured for item in resources) >= 12
```

- [ ] **Step 2: 运行测试确认丰富度不足**

Run: `python -m pytest tests/test_resources.py::test_v1_has_broad_coverage -q`
Expected: FAIL on resource count or category coverage.

- [ ] **Step 3: 合并三路 Agent 候选并人工核验**

至少收录 80 条，八个核心分类均有内容。优先原始仓库、官方文档、论文和原帖；中文社区条目保留 Datawhale、LinuxDo、V2EX、牛客等高质量候选。剔除疑似软文、无法核验转载、登录后才可访问的页面和重复事件。英文内容写中文标题与摘要，但保留原始标题字段。

- [ ] **Step 4: 生成 README 并检查首页可读性**

Run: `python -m scripts.build_readme`
Expected: README 最新内容区与八个分类全部生成，目录锚点有效，中文摘要在 GitHub Markdown 中无乱码。

- [ ] **Step 5: 运行内容验证**

```powershell
python -m scripts.validate
python -m scripts.build_readme --check
python -m pytest -q
```

Expected: all commands exit 0; running `python -m scripts.build_readme` again leaves `git diff` unchanged.

- [ ] **Step 6: 提交首版内容**

```powershell
git add data/resources.yaml README.md tests/test_resources.py
git commit -m "content: publish initial Chinese vibe coding guide"
```

### Task 3: 维护经验、贡献规则与开放式发现指南

**Files:**
- Create: `AGENTS.md`
- Create: `CONTRIBUTING.md`
- Create: `docs/content-guidelines.md`
- Create: `docs/sources.md`
- Create: `docs/maintenance.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: Task 1 的 CLI 与 Task 2 的分类实践
- Produces: 新 Agent 无历史上下文也能执行的完整维护工作流

- [ ] **Step 1: 编写 `AGENTS.md` 仓库级指南**

必须包含：项目使命、README-first 原则、开放式发现、来源非白名单、并行检索域、原始来源优先、时间窗口、质量门槛、中文摘要风格、事实/观点/厂商宣称区分、去重步骤、数据字段说明、生成命令、验证命令、diff 审阅、提交推送规范，以及“发现新类别或稳定优质来源时同步扩展数据枚举和 `docs/sources.md`”的明确要求。

- [ ] **Step 2: 编写贡献与内容规范**

`CONTRIBUTING.md` 给出提交单条资源的字段示例和本地验证命令。`docs/content-guidelines.md` 规定摘要长度 40—120 个中文字符、禁用空泛营销词、不得大段翻译原文、未知日期留空、互动数字必须注明核验日期。

- [ ] **Step 3: 编写来源地图与维护手册**

`docs/sources.md` 按官方/代码托管/中文社区/国际社区/研究/搜索发现列出种子来源、推荐搜索式和限制，并明确持续添加新来源。`docs/maintenance.md` 将维护流程写成可勾选清单，包括最近 30 天搜索、90 天遗漏回看、引用追踪、链接核验、生成、测试、diff、提交和推送。

- [ ] **Step 4: 在 README 添加贡献与维护入口**

README 人工区链接到 `CONTRIBUTING.md`、内容规范、来源地图和维护手册，并说明读者可通过 Issue/PR 推荐未列出的优质来源。

- [ ] **Step 5: 验证文档和提交**

Run: `python -m scripts.build_readme && python -m scripts.build_readme --check && git diff --check`
Expected: exit 0 and no whitespace errors.

```powershell
git add AGENTS.md CONTRIBUTING.md docs README.md
git commit -m "docs: add sustainable curation workflow"
```

### Task 4: GitHub 协作与持续质量检查

**Files:**
- Create: `.github/ISSUE_TEMPLATE/resource.yml`
- Create: `.github/ISSUE_TEMPLATE/broken-link.yml`
- Create: `.github/pull_request_template.md`
- Create: `.github/workflows/quality.yml`
- Create: `.lycheeignore`
- Create: `LICENSE`

**Interfaces:**
- Consumes: Task 1 的安装、验证和生成检查命令
- Produces: PR/push 上的 Python 内容检查与 Lychee 链接检查

- [ ] **Step 1: 添加资源推荐与失效链接 Issue 表单**

资源表单要求原文 URL、建议分类、推荐理由、原文日期和利益关系披露。失效链接表单要求 README 条目、失效 URL、观察到的状态和可选替代链接。

- [ ] **Step 2: 添加 PR 模板与 MIT License**

PR 清单覆盖原始来源、中文摘要、日期核验、非重复、生成 README、完整验证和商业关系披露。`LICENSE` 使用 2026 Scourgen 的标准 MIT 文本。

- [ ] **Step 3: 添加质量工作流**

工作流在 `pull_request` 和推送到 `main` 时运行，使用 Python 3.11，执行：

```yaml
- run: python -m pip install -e ".[dev]"
- run: python -m ruff check .
- run: python -m pytest -q
- run: python -m scripts.validate
- run: python -m scripts.build_readme --check
```

Lychee 使用固定主版本并读取 `.lycheeignore`；只忽略明确会阻止 CI 的已知动态站点，不全局忽略社区域名。

- [ ] **Step 4: 本地检查 YAML 与完整测试**

```powershell
python -c "import yaml; yaml.safe_load(open('.github/workflows/quality.yml', encoding='utf-8'))"
python -m pytest -q
python -m ruff check .
python -m scripts.validate
python -m scripts.build_readme --check
git diff --check
```

Expected: all commands exit 0.

- [ ] **Step 5: 提交协作配置**

```powershell
git add .github .lycheeignore LICENSE
git commit -m "ci: validate catalog and links"
```

### Task 5: 完整验证、记忆更新与发布

**Files:**
- Modify if needed: files failing verification only
- Create or update outside repository: `D:\Codex-Memory\Projects\Index.md`
- Create outside repository: `D:\Codex-Memory\Projects\awesome-vibecoding-cn.md`

**Interfaces:**
- Consumes: Tasks 1—4 全部产物
- Produces: 已验证并推送到 `origin/main` 的 V1

- [ ] **Step 1: 运行完整验证**

```powershell
python -m scripts.build_readme
python -m scripts.build_readme --check
python -m scripts.validate
python -m pytest -q
python -m ruff check .
git diff --check
git status --short
```

Expected: checks exit 0; only intentional files are modified; a second build produces no diff.

- [ ] **Step 2: 审阅提交历史和远程差异**

Run: `git log --oneline origin/main..HEAD` and `git diff --stat origin/main...HEAD`
Expected: only design, catalog, documentation and CI commits are present.

- [ ] **Step 3: 更新长期项目记忆**

在 `Projects/Index.md` 为规范化路径 `E:\code\awesome-vibecoding-cn` 保持唯一映射。项目笔记记录：README-first、人工触发维护、结构化数据生成、开放式来源发现、Agent 并行检索和验证后推送的稳定工作流；不记录临时候选清单或原始日志。

- [ ] **Step 4: 推送当前分支**

Run: `git push origin main`
Expected: remote reports successful update and `git status --branch --short` shows `main...origin/main` with no ahead/behind count.
