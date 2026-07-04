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
- 工作流表从6列精简为4维度：名称 | 类型 | 归档 | GitHub
- 修正：每日日志→❌不推送，月度复盘→❌不推送，GitHub同步→按需
- 新增 SCHEMA.md 4维度 Frontmatter 强制规范（workflow/archive/github/privacy）
- 新增 `.gitignore` 规则 `[github_forbid]*` 自动忽略不归档文件
- 新增 workflows.md [github_forbid] 文件命名规则章节
- 现有知识笔记全部添加4维度 Frontmatter
- Workflow Commander 同步：12个任务全部含 pushGitHub/archiveNeeded 字段
