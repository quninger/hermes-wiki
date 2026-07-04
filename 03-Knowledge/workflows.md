---
title: "Agent 标准化工作流"
created: 2026-07-04
updated: 2026-07-04
type: workflow
tags: [workflow, 核心, 系统]
---

# 🔄 Agent 标准化工作流

> **核心原则**: 所有工作、任务、对话、流程方案，100% 沉淀至 Obsidian 知识库
> **闭环规则**: 先查流程 → 再执任务 → 绑定路径 → 归档沉淀 → 记忆固化

---

## 📋 工作流总览

| 工作流 | 名称 | 作用 | 周期/触发 | 推送 | 隐私 |
|--------|------|------|-----------|------|------|
| WF-01 | 每日日志 | 记录每日工作、复盘总结 | 每日 | ✅ 推送 GitHub | 普通 |
| WF-02 | 收件箱处理 | 清理临时笔记，分流归类 | 每日 | ❌ 不推送 | 可能含隐私 |
| WF-03 | 知识沉淀 | 将零散笔记转化为常青知识 | 每周 | ✅ 推送 GitHub | 普通 |
| WF-04 | 项目管理 | 跟踪项目进度、记录里程碑 | 按需 | ✅ 推送 GitHub | 普通 |
| WF-05 | 会话归档 | 整理过期会话，压缩存储 | 每周 | ❌ 不推送 | 隐私 |
| WF-06 | 月度复盘 | 归档项目、优化结构、梳理体系 | 每月 | ✅ 推送 GitHub | 普通 |
| WF-07 | GitHub 同步 | 提交变更、推送远程 | 每日/按需 | ✅ 推送 GitHub | N/A |
| WF-08 | 求职准备 | 简历、面试题、项目整理 | 按需 | ❌ 不推送 | 隐私 |
| WF-09 | 技术调研 | 框架对比、方案评估 | 按需 | ✅ 推送 GitHub | 普通 |
| WF-10 | 网页收藏 | 提取优质内容、保存链接 | 按需 | ✅ 推送 GitHub | 普通 |
| WF-11 | 编码任务 | 编码工作按难度分层：普通→deepseek，困难→Cursor CLI | 按需 | ❌ 不推送 | 普通 |

---

## 🔧 执行流程（四步法）

### 步骤 1：匹配模板与路径
```
收到任务 → 查阅本表 → 匹配工作流 → 获取：
  ├── 资源来源文件（素材、数据）
  ├── 执行模板文件（输出格式）
  └── 结果归档路径（存储位置）
```

### 步骤 2：按流程执行
- 严格遵循既定步骤，不新增、不简化、不更改
- 遇到问题先查 03-Knowledge，再查外部资源

### 步骤 3：分层沉淀
```
沉淀层级：
├── 主页.md ← 所有工作流精简简介
├── 工作流详情文档 ← 完整流程细则
└── 日志/归档 ← 执行记录
```

### 步骤 4：记忆固化
- 定稿工作流存入 Hermes 长期记忆
- 后续任务优先匹配既定规则

---

## 📁 关联路径

| 工作流 | 模板路径 | 归档路径 | 推送范围 |
|--------|----------|----------|----------|
| 每日日志 | `04-Resource/templates/daily-template.md` | `01-Daily/` | `01-Daily/`, `03-Knowledge/` |
| 收件箱处理 | `04-Resource/templates/inbox-template.md` | `00-Inbox/` → 各目录 | ❌ 不推送 |
| 知识沉淀 | `04-Resource/templates/knowledge-template.md` | `03-Knowledge/` | `03-Knowledge/` |
| 项目管理 | `04-Resource/templates/project-template.md` | `02-Project/` | `02-Project/` |
| 会话归档 | `04-Resource/templates/archive-template.md` | `98-Archive/` | ❌ 不推送 |
| 月度复盘 | `04-Resource/templates/monthly-template.md` | `01-Daily/` | `01-Daily/` |
| GitHub 同步 | 无 | 无 | 全部 |
| 求职准备 | 无固定模板 | `02-Project/求职/` | ❌ 不推送 |
| 技术调研 | `04-Resource/templates/knowledge-template.md` | `03-Knowledge/` | `03-Knowledge/` |
| 网页收藏 | `04-Resource/templates/webclip-template.md` | `00-Inbox/` → `03-Knowledge/` | `03-Knowledge/` |

---

## 🔒 推送规则

### ✅ 推送（公开内容）
- `01-Daily/` — 每日日志（脱敏后）
- `02-Project/` — 项目记录
- `03-Knowledge/` — 知识笔记
- `04-Resource/` — 模板和资源
- `index.md` — 首页导航

### ❌ 不推送（隐私内容）
- `00-Inbox/` — 临时笔记（可能含敏感信息）
- `98-Archive/` — 归档内容
- `99-Assets/` — 附件资源
- `.hermes/` — Hermes 内部文件
- `.obsidian/` — Obsidian 配置
- `02-Project/求职/` — 求职相关（简历、面试）

---

## 📝 操作日志

| 日期 | 操作 | 工作流 |
|------|------|--------|
| 2026-07-04 | 创建标准化工作流体系 | WF-00 系统搭建 |
