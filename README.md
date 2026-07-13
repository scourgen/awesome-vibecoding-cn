# awesome-vibecoding-cn

面向中文读者持续维护的 Vibe Coding 资源目录。正文条目由结构化数据确定性生成，收录范围会随生态发展持续扩充，初始分类和来源不是白名单。

## 参与与维护

欢迎通过 Issue 或 Pull Request 推荐尚未列出的优质文章、项目、教程、产品、社区和研究；如果现有分类无法准确容纳，也可以提出新分类。提交前请阅读[贡献指南](CONTRIBUTING.md)和[内容规范](docs/content-guidelines.md)。维护者与 Agent 可参照[来源地图](docs/sources.md)扩大检索范围，并按[维护手册](docs/maintenance.md)完成核验、生成、测试、审阅、提交与推送。

<!-- AWESOME-VIBE:START -->
**最后更新时间：2026-07-13**

收录原则：公开可核验的原始 URL、中文摘要、人工审核。

## 分类目录

- [Agent 技能](#agent-技能)
- [开源项目](#开源项目)
- [工具](#工具)
- [公司与产品](#公司与产品)
- [文章](#文章)
- [教程](#教程)
- [社区](#社区)
- [研究](#研究)

## 最近更新

- ⭐ **精选** [CLI 编程智能体失败轨迹的过程分析](https://arxiv.org/abs/2607.09510) — 研究分析 Terminal-Bench 上七个模型、三个脚手架的 3843 条轨迹，并人工标注六万余步骤，指出失败常由早期认知错误启动并延迟暴露。（Xiangxin Zhao 等 · 2026-07-10）
- ⭐ **精选** [SLBench 智能体技能逻辑关系遵循基准](https://arxiv.org/abs/2607.09016) — SLBench 扫描五千余个公开技能并构造 86 个可执行案例，测试 Codex 与 Claude Code 对前置条件、约束和回退关系的遵循及安全失效。（Jifan Zhang 等 · 2026-07-10）
- [软件工程 Agent Skills 市场实证研究](https://arxiv.org/abs/2607.09065) — 论文对公共仓库与市场中的软件工程 Skills 做大规模实证分析，考察生命周期覆盖、演化和评估机制，描绘技能复用生态而非评价单个工具。（Jialun Cao 等 · 2026-07-10）
- [SCATE 面向测试生成的自适应智能体监督](https://arxiv.org/abs/2607.08983) — SCATE 将测试生成监督建模为上下文赌博机，依据覆盖率和可测试性选择下一步动作；论文报告其在特定 Gemini CLI 实验中提升覆盖率。（Sijia Gu 等 · 2026-07-09）
- [GitHub Copilot 在 VS Code 的 2026 年 6 月更新](https://github.blog/changelog/2026-07-08-github-copilot-in-visual-studio-code-june-2026-releases/) — 官方汇总集成浏览器、并行会话、费用可见性、外部模型提供方和长上下文等更新，适合核对当前代理工作流能力。（GitHub Changelog · 2026-07-08）
- ⭐ **精选** [用多智能体工作流将 Bun 从 Zig 重写为 Rust](https://bun.com/blog/bun-in-rust) — Jarred Sumner 复盘用约 50 个动态工作流、对抗审查和完整测试迁移 53 万行 Zig；工期、并发规模与成本均为作者报告。（Bun · 2026-07-08）
- [JetBrains Copilot 预览 Codex 提供方与智能体增强](https://github.blog/changelog/2026-07-07-codex-as-agent-provider-and-agentic-enhancements-in-jetbrains-ides/) — GitHub 宣布在 JetBrains Copilot 中预览 Codex 智能体提供方，并扩展 Hooks、MCP 管理和审批设置，呈现 IDE 内多智能体工作流的整合方向。（GitHub Changelog · 2026-07-07）
- [JetBrains 团队级 AI 编程治理实践](https://blog.jetbrains.com/blog/2026/07/07/jetbrains-ai-for-teams-and-organizations-from-fragmented-ai-usage-to-coordinated-software-development/) — 官方介绍团队如何统一管理模型、智能体、访问权限、使用分析和成本；其中效果与治理价值属于厂商观点。（JetBrains · 2026-07-07）
- [Claude Fable 协助 sqlite-utils 发布前审查实践](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/) — Simon Willison 公开提示词、修复记录和会话成本，展示智能体如何在发布前发现事务缺陷，并由人工复核实验与改动。（Simon Willison · 2026-07-05）
- [更强模型为何可能更不适配第三方工具](https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/) — Armin Ronacher 记录新 Claude 模型在 Pi 嵌套编辑工具中虚构字段的案例，并推测模型后训练可能偏向特定 Harness；结论属于作者观察。（Armin Ronacher · 2026-07-04）

## Agent 技能

- ⭐ **精选** [Superpowers 智能体开发方法论](https://github.com/obra/superpowers) — 将头脑风暴、测试驱动开发、系统调试、评审和验证组织成可组合的强约束技能，便于读者核对其组成、用途与适用边界。（Jesse Vincent · 2025-10-09）
- ⭐ **精选** [Anthropic Agent Skills 官方仓库](https://github.com/anthropics/skills) — 官方示例展示如何用 SKILL.md、脚本和参考资料封装可复用的智能体能力，便于读者核对其组成、用途与适用边界。（Anthropic · 2025-09-22）
- ⭐ **精选** [Spec Kit 规格驱动开发工具包](https://github.com/github/spec-kit) — 通过原则、规格、计划和任务阶段把模糊想法转成可验证的软件交付流程，便于读者核对其组成、用途与适用边界。（GitHub · 2025-08-21）
- ⭐ **精选** [GitHub Awesome Copilot 配置合集](https://github.com/github/awesome-copilot) — GitHub 官方维护的指令、提示文件、定制智能体和技能示例导航，便于读者核对其组成、用途与适用边界。（GitHub · 2025-06-11）
- ⭐ **精选** [Agent Skills 开放规范与参考实现](https://github.com/agentskills/agentskills) — 开放规范定义 SKILL.md 的目录结构、元数据与渐进式加载方式，并提供校验工具和跨智能体实现参考。（Agent Skills）
- [Claude Code 专业子智能体合集](https://github.com/VoltAgent/awesome-claude-code-subagents) — 提供覆盖开发、测试、安全、运维和产品等岗位的可委派子智能体模板，便于读者核对其组成、用途与适用边界。（VoltAgent · 2025-07-30）
- [Claude Code Templates 配置工具箱](https://github.com/davila7/claude-code-templates) — 汇集 agents、commands、hooks、MCP 和 settings 模板，并提供配套管理工具。（davila7 · 2025-07-04）
- [Awesome Claude Code 资源精选](https://github.com/hesreallyhim/awesome-claude-code) — 精选 Claude Code 的 Skills、Agents、Hooks、插件和开发辅助工具。（hesreallyhim · 2025-04-19）
- [BMAD 多角色敏捷开发方法](https://github.com/bmad-code-org/BMAD-METHOD) — 以分析师、产品经理、架构师和开发者等角色推动结构化的智能体开发生命周期，便于读者核对其组成、用途与适用边界。（BMAD Code · 2025-04-13）
- [Awesome Cursor Rules 规则集合](https://github.com/PatrickJS/awesome-cursorrules) — 按语言和框架整理 Cursor 项目规则，可用于理解旧版规则生态并迁移到新版目录格式。（PatrickJS · 2024-09-16）
- [GitHub Copilot 自定义能力速查表](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) — 对比项目指令、提示文件、智能体、技能、钩子和 MCP 的位置与支持范围，便于读者核对其组成、用途与适用边界。（GitHub Docs）
- [Vercel 跨客户端 Skills 管理工具](https://github.com/vercel-labs/skills) — 提供统一的 npx skills 命令，可为 Codex、OpenCode、Claude Code、Cursor 等客户端查找、安装和更新技能。（Vercel Labs）

## 开源项目

- ⭐ **精选** [OpenCode 开源终端编程智能体](https://github.com/anomalyco/opencode) — 提供终端优先的多模型编程智能体、完整交互界面和可扩展提供商支持，便于读者核对其能力范围、使用方式与维护入口。（Anomaly · 2025-04-30）
- ⭐ **精选** [Gemini CLI 开源企业与 API 终端智能体](https://github.com/google-gemini/gemini-cli) — 该 Apache-2.0 项目继续服务企业和 API 用户，个人免费及 Pro、Ultra 终端入口已迁移到 Antigravity CLI。（Google · 2025-04-17）
- ⭐ **精选** [Codex CLI 开源编程智能体](https://github.com/openai/codex) — OpenAI 的本地终端智能体可读写代码、运行命令并与云端、桌面端和 IDE 协作。（OpenAI · 2025-04-13）
- ⭐ **精选** [Model Context Protocol 参考服务器](https://github.com/modelcontextprotocol/servers) — 汇集官方参考服务器并导航社区实现，展示统一协议连接文件、Git 和外部服务的方式。（Model Context Protocol · 2024-11-19）
- ⭐ **精选** [OpenHands 开源软件开发平台](https://github.com/OpenHands/OpenHands) — 让智能体通过代码编辑、终端和浏览器完成软件工程任务，并支持本地或平台部署，便于读者核对其能力范围、使用方式与维护入口。（OpenHands · 2024-03-13）
- [Context7 最新文档上下文服务](https://github.com/upstash/context7) — 通过 MCP 注入特定版本的官方库文档，减少过期接口和虚构用法，便于读者核对其能力范围、使用方式与维护入口。（Upstash · 2025-03-26）
- [Serena 智能体语义编程工具](https://github.com/oraios/serena) — 借助语言服务器为编程智能体提供符号级导航、语义检索和精确编辑，便于读者核对其能力范围、使用方式与维护入口。（Oraios · 2025-03-23）
- [Roo Code 多模式编辑器智能体](https://github.com/RooCodeInc/Roo-Code) — 从 Cline 生态发展出的 VS Code 智能体，强调角色模式、任务编排和团队配置。（Roo Code · 2024-10-31）
- [Goose 模型无关开发智能体](https://github.com/aaif-goose/goose) — 现由 AAIF 维护的可扩展开源智能体，可安装依赖、编辑、执行和测试代码，便于读者核对其能力范围、使用方式与维护入口。（AAIF · 2024-08-23）
- [Repomix 仓库上下文打包工具](https://github.com/yamadashy/repomix) — 将代码库整理为适合模型输入的单文件，并提供过滤、令牌统计和安全检查，便于读者核对其能力范围、使用方式与维护入口。（yamadashy · 2024-07-13）
- [Cline 编辑器编程智能体](https://github.com/cline/cline) — 在编辑器内提供可审批的读取、修改、命令执行和验证流程，并支持多模型，便于读者核对其能力范围、使用方式与维护入口。（Cline · 2024-07-06）
- [SWE-agent 自动修复 GitHub Issue](https://github.com/SWE-agent/SWE-agent) — 将真实 Issue、终端环境和模型连接起来，自动定位、修改并测试软件修复，便于读者核对其能力范围、使用方式与维护入口。（Princeton NLP · 2024-04-02）
- [AutoGen 多智能体应用框架](https://github.com/microsoft/autogen) — 提供智能体、工具、消息和多智能体协作抽象，可用于搭建软件工程代理系统，便于读者核对其能力范围、使用方式与维护入口。（Microsoft · 2023-08-18）
- [Continue 开源 IDE 编程平台](https://github.com/continuedev/continue) — 支持自定义模型、上下文提供器、规则和智能体工作流，适合自托管与企业定制，便于读者核对其能力范围、使用方式与维护入口。（Continue · 2023-05-24）
- [Aider 终端 AI 结对编程工具](https://github.com/Aider-AI/aider) — 以 Git、代码地图和终端对话为核心，提供成熟的多模型结对编程工作流，便于读者核对其能力范围、使用方式与维护入口。（Aider · 2023-05-09）
- [AhaDiff 基于代码差异的复盘学习工具](https://github.com/AGI-is-going-to-arrive/ahadiff) — 本地优先地分析 AI 生成的 Git 差异，将具体改动转成带证据的讲解、测验和复习材料，帮助开发者理解已合入代码。（AhaDiff）
- [Simon Willison 的模型无关编程智能体](https://github.com/simonw/llm-coding-agent) — 该项目基于 LLM 插件系统构建模型无关的编程智能体，提供受根目录限制的读写、搜索、命令执行、审批和会话恢复能力。（Simon Willison）

## 工具

- ⭐ **精选** [Claude Code 开源仓库](https://github.com/anthropics/claude-code) — Anthropic 的终端编程代理仓库，包含安装说明、使用入口与问题反馈渠道，便于读者核对其功能范围、配置方式与适用场景。（Anthropic）
- [文心快码 Comate 产品能力](https://cloud.baidu.com/doc/COMATE/s/xlnvqe047) — 覆盖多智能体、自定义 Agent、Rules、MCP、补全、知识增强和独立 AI IDE。（百度智能云 · 2026-04-01）
- [腾讯 CodeBuddy 产品形态总览](https://cloud.tencent.com/document/product/1749/104236) — 对比插件、独立 IDE 与 CLI 三种形态，并说明 Craft、子智能体和自动化工作流。（腾讯云 · 2025-10-11）
- [Cursor Rules 项目规范指南](https://docs.cursor.com/context/rules) — 介绍项目规则、用户规则、记忆、触发类型和嵌套目录的当前官方机制，便于读者核对其功能范围、配置方式与适用场景。（Cursor）
- [DeepSeek 接入 Claude Code](https://api-docs.deepseek.com/guides/agent_integrations/claude_code) — 使用官方 Anthropic 兼容端点将 DeepSeek 模型配置到 Claude Code。（DeepSeek）
- [GLM Coding Plan 接入指南](https://docs.bigmodel.cn/cn/coding-plan/quick-start) — 介绍如何把 GLM 编程模型接入 Claude Code、Cursor、OpenCode 和 Cline 等工具。（智谱 AI）
- [Gemini CLI 工具与安全审批机制](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md) — 解释文件、Shell、Web 和 MCP 工具，以及确认、沙箱和可信目录等执行边界。（Google）
- [TRAE AI 原生 IDE](https://www.trae.ai/ide) — 字节系 AI 原生开发环境入口，面向个人开发者提供智能体式编码体验，便于读者核对其功能范围、配置方式与适用场景。（TRAE）
- [Windsurf Cascade 技能指南](https://docs.windsurf.com/windsurf/cascade/skills) — 使用 SKILL.md、脚本、模板和参考资料封装复杂流程，并按需渐进加载内容，便于读者核对其功能范围、配置方式与适用场景。（Windsurf）
- [Windsurf 记忆、Rules 与 AGENTS.md](https://docs.windsurf.com/zh/windsurf/cascade/memories) — 官方中文文档比较 Rules、AGENTS.md、Workflows、Skills 和自动记忆的持久化方式。（Windsurf）
- [通义灵码项目规则指南](https://help.aliyun.com/zh/lingma/qoder-cn/user-guide/rules) — 说明项目规则目录及手动、模型判断、始终启用和文件匹配四类触发方式，便于读者核对其功能范围、配置方式与适用场景。（阿里云）

## 公司与产品

- ⭐ **精选** [Gemini CLI 迁移至 Antigravity CLI 公告](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) — 公告确认 2026 年 6 月 18 日起个人免费及 Pro、Ultra 终端体验迁至 Antigravity CLI，企业与 API 使用继续保留。（Google Developers Blog · 2026-05-19）
- ⭐ **精选** [OpenAI Codex 官方开发者入口](https://developers.openai.com/) — 聚合 Codex 产品、开发文档、案例和智能体编程资源的官方入口，便于读者从官方资料核对功能范围与使用入口。（OpenAI）
- [Qoder AI 编程产品套件概览](https://help.aliyun.com/en/lingma/product-overview/introduction-of-lingma) — 官方说明通义灵码更名后的 IDE、CLI、云端任务、专家子智能体与 Quest 工作流，相关能力属于厂商产品介绍。（Alibaba Cloud · 2026-01-16）
- [Claude Code 正式可用与 Claude 4](https://www.anthropic.com/news/claude-4) — 记录 Claude Code 正式可用，并介绍后台任务、IDE 集成和代理式开发能力。（Anthropic · 2025-05-22）
- [Amazon Q Developer 官方文档中心](https://aws.amazon.com/documentation-overview/q-developer/) — 覆盖 IDE 对话、代码解释、修复、测试以及从自然语言生成完整功能的官方资料，便于读者从官方资料核对功能范围与使用入口。（AWS）
- [Cloudflare Workers AI 平台](https://developers.cloudflare.com/workers-ai/) — 在 Cloudflare GPU 网络运行开放模型，并可结合 AI Gateway 与 Vectorize 构建应用。（Cloudflare）
- [GitHub Copilot 云端智能体](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) — 介绍异步处理 Issue、在独立环境编码并创建草稿拉取请求的云端智能体，便于读者从官方资料核对功能范围与使用入口。（GitHub Docs）
- [Lovable 自然语言全栈开发平台](https://docs.lovable.dev/introduction/welcome) — 生成前端、后端、数据库、认证和集成，并支持 GitHub 同步与部署，便于读者从官方资料核对功能范围与使用入口。（Lovable）
- [Replit Agent 云端应用开发](https://docs.replit.com/learn/build-with-agent) — 在云端从想法生成、运行、调试并发布应用，覆盖从编码到托管的一体化路线，便于读者从官方资料核对功能范围与使用入口。（Replit）
- [Vercel AI SDK 开发工具包](https://vercel.com/ai-sdk) — 面向 TypeScript 提供多模型调用、流式响应、工具调用和智能体开发能力。（Vercel）
- [Vercel v0 全栈应用生成器](https://vercel.com/docs/v0) — 从自然语言生成界面、落地页和全栈应用，并可直接衔接 Vercel 部署，便于读者从官方资料核对功能范围与使用入口。（Vercel）

## 文章

- ⭐ **精选** [用多智能体工作流将 Bun 从 Zig 重写为 Rust](https://bun.com/blog/bun-in-rust) — Jarred Sumner 复盘用约 50 个动态工作流、对抗审查和完整测试迁移 53 万行 Zig；工期、并发规模与成本均为作者报告。（Bun · 2026-07-08）
- ⭐ **精选** [Anthropic 跨产品智能体隔离与安全边界](https://www.anthropic.com/engineering/how-we-contain-claude) — 官方复盘 claude.ai、Claude Code 与 Cowork 的容器、沙箱和虚拟机隔离方案，并披露审批疲劳、配置预加载与出口控制等失效案例。（Anthropic Engineering · 2026-05-25）
- ⭐ **精选** [长时间应用开发的三智能体 Harness 设计](https://www.anthropic.com/engineering/harness-design-long-running-apps) — Anthropic 工程师以规划、生成和评估三类智能体拆分长任务，通过结构化交接与独立验收缓解上下文衰减和自我评价偏宽的问题。（Anthropic Engineering · 2026-03-24）
- ⭐ **精选** [Harness Engineering 智能体优先代码库实践](https://openai.com/index/harness-engineering/) — 总结仓库可读性、约束、反馈回路、文档结构和持续熵管理等智能体工程经验，可用于了解相关方法、背景与工程适用边界。（OpenAI · 2026-02-11）
- ⭐ **精选** [Claude Code 智能体编程最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices) — 系统讲解项目指令、探索与计划、测试驱动开发、上下文管理和独立审查，可用于了解相关方法、背景与工程适用边界。（Anthropic Engineering · 2025-04-18）
- ⭐ **精选** [别把所有 AI 辅助编程都叫 Vibe Coding](https://simonwillison.net/2025/Mar/19/vibe-coding/) — 区分忽略代码细节的原始 Vibe Coding 与工程师审阅、理解并负责的 AI 辅助开发。（Simon Willison · 2025-03-19）
- [GitHub Copilot 在 VS Code 的 2026 年 6 月更新](https://github.blog/changelog/2026-07-08-github-copilot-in-visual-studio-code-june-2026-releases/) — 官方汇总集成浏览器、并行会话、费用可见性、外部模型提供方和长上下文等更新，适合核对当前代理工作流能力。（GitHub Changelog · 2026-07-08）
- [JetBrains Copilot 预览 Codex 提供方与智能体增强](https://github.blog/changelog/2026-07-07-codex-as-agent-provider-and-agentic-enhancements-in-jetbrains-ides/) — GitHub 宣布在 JetBrains Copilot 中预览 Codex 智能体提供方，并扩展 Hooks、MCP 管理和审批设置，呈现 IDE 内多智能体工作流的整合方向。（GitHub Changelog · 2026-07-07）
- [JetBrains 团队级 AI 编程治理实践](https://blog.jetbrains.com/blog/2026/07/07/jetbrains-ai-for-teams-and-organizations-from-fragmented-ai-usage-to-coordinated-software-development/) — 官方介绍团队如何统一管理模型、智能体、访问权限、使用分析和成本；其中效果与治理价值属于厂商观点。（JetBrains · 2026-07-07）
- [Claude Fable 协助 sqlite-utils 发布前审查实践](https://simonwillison.net/2026/Jul/5/sqlite-utils-fable/) — Simon Willison 公开提示词、修复记录和会话成本，展示智能体如何在发布前发现事务缺陷，并由人工复核实验与改动。（Simon Willison · 2026-07-05）
- [更强模型为何可能更不适配第三方工具](https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/) — Armin Ronacher 记录新 Claude 模型在 Pi 嵌套编辑工具中虚构字段的案例，并推测模型后训练可能偏向特定 Harness；结论属于作者观察。（Armin Ronacher · 2026-07-04）
- [百度文心快码 2026 年智能体能力更新日志](https://cloud.baidu.com/doc/COMATE/s/2mjzerjsp) — 1.9.0 版加入异步子智能体、记忆、自动化、插件创建和 Skills 选择器，页面可用于持续追踪后续版本变化。（百度智能云 · 2026-06-01）
- [Gemini Code Assist 负责任 AI 指南](https://developers.google.com/gemini-code-assist/docs/responsible-ai) — 说明幻觉、偏差、安全过滤和有限领域能力，并强调生成代码必须经过人工审核，可用于了解相关方法、背景与工程适用边界。（Google · 2026-05-27）
- [Sourcegraph 的大型代码库 Agentic Coding 指南](https://sourcegraph.com/blog/agentic-coding) — 文章从大型组织和复杂代码库出发，讨论上下文获取、工具接入与审查边界，补充个人项目之外的工程实践视角。（Matt Tanner · 2026-05-21）
- [Symphony 项目看板智能体编排规范](https://openai.com/index/open-source-codex-orchestration-symphony/) — 将项目管理看板变成编程智能体控制面，用工作队列缓解多任务上下文切换，可用于了解相关方法、背景与工程适用边界。（OpenAI · 2026-04-27）
- [Claude Code 质量下降事件复盘](https://www.anthropic.com/engineering/april-23-postmortem) — 官方将近期质量问题追溯到默认推理强度、闲置会话思考清理和系统提示三项变更，并说明修复时间与后续发布流程调整。（Anthropic Engineering · 2026-04-23）
- [Claude Code 自动模式的两阶段安全审核](https://www.anthropic.com/engineering/claude-code-auto-mode) — 官方说明 Claude Code 自动模式如何用两阶段分类器审核高风险工具调用，并公开误拦截与漏检数据，强调它不能替代高风险场景的人类复核。（Anthropic Engineering · 2026-03-25）
- [Cursor 如何用自主 Agent 守护代码库](https://cursor.com/blog/security-agents) — 展示持续安全审查、漏洞发现、依赖更新和不变量检查等可复用智能体模板，可用于了解相关方法、背景与工程适用边界。（Cursor · 2026-03-16）
- [AI 编码实践：从 Vibe Coding 到 SDD](https://zhuanlan.zhihu.com/p/2001605764670833810) — 淘特导购团队复盘从补全、智能体与规则演进到轻量规格驱动开发的工程方案，可用于了解相关方法、背景与工程适用边界。（阿里云开发者）
- [Lovable 应用安全总览](https://docs.lovable.dev/features/security) — 覆盖密钥防泄漏、行级安全、数据库、代码和依赖扫描以及发布前检查，可用于了解相关方法、背景与工程适用边界。（Lovable）
- [Replit 共享责任模型](https://docs.replit.com/references/security/shared-responsibility-model) — 划分平台、智能体、开发环境、已发布应用和用户各自承担的安全责任，可用于了解相关方法、背景与工程适用边界。（Replit）
- [为什么 SWE-bench Verified 已难衡量前沿能力](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) — 分析测试缺陷和数据污染如何削弱榜单区分度，提醒读者谨慎解读单一基准，可用于了解相关方法、背景与工程适用边界。（OpenAI）

## 教程

- ⭐ **精选** [Easy-Vibe 会说话就会做应用](https://github.com/datawhalechina/easy-vibe) — 面向零基础到进阶开发者的开源课程，覆盖全栈、RAG、MCP、SaaS 和小程序开发。（Datawhale）
- [文心快码 Zulu Agent 入门](https://cloud.baidu.com/doc/COMATE/s/vm66asjm4) — 演示从需求到代码、多智能体拆解、命令执行、验证和迭代的完整流程，便于按步骤理解流程、验证方法与适用场景。（百度智能云 · 2026-02-28）
- [Bolt 十分钟应用快速开始](https://support.bolt.new/building/quickstart) — 通过完整示例演示从提示、数据库和登录到预览及发布的浏览器开发流程，便于按步骤理解流程、验证方法与适用场景。（Bolt）
- [Claude Code 安装与快速开始](https://docs.anthropic.com/en/docs/claude-code/getting-started) — 官方说明安装、登录、系统要求、更新方式和首次运行终端任务的步骤，便于按步骤理解流程、验证方法与适用场景。（Anthropic）
- [Codex 官方实战案例库](https://developers.openai.com/codex/use-cases) — 展示代码迁移、安全扫描、拉取请求审查、前端构建、测试和自动化等任务模式，便于按步骤理解流程、验证方法与适用场景。（OpenAI）
- [Gemini CLI 企业与 API 用户快速开始](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/index.md) — 介绍安装、认证、配置和首个任务，个人免费及 Pro、Ultra 用户应改用 Antigravity CLI。（Google）
- [GitHub Copilot 自定义案例库](https://docs.github.com/en/copilot/tutorials/customization-library) — 官方整理可直接复用的项目指令、提示文件和定制智能体实例，便于按步骤理解流程、验证方法与适用场景。（GitHub Docs）
- [Lovable 产品开发提示最佳实践](https://docs.lovable.dev/prompting/prompting-one) — 从需求澄清、用户旅程和组件化构建讲到版本控制与逐步迭代，便于按步骤理解流程、验证方法与适用场景。（Lovable）
- [Replit Vibe Coding 安全清单](https://docs.replit.com/learn/security-checklist) — 从前端、后端、HTTPS、认证和输入验证到持续维护逐项检查生成式应用，便于按步骤理解流程、验证方法与适用场景。（Replit）
- [通义灵码多文件修改与单元测试](https://help.aliyun.com/zh/lingma/user-guide/edit/) — 官方讲解需求拆分、上下文选择、快照回退以及测试的生成、运行与修复，便于按步骤理解流程、验证方法与适用场景。（阿里云）

## 社区

- ⭐ **精选** [Vibe Coding 生产项目实践讨论](https://linux.do/t/topic/2360067) — 针对老项目失控问题讨论 SDD、TDD、灰度、备份、多模型互审和人工评审，可用于观察实践经验、分歧与具体使用边界。（LINUX DO · eof_karel · 2026-06-10）
- ⭐ **精选** [培训 Codex 后工作反而更多了](https://linux.do/t/topic/2268339) — 记录内部工具培训后工期被压缩、任务增加的经历，呈现效率收益分配的组织争议，可用于观察实践经验、分歧与具体使用边界。（LINUX DO · fairyw · 2026-05-29）
- ⭐ **精选** [大量生成代码后的线上质量责任](https://www.v2ex.com/t/1208265) — 讨论人工编写测试、拉取请求钩子和独立复核，警惕同一智能体为过测试采用脏实现，可用于观察实践经验、分歧与具体使用边界。（V2EX · kyrieIvring · 2026-04-24）
- [V2EX：两年 Vibe Coding 经历与使用方式反思](https://v2ex.com/t/1221657) — 作者结合个人和身边开发者经历，区分完全委托、协同增强与轻量使用，呈现不同能力基础下的收益和风险判断。（SoraStar · 2026-06-20）
- [AI 编程普及率的信息茧房](https://www.v2ex.com/t/1221461) — 通过自由职业者和回复者的个人经历提醒读者，技术社区热度不等于全行业普及率，可用于观察实践经验、分歧与具体使用边界。（V2EX · NotAfraidLP · 2026-06-19）
- [Reddit：用确定性脚本替代不必要的模型调用](https://www.reddit.com/r/vibecoding/comments/1u2z798/after_10_years_as_an_engineer_the_thing_id_teach/) — 帖子主张将可重复的解析、校验和转换固化为确定性工具，减少智能体反复消耗上下文和模型调用的成本。（r/vibecoding · 2026-06-11）
- [V2EX：半年 Vibe Coding 的效率与疲劳体验](https://www.v2ex.com/t/1219408) — 作者记录交付速度提升之外的审查疲劳、成就感下降和规格维护成本，评论区也补充了不同开发者的应对方式。（coderYang · 2026-06-10）
- [一个未能实现的 Vibe Coding Harness](https://linux.do/t/topic/2306363) — 尝试用意图分析、提示质量记录和上下文注入降低门槛，并坦诚保留无法实现的结论，可用于观察实践经验、分歧与具体使用边界。（LINUX DO · Soei · 2026-06-04）
- [Vibe Coding 进入工作后如何长效维护](https://linux.do/t/topic/2279770) — 围绕真实线下工具投入生产后的维护成本，讨论从生成成品转向固定协作流程，可用于观察实践经验、分歧与具体使用边界。（LINUX DO · skyrock · 2026-05-31）
- [中文社区 AI 编程工具实用对比](https://www.v2ex.com/t/1210849) — 用户按当时价格与体验比较 Claude Code、Codex、Cursor、TRAE、通义灵码和 Qoder。（V2EX · fireeeeee · 2026-05-07）
- [Vibe Coding 从入门到 Harness Engineering](https://linux.do/t/topic/2085611) — 以开源项目自荐形式串联 Prompt、上下文、MCP、Skills、规格驱动开发和 Harness Engineering。（LINUX DO · joytion · 2026-04-30）
- [中文开发者都在 Vibe Coding 什么项目](https://linux.do/t/topic/2051569) — 汇集装箱工具、启动页、自动打卡、桌面启动器、小说界面和浏览器插件等真实选题，可用于观察实践经验、分歧与具体使用边界。（LINUX DO · duiguangbin · 2026-04-25）
- [Vibe Coding 的意义与工程边界](https://v2ex.com/t/1208240) — 高互动讨论主张架构、接口和责任边界由人掌握，AI 负责小步局部实现，可用于观察实践经验、分歧与具体使用边界。（V2EX · chuchen023 · 2026-04-24）
- [Vibe Coding 一周体验与工程流程](https://www.v2ex.com/t/1203913) — 详细记录原型、业务与权限文档、前后端智能体、人工验证、评审和提交的流程，可用于观察实践经验、分歧与具体使用边界。（V2EX · a526796017 · 2026-04-07）
- [V2EX：Vibe Coding 迁移旧项目时遗漏隐性逻辑](https://www.v2ex.com/t/1217323) — 讨论提出旧系统的隐藏配置、第三方逻辑和架构约束容易在重构时丢失，适合作为规格梳理与回归验证的反例。（UnYu）

## 研究

- ⭐ **精选** [CLI 编程智能体失败轨迹的过程分析](https://arxiv.org/abs/2607.09510) — 研究分析 Terminal-Bench 上七个模型、三个脚手架的 3843 条轨迹，并人工标注六万余步骤，指出失败常由早期认知错误启动并延迟暴露。（Xiangxin Zhao 等 · 2026-07-10）
- ⭐ **精选** [SLBench 智能体技能逻辑关系遵循基准](https://arxiv.org/abs/2607.09016) — SLBench 扫描五千余个公开技能并构造 86 个可执行案例，测试 Codex 与 Claude Code 对前置条件、约束和回退关系的遵循及安全失效。（Jifan Zhang 等 · 2026-07-10）
- ⭐ **精选** [微软命令行 AI 编程智能体采用与影响研究](https://arxiv.org/abs/2607.01418) — 研究分析微软内部数万名开发者的早期推广数据，采用者合并 PR 数提高约 24%，但作者明确指出该指标不等同于实际价值。（Emerson Murphy-Hill 等 · 2026-07-01）
- ⭐ **精选** [AI 编程工具生产力与学习效果元分析](https://arxiv.org/abs/2605.04779) — 元分析汇总 23 项研究和 27 个效应量，发现生产力有中等正向效应且异质性明显，学习效果则未达到统计显著。（Sebastian Maier 等 · 2026-05-06）
- ⭐ **精选** [SlopCodeBench 长期代码退化基准](https://arxiv.org/abs/2603.24755) — 让智能体连续响应变化需求，衡量代码冗余和结构侵蚀如何随多轮迭代增长，便于核对任务设计、评估方法与结论适用范围。（Gabriel Orlanski 等 · 2026-03-25）
- ⭐ **精选** [Terminal-Bench 真实终端任务基准](https://arxiv.org/abs/2601.11868) — 以独立环境、人工解法和测试评估智能体完成复杂长时终端工作流的能力，便于核对任务设计、评估方法与结论适用范围。（Mike A. Merrill 等 · 2026-01-17）
- ⭐ **精选** [SecureAgentBench 安全编码基准](https://arxiv.org/abs/2509.22097) — 用真实漏洞场景的多文件任务同时检查功能、已知漏洞和新引入的安全问题，便于核对任务设计、评估方法与结论适用范围。（Junkai Chen 等 · 2025-09-26）
- ⭐ **精选** [早期 2025 AI 工具对资深开发者生产力的影响](https://arxiv.org/abs/2507.09089) — 随机对照实验发现特定早期工具让成熟仓库的资深维护者平均变慢，结论不应泛化到所有场景。（Joel Becker 等 · 2025-07-12）
- ⭐ **精选** [SWE-bench 真实软件工程基准](https://www.swebench.com/original.html) — 要求模型依据真实 GitHub Issue 修改完整仓库并通过测试，奠定现代编程智能体评价方式。（Carlos E. Jimenez 等）
- [软件工程 Agent Skills 市场实证研究](https://arxiv.org/abs/2607.09065) — 论文对公共仓库与市场中的软件工程 Skills 做大规模实证分析，考察生命周期覆盖、演化和评估机制，描绘技能复用生态而非评价单个工具。（Jialun Cao 等 · 2026-07-10）
- [SCATE 面向测试生成的自适应智能体监督](https://arxiv.org/abs/2607.08983) — SCATE 将测试生成监督建模为上下文赌博机，依据覆盖率和可测试性选择下一步动作；论文报告其在特定 Gemini CLI 实验中提升覆盖率。（Sijia Gu 等 · 2026-07-09）
- [立场论文：现有编程基准与实际开发目标错位](https://arxiv.org/abs/2606.17799) — 作者认为现有评测混合模型、工具链和环境效果，并依赖单一参考解法，建议增加组件级信号与真实工作流评估。（Maria I. Gorinova 等 · 2026-06-16）
- [Agentic Agile-V 可审计智能体开发框架](https://arxiv.org/abs/2605.20456) — 论文提出 SCOPE-V 生命周期，将规格、约束、编排、证据、演进和验证串联，并在关键节点保留人工审批。（Christopher Koch · 2026-05-19）
- [Mise en Place 智能体上下文工程方法](https://arxiv.org/abs/2605.05400) — 框架将开发前准备拆为上下文奠基、协作式规格和任务分解三阶段，强调在调用智能体之前先构造可验证的工作环境。（Andrew Zigler · 2026-05-06）
- [SWE-rebench V2 多语言任务流水线](https://arxiv.org/abs/2602.23866) — 将任务收集扩展到二十种语言和数千个仓库，更贴近真实多语言软件生态，便于核对任务设计、评估方法与结论适用范围。（Ibragim Badertdinov 等 · 2026-02-27）
- [JAWS-BENCH 编程智能体越狱评估](https://arxiv.org/abs/2510.01359) — 比较不同工作区上下文中的可执行恶意代码攻击，评估智能体包装对越狱风险的放大，便于核对任务设计、评估方法与结论适用范围。（Shoumik Saha 等 · 2025-10-01）
- [SWE-rebench 持续更新软件工程基准](https://arxiv.org/abs/2505.20411) — 自动从新 GitHub 拉取请求抽取可执行任务，以新鲜数据降低固定榜单污染，便于核对任务设计、评估方法与结论适用范围。（Ibragim Badertdinov 等 · 2025-05-26）
- [SWE-smith 软件工程训练数据](https://arxiv.org/abs/2504.21798) — 从一百二十八个仓库合成约五万个可执行任务，并训练开源软件工程智能体模型，便于核对任务设计、评估方法与结论适用范围。（John Yang 等 · 2025-04-30）
- [SWE-Lancer 真实外包任务基准](https://arxiv.org/abs/2502.12115) — 用一千四百多个真实软件工程和管理任务评估模型能否完成有经济价值的外包工作，便于核对任务设计、评估方法与结论适用范围。（Samuel Miserendino 等 · 2025-02-17）
- [SWE-bench Verified 人工核验基准](https://openai.com/index/introducing-swe-bench-verified/) — 人工核验五百个软件修复任务以降低测试缺陷和描述歧义，阅读时应结合其后续退役说明。（OpenAI 与 SWE-bench · 2024-08-13）
<!-- AWESOME-VIBE:END -->
