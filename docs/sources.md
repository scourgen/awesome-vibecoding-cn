# 来源地图与发现策略

本页记录可重复使用的种子来源、搜索式和访问限制，不是收录白名单。维护者必须继续通过主题搜索、引用追踪、相关推荐和新社区发现扩大搜索面；任何未列出的优质文章、项目、教程、产品或社区都应按统一质量门槛主动评估。一个新来源经过多次核验、持续产出高质量内容后，应补入本页，并注明适合检索的主题和限制。

搜索式中的日期范围应按维护日调整：常规更新优先最近 30 天，并额外回看最近 90 天的重要遗漏。

## 官方与作者来源

种子来源包括 OpenAI、Anthropic、Google、GitHub、Microsoft、AWS、Cloudflare、Vercel、Sourcegraph、JetBrains、Cursor、Replit、Lovable、国内模型与 AI Coding 厂商的官方文档、工程博客、更新日志、安全公告，以及独立作者的原始博客。

推荐搜索式：

```text
site:官方域名 (agent OR coding OR Codex OR "vibe coding") after:YYYY-MM-DD
site:官方域名 (release OR changelog OR security OR benchmark) after:YYYY-MM-DD
site:sourcegraph.com/blog ("coding agent" OR "agentic coding" OR "large codebase") after:YYYY-MM-DD
site:blog.jetbrains.com (Junie OR "coding agent" OR ACP OR benchmark) after:YYYY-MM-DD
"项目名" (announcement OR documentation OR migration OR deprecation)
```

限制：官方页面最适合核验产品状态，但其中的性能、效率、市场地位和安全宣称仍属于厂商表述。文档可能静默更新；记录可见发布日期或核验日期，必要时查公告或 Release 交叉确认。Sourcegraph 与 JetBrains 的文章可能同时包含工程经验、产品定位或自有基准结论，应分开转述并保留样本、评测周期与厂商归属。

## 代码托管与项目生态

种子来源包括 GitHub 仓库、Releases、Discussions、Topics、Trending，研究代码与数据集仓库，项目官方组织页，以及 Agent Skills 官方规范与参考实现。规范站和实现仓库可交叉核对格式演进、校验工具与客户端兼容性。

推荐搜索式：

```text
site:github.com ("agent skills" OR "coding agent" OR "vibe coding")
site:agentskills.io (specification OR "client implementation" OR validation)
site:github.com/topics (ai-coding OR coding-agent OR llm-agent)
site:github.com 项目名 (releases OR discussions OR security)
```

检索时查看 README、LICENSE、最近 Release、提交与 Issue/Discussion 状态，区分真正的上游仓库、镜像、Fork 和同名项目。

限制：Star 和 Trending 只能作为发现信号，不等于质量；若记录 Star、下载量或活跃度，必须注明核验日期。仓库创建时间不一定等于产品发布日期，未知发布日期应留空。规范页面可能原地更新且不标发布日期，应引用规范页本身并记录核验日期，不从仓库创建时间推测规范发布时间。

## 中文社区与中文内容

种子来源包括 Datawhale、LINUX DO、V2EX、牛客、掘金、知乎、少数派、国内厂商开发者社区与公开技术公众号文章。

推荐搜索式：

```text
site:linux.do (Vibe Coding OR Codex OR Claude Code OR 智能体开发)
site:v2ex.com (Vibe Coding OR AI 编程 OR 编程智能体)
site:datawhale.cn OR site:github.com/datawhalechina (AI 编程 OR 智能体)
site:juejin.cn OR site:zhihu.com (AI 编程 实践 OR 智能体 工作流)
```

限制：社区内容是经验与观点，不自动成为事实；优先信息完整的原帖和有实证细节的讨论。公众号转载一律不收录，必须定位到可公开访问、可核验的公众号原文或厂商原文；找不到原始 URL 就跳过。登录墙、删除帖、软文和其他不可公开访问页面同样不收录。不要依赖账号 Cookie，也不要绕过访问控制。

## 国际社区与独立作者

种子来源包括 Hacker News、Reddit 的相关技术社区、公开可访问的 X 原帖、开发者个人博客和项目社区讨论区。

推荐搜索式：

```text
site:news.ycombinator.com ("coding agent" OR "vibe coding")
site:reddit.com ("coding agent" OR "vibe coding" OR "agent workflow")
site:x.com 作者或项目名 (release OR benchmark OR workflow)
"文章或项目名" 作者 blog
```

限制：互动高不代表结论可靠。应打开原帖、核对发布时间与上下文，并追到所引用的项目、论文或公告。X 与 Reddit 可能要求登录或动态加载；无法稳定公开核验时，不依赖搜索摘要充当证据，优先寻找作者博客或项目页。

## 研究、基准与安全

种子来源包括 arXiv、论文作者或机构项目页、SWE-bench 等基准官网、研究机构博客、会议论文库，以及公开的代码与数据集。

推荐搜索式：

```text
site:arxiv.org ("coding agent" OR "software engineering agent" OR "vibe coding")
site:arxiv.org (benchmark OR security OR productivity) "coding agent"
"论文标题" (code OR dataset OR project)
"基准名称" (limitations OR contamination OR verified)
```

限制：优先使用论文原文的首次公开日期，并区分预印本版本、会议发表与项目公告日期。摘要需保留实验对象、样本和适用范围；作者博客可帮助理解，但不能替代论文证据。基准分数要核对版本、模型设置和发布日期。

## 搜索发现与引用追踪

搜索引擎、GitHub 推荐、论文参考文献、社区交叉链接、厂商 changelog 和项目 README 的生态列表用于发现未列来源。可组合中英文同义词，避免只搜索“Vibe Coding”：

```text
(AI 编程 OR 编程智能体 OR 规格驱动开发 OR Agent Skills) after:YYYY-MM-DD
(coding agent OR agentic coding OR harness engineering OR spec-driven development) after:YYYY-MM-DD
"已收录项目名" alternatives OR related OR ecosystem
"关键论断或数据" 原始报告或论文标题
```

限制：搜索排序和摘要会过时、截断或误标日期，不能作为最终引用。搜索发现的每个候选都要回到原始页面核验。不要只使用单一搜索引擎或固定关键词；每轮维护至少加入一个由引用、交叉推荐或新关键词发现的候选来源。

## 扩充本页的条件

新来源满足以下条件时加入相应章节：至少两次提供可公开访问、可核验、信息密度高且与本仓库直接相关的内容；来源身份和原始链接清晰；访问方式不依赖凭据或规避限制。补充时写清来源类型、推荐搜索式和已知限制，不只追加一个裸链接。

若新内容形态需要新分类，应同时更新数据分类键、README 中文显示映射、测试和相关指南。来源扩充与分类扩充都应在当次维护提交中完成，不能留给“以后再整理”。
