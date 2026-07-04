---
title: "【系统】Agent 工作流与模型编排配置手册"
created: 2026-07-04
updated: 2026-07-04
type: concept
tags: [agent, workflow, model-orchestration, config, 系统级]
workflow: WF-03
archive: true
github: allow
privacy: false
---

# Agent 工作流与模型编排 · 一键配置手册

> **文档用途**：将本文档交给任何 Agent 客户端，即可完成工作流系统配置。
> **适用对象**：Hermes Agent、Cursor、Claude Code、Codex 等支持系统提示词的 Agent。
> **配置方式**：将「第一章」写入 Agent 系统提示词（SOUL.md / System Prompt / User Rules），将「第二章」作为执行时的参考文件。

---

# 第一章：系统级配置（写入 Agent 底层）

> 以下内容直接写入 Agent 的系统提示词 / SOUL.md / User Rules，作为最高优先级执行规则。

```markdown
# 系统级执行规则（最高优先级）

## 入口
{vault_path}/主页.md — 第一查阅入口，每次任务必须先查看

## 执行流程
收到任务 → 查 主页.md → 匹配工作流 → 打开链接的详细执行文件 → 按文件内容执行 → 归档 → 固化记忆

## 四步法（每步都参照详细执行文件）
1. 匹配模板与路径 → 获取三类路径：资源来源 / 执行模板 / 结果归档
2. 按流程执行 → 严格遵循详细执行文件，遇问题先查 03-Knowledge
3. 分层沉淀 → 主页.md←总览 / 工作流详情 / 日志归档
4. 记忆固化 → 写入长期记忆，后续任务优先匹配

## [github_forbid] 规则
- 不归档任务输出文件加前缀 [github_forbid]
- gitignore 已配置 [github_forbid]* 自动跳过

## 模型编排（WF-12）

### 模型链（按优先级降序）
mimo (主模型) → deepseek (编码/推理) → glm (免费兜底) → siliconflow (备选池)

### 任务-模型路由
| 任务类型 | 首选 | 备选 |
|----------|------|------|
| 日常对话/写作 | mimo | deepseek |
| 轻量任务(文件压缩/方案规划/文档搜索/格式化/网页提取) | glm-4-flash | siliconflow |
| 技术调研/系统诊断/配置编辑 | deepseek | glm |
| 编码/调试/UI开发 | deepseek | Cursor CLI |
| 困难任务(重构/debug/架构) | Cursor CLI | deepseek |

### 子代理委派
| 难度 | 委派目标 | 场景 |
|------|----------|------|
| 轻量 | glm-4-flash (免费) | 文件压缩、方案规划、文档搜索、格式转换 |
| 中等 | deepseek | 代码审查、技术调研、系统诊断、Git操作 |
| 复杂 | mimo | 多文件协作、复杂应用、架构设计 |

- 最大3路并行，嵌套深度1层，结果异步返回

### 故障降级链
mimo → deepseek → glm-4-flash(免费) → siliconflow(免费)

### 编码任务
- 🟢 普通编码 → deepseek（原生工具）
- 🔴 困难编码 → Cursor CLI（cursor-agent.cmd --print --force --trust）

## 记忆规则
- 只存：可复用的工作流规则、系统配置、用户偏好
- 不存：单次执行结果、临时任务记录、会话日志
```

> **配置时替换**：`{vault_path}` 替换为实际 Obsidian 知识库路径（如 `E:/工作需要/hermes-wiki`）

---

# 第二章：Obsidian 知识库结构

> 以下内容是 Obsidian 知识库的标准目录结构和文件清单，Agent 按此结构执行。

## 2.1 六段式目录

```
{vault_path}/
├── 00-Inbox/          # 收件箱（临时灵感、速记，不分类不整理）
├── 01-Daily/          # 每日日志（日/周/月复盘、日程、待办）
├── 02-Project/        # 项目库（短期任务、项目、目标）
├── 03-Knowledge/      # 知识库（常青笔记、永久知识、体系化内容）
│   ├── concepts/      # 概念定义、原理讲解
│   ├── entities/      # 实体页（人物/公司/模型）
│   ├── comparisons/   # 对比分析、横评
│   ├── queries/       # 查询与问答
│   └── summaries/     # 综合总结
├── 04-Resource/       # 资源库（模板、教程、素材、参考资料）
│   ├── templates/     # 各类模板集中存放
│   └── 工作流/        # 工作流详细执行文件（WF-01~12）
├── 99-Assets/         # 全局附件（图片、截图、文件、音视频）
├── 98-Archive/        # 归档库（完结项目、过期笔记、历史记录）
├── 主页.md            # 第一查阅入口（工作流总览+4维度表+链接）
├── index.md           # 首页导航
├── SCHEMA.md          # 知识库规范
└── log.md             # 操作日志
```

## 2.2 核心文件清单

| 文件 | 用途 | 优先级 |
|------|------|--------|
| `主页.md` | 第一查阅入口，4维度工作流表+链接 | 最高 |
| `SCHEMA.md` | 知识库规范（Frontmatter、命名、标签） | 高 |
| `log.md` | 操作日志（只追加） | 中 |
| `04-Resource/templates/` | 模板文件夹 | 中 |
| `04-Resource/工作流/` | 12个工作流详情文件 | 高 |

---

# 第三章：工作流4维度表

