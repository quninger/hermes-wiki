---
title: "WF-07 GitHub 同步"
created: 2026-07-04
type: workflow-detail
tags: [workflow, 同步, GitHub]
---

# WF-07 GitHub 同步

## 概述
本地知识库与 GitHub 仓库保持同步，支持版本追溯和多设备协作。

## 数据来源
无外部数据来源，操作对象为本地 git 仓库。

## 输出模板
无固定模板，使用 git 命令操作。

## 版本控制规则

| 状态 | 含义 | 目录 |
|------|------|------|
| ✅ 推送 | commit + push | `01-Daily/`, `02-Project/`, `03-Knowledge/`, `04-Resource/` |
| 🔒 本地提交 | commit 不 push | `00-Inbox/`, `98-Archive/` |
| ❌ 不提交 | 仅本地文件 | `99-Assets/`, `.obsidian/`, `.hermes/` |

**pre-push hook** 自动阻止推送 `00-Inbox/` 和 `98-Archive/` 内容。

## 执行步骤

### 日常同步（推荐）

```bash
cd E:/工作需要/hermes-wiki

# 1. 开始前：拉取远程最新
git pull origin master

# 2. 工作中：频繁 commit
git add -A && git commit -m "feat: xxx"

# 3. 结束时：push 到远程
git push origin master
```

### 完整流程

```bash
# 1. 检查状态
git status

# 2. 拉取远程（避免冲突）
git pull --rebase origin master

# 3. 添加变更
git add -A

# 4. 提交（Conventional Commits）
git commit -m "feat(scope): 描述"

# 5. 推送（pre-push hook 自动过滤隐私内容）
git push origin master

# 6. 验证
git log --oneline -5
```

### 冲突处理

```bash
# 方式1：变基到最新（推荐）
git pull --rebase origin master

# 方式2：合并
git pull origin master

# 解决冲突后
git add <冲突文件>
git commit -m "fix: 解决合并冲突"
git push origin master
```

### 紧急推送（跳过 hook）

```bash
git push --no-verify  # 跳过 pre-push hook
```

## 提交规范（Conventional Commits）

```
type(scope): 描述

类型:
- feat: 新功能/新内容
- fix: 修复错误
- docs: 文档更新
- refactor: 重构/整理
- chore: 杂项维护
```

示例：
```bash
git commit -m "docs(工作流): 新增科技消息推送流程"
git commit -m "feat(知识库): 添加 WF-13 科技早报"
git commit -m "fix(模板): 修复归档模板格式"
```

## 关联文件
- Hook: `.git/hooks/pre-push`
- 规则: `.gitignore`
- 文档: `03-Knowledge/workflows.md`
