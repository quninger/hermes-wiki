# Wiki Log

> 按时间顺序记录所有 wiki 操作。只追加。
> 格式: `## [YYYY-MM-DD] 操作 | 主题`
> 操作: ingest, update, query, lint, create, archive, delete

## [2026-06-14] create | Wiki 初始化
- 领域: AI Agent / 前端 Agent 工程
- 结构创建: SCHEMA.md, index.md, log.md
- 目录: raw/{articles,papers,transcripts,assets}, entities, concepts, comparisons, queries

## [2026-07-04] create | Hermes Agent 工作流与模型编排
- 创建: 03-Knowledge/concepts/【AI工程】Hermes-Agent工作流与模型编排.md
- 创建: 04-Resource/hermes-agent-workflow.html（可展示个人网页）
- 领域: AI Agent 工作流 / 模型编排 / 工具集 / 知识管理
- 工作流: WF-03 知识沉淀
- [查看网页](04-Resource/hermes-agent-workflow.html)

## [2026-07-04] update | 差距补齐 + 验收测试
- 工作流表新增 WF-12 模型编排
- WF-05 会话归档补充细则（≤1000字、问题→方案→结果）
- 创建 `主页.md` 作为第一查阅入口
- 创建 `04-Resource/templates/会话归档模板.md`
- 工作流详情追加 WF-12 模型编排执行细则 + WF-05 会话归档细则
- 运行 5 项验收测试全部通过
- 创建验收测试报告
- 记忆固化工作流核心原则

## [2026-07-04] create | Workflow Commander 交互模拟器
- 创建 `04-Resource/workflow-commander.html` 互动网页模拟器
- 完整演示：小模型规划→大模型执行→4步工作流闭环
- 可视化模型链路由 + 实时执行日志 + 归档路径动画
- 10种预设任务覆盖全部12个WF工作流

## [2026-07-04] update | 4维度重构 + [github_forbid] 规则
- 工作流表从6列精简为4维度：名称|类型|归档|GitHub
- 修正：每日日志→❌不推送，月度复盘→❌不推送，GitHub同步→按需
- 新增 SCHEMA.md 4维度 Frontmatter 强制规范（workflow/archive/github/privacy）
- 新增 `.gitignore` 规则 `[github_forbid]*` 自动忽略不归档文件
- 新增 workflows.md [github_forbid] 文件命名规则章节
- Workflow Commander 同步：12个任务全部含 pushGitHub/archiveNeeded 字段

## [2026-07-04] refactor | 分层架构重构：SOUL.md/主页.md/工作流详情
- SOUL.md 精简为入口规则+模型编排概要（不含工作流细节）
- 主页.md 增加4维度表+每个WF链接到Obsidian详细执行文件
- 创建 04-Resource/工作流/WF-01~12 共12个工作流详情文档
- 执行流程变为：查主页.md→打开详细文件→按文件内容执行
- 记忆固化更新，工作流细节不在记忆中重复存储

## [2026-07-04] create | 一键配置手册
- 创建 03-Knowledge/concepts/【系统】Agent工作流与模型编排-一键配置手册.md
- 7章完整内容：系统配置/Obsidian结构/4维度表/Frontmatter规范/记忆规则/[github_forbid]/一键配置步骤
- 适用于所有 Agent 客户端（Hermes/Cursor/Claude Code/Codex）
- 主页.md 快速链接已更新

## [2026-07-04] refactor | 模型编排升级v3.0 + 建立方案
- 模型编排升级为三层架构：主模型规划 → MoA/delegate/混合 → 执行聚合
- 创建 03-Knowledge/concepts/【系统】Hermes-Agent模型编排建立方案.md
- 9章完整内容：理解编排/模型画像/MoA配置/delegate模式/混合模式/决策逻辑/SOUL写入/验证/维护
- 主页.md 快速链接已更新

## [2026-07-04] archive | 三层编排会话归档（MoA+delegate）
- 按WF-12三层架构执行会话归档
- 第一层：主模型分析10个会话，决定编排策略
- 第二层A：delegate并行压缩Cron会话（2个子代理，5.72s）
- 第二层B：MoA deep分析丰富会话（2个子代理，138s）
- 第三层：聚合生成 98-Archive/会话归档/2026-07-04-会话归档汇总.md