> Agent 执行时参照此表匹配工作流，点击链接查看详细执行方案。

| # | 工作流 | 类型 | 归档 | GitHub | 详细文件 |
|:-:|:-------|:----:|:----:|:------:|:---------|
| 1 | 📅 每日日志 | 每日 | ✅ 需要(本地) | ❌ 禁止 | `04-Resource/工作流/WF-01-每日日志.md` |
| 2 | 📥 收件箱处理 | 每日 | ✅ 需要 | ❌ 禁止(隐私) | `04-Resource/工作流/WF-02-收件箱处理.md` |
| 3 | 📚 知识沉淀 | 每周 | ✅ 需要 | ✅ 推送 | `04-Resource/工作流/WF-03-知识沉淀.md` |
| 4 | 🎯 项目管理 | 按需 | ✅ 需要 | ✅ 推送 | `04-Resource/工作流/WF-04-项目管理.md` |
| 5 | 📝 会话归档 | 每周 | ✅ 需要 | ❌ 禁止(隐私) | `04-Resource/工作流/WF-05-会话归档.md` |
| 6 | 📊 月度复盘 | 每月 | ✅ 需要(本地) | ❌ 禁止 | `04-Resource/工作流/WF-06-月度复盘.md` |
| 7 | 🔄 GitHub同步 | 按需 | ❌ 不需要 | N/A | `04-Resource/工作流/WF-07-GitHub同步.md` |
| 8 | 🔒 求职准备 | 按需 | ✅ 需要 | ❌ 禁止(隐私) | `04-Resource/工作流/WF-08-求职准备.md` |
| 9 | 🔍 技术调研 | 按需 | ✅ 需要 | ✅ 推送 | `04-Resource/工作流/WF-09-技术调研.md` |
| 10 | 📎 网页收藏 | 按需 | ✅ 需要 | ✅ 推送 | `04-Resource/工作流/WF-10-网页收藏.md` |
| 11 | 💻 编码任务 | 按需 | ❌ 不需要 | ❌ 禁止 | `04-Resource/工作流/WF-11-编码任务.md` |
| 12 | 🧠 模型编排 | 每次任务 | ❌ 不需要 | N/A | `04-Resource/工作流/WF-12-模型编排.md` |

---

# 第四章：Frontmatter 规范

> 每篇归档笔记必须包含以下 YAML frontmatter。

```yaml
---
title: "页面标题"
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [标签列表]
workflow: WF-xx          # 所属工作流（如 WF-03、WF-09）
archive: true | false    # 是否需要本地归档
github: allow | forbid | na  # GitHub 推送策略
privacy: true | false    # 是否含隐私内容
---
```

---

# 第五章：记忆规则

> Agent 的长期记忆（SOUL.md / Memory）应遵循以下规则：

## ✅ 应该存入记忆的
- 工作流入口规则（查主页.md→匹配WF→打开详细文件执行）
- 模型编排规则（模型链、任务路由、委派规则）
- 用户偏好（格式要求、推送习惯、命名规范）
- 环境配置（工具路径、API密钥、Git配置）
- 系统规则（限速铁律、安全规则、隐私边界）

## ❌ 不应存入记忆的
- 单次任务的执行结果
- 临时会话记录
- 已过期的项目状态
- 可从文件中读取的工作流细节（存文件不存记忆）

---

# 第六章：[github_forbid] 文件命名规则

> 对于不需要归档的任务，输出文件命名遵循以下规则：

1. 文件名以 `[github_forbid]` 开头
2. `.gitignore` 中配置 `[github_forbid]*` 自动忽略
3. git 操作时自动跳过，无需手动排除
4. 文件仍保留在本地

**示例**：`[github_forbid]数据清洗脚本调试.md`

---

# 第七章：一键配置步骤

## 步骤 1：创建 Obsidian 知识库

按「第二章」的目录结构创建六段式目录。

## 步骤 2：创建核心文件

- `主页.md` — 按「第三章」创建4维度表+链接
- `SCHEMA.md` — 按「第四章」创建 Frontmatter 规范
- `log.md` — 创建空操作日志

## 步骤 3：创建工作流详情文件

在 `04-Resource/工作流/` 下创建 12 个 WF-xx.md 文件，每个包含：
- YAML frontmatter（workflow/archive/github/privacy）
- 目的、触发条件、执行步骤、模板路径、归档路径、注意事项

## 步骤 4：配置 Agent 系统提示词

将「第一章」的内容写入 Agent 的系统提示词（SOUL.md / System Prompt / User Rules）。

## 步骤 5：配置 Git

- `.gitignore` 添加 `[github_forbid]*`
- 排除隐私目录（`00-Inbox/`、`98-Archive/`、`.obsidian/`、`.hermes/`）

## 步骤 6：验证

运行验收测试（参考 `02-Project/【项目】工作流验收测试.md`），确保：
- ✅ 环境确认（目录存在、文件可读）
- ✅ Inbox 流转（捕捉→处理→清理）
- ✅ 四步工作流（匹配→执行→沉淀→固化）
- ✅ 会话归档（≤1000字，问题→方案→结果）
- ✅ 系统记忆验证（入口规则、4维度规则已写入）

---

> **最后更新**: 2026-07-04
> **维护者**: Hermes Agent @ Nous Research
> **适用范围**: 所有支持系统提示词的 Agent 客户端
