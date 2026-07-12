# 贡献指南

感谢帮助完善面向中文读者的 Vibe Coding 资源库。你可以通过 Issue 推荐链接，也可以直接提交 Pull Request。现有分类和来源只是种子集合：未列出的优质文章、项目、教程、产品、社区或研究同样欢迎，必要时可以提出新分类。

## 收录前检查

- 只提交官方页面、代码仓库、论文原文、作者或社区原帖等可公开核验的原始 URL；搜索结果、转载或聚合页只能用于发现，找不到原始 URL 就不收录。
- 链接应公开可访问并使用 HTTPS，不应要求维护者提供账号、Cookie 或绕过付费墙。
- 内容应与 AI 编程、智能体工作流、工具生态、工程质量或安全直接相关，并能为中文读者提供明确价值。
- 先在 `data/resources.yaml` 搜索 URL、标题、项目名和同一事件，避免重复收录。
- 厂商宣传、社区观点和研究结论必须注明属性，不写成无来源的客观事实。

详细标准见[内容规范](docs/content-guidelines.md)，完整来源策略见[来源地图](docs/sources.md)。

## 提交一条资源

在 `data/resources.yaml` 的 `resources` 列表中增加完整记录。以下示例可直接作为字段结构参考，但请替换为已核验的真实内容：

```yaml
  - id: example-agent-workflow
    title_zh: 示例智能体工作流实践
    title_original: Example Agent Workflow
    url: https://example.com/agent-workflow
    category: articles
    source: Example Engineering
    published_at: 2026-07-01
    added_at: 2026-07-13
    language: en
    summary_zh: 通过可复现案例说明如何拆分智能体任务、设置验证门槛、审查生成代码，并在交付前保留清晰的人工责任边界。
    tags: [agent, workflow, verification]
    featured: false
```

字段要求：

- `id` 一经收录应保持稳定，使用唯一的英文短横线标识。
- `title_zh` 和 `summary_zh` 必须包含中文；摘要按 `summary_zh.strip()` 的 Python Unicode code point 总数计为 40—120（含中英文、空格与标点），并以句号结尾。
- `title_original` 保留原始标题，中文原文可以与中文标题相同。
- `url` 使用去除跟踪参数后的原始 HTTPS 链接。
- `category` 可复用已有分类；新增分类时，请同时更新中文显示映射、相关测试和文档。
- `source` 填写原始页面明确显示的组织、平台或作者，不用搜索引擎、转载站或维护者作为来源。
- `published_at` 只填原文可核验的日期；未知时写 `published_at:`，不要猜测。
- `added_at` 是本次实际收录日期，不是原文日期。
- `language` 使用简短语言代码，如 `zh` 或 `en`。
- `tags` 使用简短、可复用的英文标签列表；先搜索现有拼写，避免为同一概念创建大小写或单复数变体。
- `featured: true` 只用于代表性强、对大多数读者有长期价值的精选资源。

如果你发现的是稳定产出优质内容的新来源，请在同一 PR 中补充 `docs/sources.md`；如果内容不适合现有分类，请说明新分类的边界，并同步修改生成器分类标签和测试。

## 本地生成与验证

需要 Python 3.11+。安装项目及开发依赖后，在仓库根目录运行：

```powershell
python -m pip install -e ".[dev]"
python -m scripts.validate
python -m scripts.build_readme
python -m scripts.build_readme --check
python -m pytest
python -m ruff check .
git diff --check
```

生成脚本只更新 README 的标记区。请把生成后的 `README.md` 与数据改动一起提交，并人工检查标题、摘要、分类、最近更新时间排序和链接目标。

## Pull Request 说明

PR 中请列出原始链接、核验日期、收录理由和实际运行的验证命令。若页面需要登录或只能找到二手来源，请不要提交该资源；二手来源只能用于发现，必须先定位可公开访问、可核验的原始 URL。日期无法确定时将 `published_at` 留空；互动数字可能变化时注明核验日期。一个 PR 可以收录多条相关资源，但不要混入无关格式化或代码改动。
