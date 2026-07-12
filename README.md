# awesome-vibecoding-cn

面向中文读者持续维护的 Vibe Coding 资源目录。正文条目由结构化数据确定性生成，收录范围会随生态发展持续扩充，初始分类和来源不是白名单。

## 参与与维护

欢迎通过 Issue 或 Pull Request 推荐尚未列出的优质文章、项目、教程、产品、社区和研究；如果现有分类无法准确容纳，也可以提出新分类。提交前请阅读[贡献指南](CONTRIBUTING.md)和[内容规范](docs/content-guidelines.md)。维护者与 Agent 可参照[来源地图](docs/sources.md)扩大检索范围，并按[维护手册](docs/maintenance.md)完成核验、生成、测试、审阅、提交与推送。

<!-- AWESOME-VIBE:START -->
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

- [AI 编程普及率的信息茧房](https://www.v2ex.com/t/1221461) — 通过自由职业者和回复者的个人经历提醒读者，技术社区热度不等于全行业普及率。（V2EX · NotAfraidLP · 2026-06-19）
- ⭐ **精选** [Vibe Coding 生产项目实践讨论](https://linux.do/t/topic/2360067) — 针对老项目失控问题讨论 SDD、TDD、灰度、备份、多模型互审和人工评审。（LINUX DO · eof_karel · 2026-06-10）
- [一个未能实现的 Vibe Coding Harness](https://linux.do/t/topic/2306363) — 尝试用意图分析、提示质量记录和上下文注入降低门槛，并坦诚保留无法实现的结论。（LINUX DO · Soei · 2026-06-04）
- [Vibe Coding 进入工作后如何长效维护](https://linux.do/t/topic/2279770) — 围绕真实线下工具投入生产后的维护成本，讨论从生成成品转向固定协作流程。（LINUX DO · skyrock · 2026-05-31）
- ⭐ **精选** [培训 Codex 后工作反而更多了](https://linux.do/t/topic/2268339) — 记录内部工具培训后工期被压缩、任务增加的经历，呈现效率收益分配的组织争议。（LINUX DO · fairyw · 2026-05-29）
- [Gemini Code Assist 负责任 AI 指南](https://developers.google.com/gemini-code-assist/docs/responsible-ai) — 说明幻觉、偏差、安全过滤和有限领域能力，并强调生成代码必须经过人工审核。（Google · 2026-05-27）
- [Vibe Coding 难解音画同步问题](https://v2ex.com/t/1215040) — 以音画同步失败说明底层复杂问题不能靠反复抽取答案，应先理解核心链路再用 AI 加速。（V2EX · dsd2077 · 2026-05-24）
- ⭐ **精选** [Gemini CLI 迁移至 Antigravity CLI 公告](https://github.com/google-gemini/gemini-cli/discussions/27274) — 公告确认 2026 年 6 月 18 日起个人免费及 Pro、Ultra 终端体验迁至 Antigravity CLI，企业与 API 使用继续保留。（Google Gemini CLI · 2026-05-19）
- [中文社区 AI 编程工具实用对比](https://www.v2ex.com/t/1210849) — 用户按当时价格与体验比较 Claude Code、Codex、Cursor、TRAE、通义灵码和 Qoder。（V2EX · fireeeeee · 2026-05-07）
- [Vibe Coding 从入门到 Harness Engineering](https://linux.do/t/topic/2085611) — 以开源项目自荐形式串联 Prompt、上下文、MCP、Skills、规格驱动开发和 Harness Engineering。（LINUX DO · joytion · 2026-04-30）

## Agent 技能

- ⭐ **精选** [Superpowers 智能体开发方法论](https://github.com/obra/superpowers) — 将头脑风暴、测试驱动开发、系统调试、评审和验证组织成可组合的强约束技能。（Jesse Vincent · 2025-10-09）
- ⭐ **精选** [Anthropic Agent Skills 官方仓库](https://github.com/anthropics/skills) — 官方示例展示如何用 SKILL.md、脚本和参考资料封装可复用的智能体能力。（Anthropic · 2025-09-22）
- ⭐ **精选** [Spec Kit 规格驱动开发工具包](https://github.com/github/spec-kit) — 通过原则、规格、计划和任务阶段把模糊想法转成可验证的软件交付流程。（GitHub · 2025-08-21）
- ⭐ **精选** [GitHub Awesome Copilot 配置合集](https://github.com/github/awesome-copilot) — GitHub 官方维护的指令、提示文件、定制智能体和技能示例导航。（GitHub · 2025-06-11）
- [Claude Code 专业子智能体合集](https://github.com/VoltAgent/awesome-claude-code-subagents) — 提供覆盖开发、测试、安全、运维和产品等岗位的可委派子智能体模板。（VoltAgent · 2025-07-30）
- [Claude Code Templates 配置工具箱](https://github.com/davila7/claude-code-templates) — 汇集 agents、commands、hooks、MCP 和 settings 模板，并提供配套管理工具。（davila7 · 2025-07-04）
- [Awesome Claude Code 资源精选](https://github.com/hesreallyhim/awesome-claude-code) — 精选 Claude Code 的 Skills、Agents、Hooks、插件和开发辅助工具。（hesreallyhim · 2025-04-19）
- [BMAD 多角色敏捷开发方法](https://github.com/bmad-code-org/BMAD-METHOD) — 以分析师、产品经理、架构师和开发者等角色推动结构化的智能体开发生命周期。（BMAD Code · 2025-04-13）
- [Awesome Cursor Rules 规则集合](https://github.com/PatrickJS/awesome-cursorrules) — 按语言和框架整理 Cursor 项目规则，可用于理解旧版规则生态并迁移到新版目录格式。（PatrickJS · 2024-09-16）
- [GitHub Copilot 自定义能力速查表](https://docs.github.com/en/copilot/reference/customization-cheat-sheet) — 对比项目指令、提示文件、智能体、技能、钩子和 MCP 的位置与支持范围。（GitHub Docs）

## 开源项目

- ⭐ **精选** [OpenCode 开源终端编程智能体](https://github.com/anomalyco/opencode) — 提供终端优先的多模型编程智能体、完整交互界面和可扩展提供商支持。（Anomaly · 2025-04-30）
- ⭐ **精选** [Gemini CLI 开源企业与 API 终端智能体](https://github.com/google-gemini/gemini-cli) — 该 Apache-2.0 项目继续服务企业和 API 用户，个人免费及 Pro、Ultra 终端入口已迁移到 Antigravity CLI。（Google · 2025-04-17）
- ⭐ **精选** [Codex CLI 开源编程智能体](https://github.com/openai/codex) — OpenAI 的本地终端智能体可读写代码、运行命令并与云端、桌面端和 IDE 协作。（OpenAI · 2025-04-13）
- ⭐ **精选** [Model Context Protocol 参考服务器](https://github.com/modelcontextprotocol/servers) — 汇集官方参考服务器并导航社区实现，展示统一协议连接文件、Git 和外部服务的方式。（Model Context Protocol · 2024-11-19）
- ⭐ **精选** [OpenHands 开源软件开发平台](https://github.com/OpenHands/OpenHands) — 让智能体通过代码编辑、终端和浏览器完成软件工程任务，并支持本地或平台部署。（OpenHands · 2024-03-13）
- [Context7 最新文档上下文服务](https://github.com/upstash/context7) — 通过 MCP 注入特定版本的官方库文档，减少过期接口和虚构用法。（Upstash · 2025-03-26）
- [Serena 智能体语义编程工具](https://github.com/oraios/serena) — 借助语言服务器为编程智能体提供符号级导航、语义检索和精确编辑。（Oraios · 2025-03-23）
- [Roo Code 多模式编辑器智能体](https://github.com/RooCodeInc/Roo-Code) — 从 Cline 生态发展出的 VS Code 智能体，强调角色模式、任务编排和团队配置。（Roo Code · 2024-10-31）
- [Goose 模型无关开发智能体](https://github.com/aaif-goose/goose) — 现由 AAIF 维护的可扩展开源智能体，可安装依赖、编辑、执行和测试代码。（AAIF · 2024-08-23）
- [Repomix 仓库上下文打包工具](https://github.com/yamadashy/repomix) — 将代码库整理为适合模型输入的单文件，并提供过滤、令牌统计和安全检查。（yamadashy · 2024-07-13）
- [Cline 编辑器编程智能体](https://github.com/cline/cline) — 在编辑器内提供可审批的读取、修改、命令执行和验证流程，并支持多模型。（Cline · 2024-07-06）
- [SWE-agent 自动修复 GitHub Issue](https://github.com/SWE-agent/SWE-agent) — 将真实 Issue、终端环境和模型连接起来，自动定位、修改并测试软件修复。（Princeton NLP · 2024-04-02）
- [AutoGen 多智能体应用框架](https://github.com/microsoft/autogen) — 提供智能体、工具、消息和多智能体协作抽象，可用于搭建软件工程代理系统。（Microsoft · 2023-08-18）
- [Continue 开源 IDE 编程平台](https://github.com/continuedev/continue) — 支持自定义模型、上下文提供器、规则和智能体工作流，适合自托管与企业定制。（Continue · 2023-05-24）
- [Aider 终端 AI 结对编程工具](https://github.com/Aider-AI/aider) — 以 Git、代码地图和终端对话为核心，提供成熟的多模型结对编程工作流。（Aider · 2023-05-09）

## 工具

- ⭐ **精选** [Claude Code 开源仓库](https://github.com/anthropics/claude-code) — Anthropic 的终端编程代理仓库，包含安装说明、使用入口与问题反馈渠道。（Anthropic）
- [文心快码 Comate 产品能力](https://cloud.baidu.com/doc/COMATE/s/xlnvqe047) — 覆盖多智能体、自定义 Agent、Rules、MCP、补全、知识增强和独立 AI IDE。（百度智能云 · 2026-04-01）
- [腾讯 CodeBuddy 产品形态总览](https://cloud.tencent.com/document/product/1749/104236) — 对比插件、独立 IDE 与 CLI 三种形态，并说明 Craft、子智能体和自动化工作流。（腾讯云 · 2025-10-11）
- [Cursor Rules 项目规范指南](https://docs.cursor.com/context/rules) — 介绍项目规则、用户规则、记忆、触发类型和嵌套目录的当前官方机制。（Cursor）
- [DeepSeek 接入 Claude Code](https://api-docs.deepseek.com/guides/agent_integrations/claude_code) — 使用官方 Anthropic 兼容端点将 DeepSeek 模型配置到 Claude Code。（DeepSeek）
- [GLM Coding Plan 接入指南](https://docs.bigmodel.cn/cn/coding-plan/quick-start) — 介绍如何把 GLM 编程模型接入 Claude Code、Cursor、OpenCode 和 Cline 等工具。（智谱 AI）
- [Gemini CLI 工具与安全审批机制](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md) — 解释文件、Shell、Web 和 MCP 工具，以及确认、沙箱和可信目录等执行边界。（Google）
- [TRAE AI 原生 IDE](https://www.trae.ai/ide) — 字节系 AI 原生开发环境入口，面向个人开发者提供智能体式编码体验。（TRAE）
- [Windsurf Cascade 技能指南](https://docs.windsurf.com/windsurf/cascade/skills) — 使用 SKILL.md、脚本、模板和参考资料封装复杂流程，并按需渐进加载内容。（Windsurf）
- [Windsurf 记忆、Rules 与 AGENTS.md](https://docs.windsurf.com/zh/windsurf/cascade/memories) — 官方中文文档比较 Rules、AGENTS.md、Workflows、Skills 和自动记忆的持久化方式。（Windsurf）
- [通义灵码项目规则指南](https://help.aliyun.com/zh/lingma/qoder-cn/user-guide/rules) — 说明项目规则目录及手动、模型判断、始终启用和文件匹配四类触发方式。（阿里云）

## 公司与产品

- ⭐ **精选** [Gemini CLI 迁移至 Antigravity CLI 公告](https://github.com/google-gemini/gemini-cli/discussions/27274) — 公告确认 2026 年 6 月 18 日起个人免费及 Pro、Ultra 终端体验迁至 Antigravity CLI，企业与 API 使用继续保留。（Google Gemini CLI · 2026-05-19）
- ⭐ **精选** [OpenAI Codex 官方开发者入口](https://developers.openai.com/) — 聚合 Codex 产品、开发文档、案例和智能体编程资源的官方入口。（OpenAI）
- [Claude Code 正式可用与 Claude 4](https://www.anthropic.com/news/claude-4) — 记录 Claude Code 正式可用，并介绍后台任务、IDE 集成和代理式开发能力。（Anthropic · 2025-05-22）
- [Amazon Q Developer 官方文档中心](https://aws.amazon.com/documentation-overview/q-developer/) — 覆盖 IDE 对话、代码解释、修复、测试以及从自然语言生成完整功能的官方资料。（AWS）
- [Cloudflare Workers AI 平台](https://developers.cloudflare.com/workers-ai/) — 在 Cloudflare GPU 网络运行开放模型，并可结合 AI Gateway 与 Vectorize 构建应用。（Cloudflare）
- [GitHub Copilot 云端智能体](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) — 介绍异步处理 Issue、在独立环境编码并创建草稿拉取请求的云端智能体。（GitHub Docs）
- [Lovable 自然语言全栈开发平台](https://docs.lovable.dev/introduction/welcome) — 生成前端、后端、数据库、认证和集成，并支持 GitHub 同步与部署。（Lovable）
- [Replit Agent 云端应用开发](https://docs.replit.com/learn/build-with-agent) — 在云端从想法生成、运行、调试并发布应用，覆盖从编码到托管的一体化路线。（Replit）
- [Vercel AI SDK 开发工具包](https://vercel.com/ai-sdk) — 面向 TypeScript 提供多模型调用、流式响应、工具调用和智能体开发能力。（Vercel）
- [Vercel v0 全栈应用生成器](https://vercel.com/docs/v0) — 从自然语言生成界面、落地页和全栈应用，并可直接衔接 Vercel 部署。（Vercel）

## 文章

- ⭐ **精选** [Harness Engineering 智能体优先代码库实践](https://openai.com/index/harness-engineering/) — 总结仓库可读性、约束、反馈回路、文档结构和持续熵管理等智能体工程经验。（OpenAI · 2026-02-11）
- ⭐ **精选** [Claude Code 智能体编程最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices) — 系统讲解项目指令、探索与计划、测试驱动开发、上下文管理和独立审查。（Anthropic Engineering · 2025-04-18）
- ⭐ **精选** [别把所有 AI 辅助编程都叫 Vibe Coding](https://simonwillison.net/2025/Mar/19/vibe-coding/) — 区分忽略代码细节的原始 Vibe Coding 与工程师审阅、理解并负责的 AI 辅助开发。（Simon Willison · 2025-03-19）
- [Gemini Code Assist 负责任 AI 指南](https://developers.google.com/gemini-code-assist/docs/responsible-ai) — 说明幻觉、偏差、安全过滤和有限领域能力，并强调生成代码必须经过人工审核。（Google · 2026-05-27）
- [Symphony 项目看板智能体编排规范](https://openai.com/index/open-source-codex-orchestration-symphony/) — 将项目管理看板变成编程智能体控制面，用工作队列缓解多任务上下文切换。（OpenAI · 2026-04-27）
- [Cursor 如何用自主 Agent 守护代码库](https://cursor.com/blog/security-agents) — 展示持续安全审查、漏洞发现、依赖更新和不变量检查等可复用智能体模板。（Cursor · 2026-03-16）
- [AI 编码实践：从 Vibe Coding 到 SDD](https://zhuanlan.zhihu.com/p/2001605764670833810) — 淘特导购团队复盘从补全、智能体与规则演进到轻量规格驱动开发的工程方案。（阿里云开发者）
- [Lovable 应用安全总览](https://docs.lovable.dev/features/security) — 覆盖密钥防泄漏、行级安全、数据库、代码和依赖扫描以及发布前检查。（Lovable）
- [Replit 共享责任模型](https://docs.replit.com/references/security/shared-responsibility-model) — 划分平台、智能体、开发环境、已发布应用和用户各自承担的安全责任。（Replit）
- [为什么 SWE-bench Verified 已难衡量前沿能力](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) — 分析测试缺陷和数据污染如何削弱榜单区分度，提醒读者谨慎解读单一基准。（OpenAI）

## 教程

- ⭐ **精选** [Easy-Vibe 会说话就会做应用](https://github.com/datawhalechina/easy-vibe) — 面向零基础到进阶开发者的开源课程，覆盖全栈、RAG、MCP、SaaS 和小程序开发。（Datawhale）
- [文心快码 Zulu Agent 入门](https://cloud.baidu.com/doc/COMATE/s/vm66asjm4) — 演示从需求到代码、多智能体拆解、命令执行、验证和迭代的完整流程。（百度智能云 · 2026-02-28）
- [Bolt 十分钟应用快速开始](https://support.bolt.new/building/quickstart) — 通过完整示例演示从提示、数据库和登录到预览及发布的浏览器开发流程。（Bolt）
- [Claude Code 安装与快速开始](https://docs.anthropic.com/en/docs/claude-code/getting-started) — 官方说明安装、登录、系统要求、更新方式和首次运行终端任务的步骤。（Anthropic）
- [Codex 官方实战案例库](https://developers.openai.com/codex/use-cases) — 展示代码迁移、安全扫描、拉取请求审查、前端构建、测试和自动化等任务模式。（OpenAI）
- [Gemini CLI 企业与 API 用户快速开始](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/index.md) — 介绍安装、认证、配置和首个任务，个人免费及 Pro、Ultra 用户应改用 Antigravity CLI。（Google）
- [GitHub Copilot 自定义案例库](https://docs.github.com/en/copilot/tutorials/customization-library) — 官方整理可直接复用的项目指令、提示文件和定制智能体实例。（GitHub Docs）
- [Lovable 产品开发提示最佳实践](https://docs.lovable.dev/prompting/prompting-one) — 从需求澄清、用户旅程和组件化构建讲到版本控制与逐步迭代。（Lovable）
- [Replit Vibe Coding 安全清单](https://docs.replit.com/learn/security-checklist) — 从前端、后端、HTTPS、认证和输入验证到持续维护逐项检查生成式应用。（Replit）
- [通义灵码多文件修改与单元测试](https://help.aliyun.com/zh/lingma/user-guide/edit/) — 官方讲解需求拆分、上下文选择、快照回退以及测试的生成、运行与修复。（阿里云）

## 社区

- ⭐ **精选** [Vibe Coding 生产项目实践讨论](https://linux.do/t/topic/2360067) — 针对老项目失控问题讨论 SDD、TDD、灰度、备份、多模型互审和人工评审。（LINUX DO · eof_karel · 2026-06-10）
- ⭐ **精选** [培训 Codex 后工作反而更多了](https://linux.do/t/topic/2268339) — 记录内部工具培训后工期被压缩、任务增加的经历，呈现效率收益分配的组织争议。（LINUX DO · fairyw · 2026-05-29）
- ⭐ **精选** [大量生成代码后的线上质量责任](https://www.v2ex.com/t/1208265) — 讨论人工编写测试、拉取请求钩子和独立复核，警惕同一智能体为过测试采用脏实现。（V2EX · kyrieIvring · 2026-04-24）
- [AI 编程普及率的信息茧房](https://www.v2ex.com/t/1221461) — 通过自由职业者和回复者的个人经历提醒读者，技术社区热度不等于全行业普及率。（V2EX · NotAfraidLP · 2026-06-19）
- [一个未能实现的 Vibe Coding Harness](https://linux.do/t/topic/2306363) — 尝试用意图分析、提示质量记录和上下文注入降低门槛，并坦诚保留无法实现的结论。（LINUX DO · Soei · 2026-06-04）
- [Vibe Coding 进入工作后如何长效维护](https://linux.do/t/topic/2279770) — 围绕真实线下工具投入生产后的维护成本，讨论从生成成品转向固定协作流程。（LINUX DO · skyrock · 2026-05-31）
- [Vibe Coding 难解音画同步问题](https://v2ex.com/t/1215040) — 以音画同步失败说明底层复杂问题不能靠反复抽取答案，应先理解核心链路再用 AI 加速。（V2EX · dsd2077 · 2026-05-24）
- [中文社区 AI 编程工具实用对比](https://www.v2ex.com/t/1210849) — 用户按当时价格与体验比较 Claude Code、Codex、Cursor、TRAE、通义灵码和 Qoder。（V2EX · fireeeeee · 2026-05-07）
- [Vibe Coding 从入门到 Harness Engineering](https://linux.do/t/topic/2085611) — 以开源项目自荐形式串联 Prompt、上下文、MCP、Skills、规格驱动开发和 Harness Engineering。（LINUX DO · joytion · 2026-04-30）
- [中文开发者都在 Vibe Coding 什么项目](https://linux.do/t/topic/2051569) — 汇集装箱工具、启动页、自动打卡、桌面启动器、小说界面和浏览器插件等真实选题。（LINUX DO · duiguangbin · 2026-04-25）
- [Vibe Coding 的意义与工程边界](https://v2ex.com/t/1208240) — 高互动讨论主张架构、接口和责任边界由人掌握，AI 负责小步局部实现。（V2EX · chuchen023 · 2026-04-24）
- [Vibe Coding 一周体验与工程流程](https://www.v2ex.com/t/1203913) — 详细记录原型、业务与权限文档、前后端智能体、人工验证、评审和提交的流程。（V2EX · a526796017 · 2026-04-07）

## 研究

- ⭐ **精选** [SlopCodeBench 长期代码退化基准](https://arxiv.org/abs/2603.24755) — 让智能体连续响应变化需求，衡量代码冗余和结构侵蚀如何随多轮迭代增长。（Gabriel Orlanski 等 · 2026-03-25）
- ⭐ **精选** [Terminal-Bench 真实终端任务基准](https://arxiv.org/abs/2601.11868) — 以独立环境、人工解法和测试评估智能体完成复杂长时终端工作流的能力。（Mike A. Merrill 等 · 2026-01-17）
- ⭐ **精选** [SecureAgentBench 安全编码基准](https://arxiv.org/abs/2509.22097) — 用真实漏洞场景的多文件任务同时检查功能、已知漏洞和新引入的安全问题。（Junkai Chen 等 · 2025-09-26）
- ⭐ **精选** [早期 2025 AI 工具对资深开发者生产力的影响](https://arxiv.org/abs/2507.09089) — 随机对照实验发现特定早期工具让成熟仓库的资深维护者平均变慢，结论不应泛化到所有场景。（Joel Becker 等 · 2025-07-12）
- ⭐ **精选** [SWE-bench 真实软件工程基准](https://www.swebench.com/original.html) — 要求模型依据真实 GitHub Issue 修改完整仓库并通过测试，奠定现代编程智能体评价方式。（Carlos E. Jimenez 等）
- [SWE-rebench V2 多语言任务流水线](https://arxiv.org/abs/2602.23866) — 将任务收集扩展到二十种语言和数千个仓库，更贴近真实多语言软件生态。（Ibragim Badertdinov 等 · 2026-02-27）
- [JAWS-BENCH 编程智能体越狱评估](https://arxiv.org/abs/2510.01359) — 比较不同工作区上下文中的可执行恶意代码攻击，评估智能体包装对越狱风险的放大。（Shoumik Saha 等 · 2025-10-01）
- [SWE-rebench 持续更新软件工程基准](https://arxiv.org/abs/2505.20411) — 自动从新 GitHub 拉取请求抽取可执行任务，以新鲜数据降低固定榜单污染。（Ibragim Badertdinov 等 · 2025-05-26）
- [SWE-smith 软件工程训练数据](https://arxiv.org/abs/2504.21798) — 从一百二十八个仓库合成约五万个可执行任务，并训练开源软件工程智能体模型。（John Yang 等 · 2025-04-30）
- [SWE-Lancer 真实外包任务基准](https://arxiv.org/abs/2502.12115) — 用一千四百多个真实软件工程和管理任务评估模型能否完成有经济价值的外包工作。（Samuel Miserendino 等 · 2025-02-17）
- [SWE-bench Verified 人工核验基准](https://openai.com/index/introducing-swe-bench-verified/) — 人工核验五百个软件修复任务以降低测试缺陷和描述歧义，阅读时应结合其后续退役说明。（OpenAI 与 SWE-bench · 2024-08-13）
<!-- AWESOME-VIBE:END -->
