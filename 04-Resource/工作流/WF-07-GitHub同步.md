---
workflow:
  id: WF-07
  name: GitHub 同步
  version: "1.0"
  category: 版本管理
  status: 活跃
archive:
  location: N/A（Git 仓库即归档）
  naming: 遵循 Git 提交规范
  retention: 永久（Git 历史）
github:
  repo: hermes-wiki
  branch: main
  path: 04-Resource/工作流/WF-07-GitHub同步.md
privacy:
  level: 公开
  contains: Git 操作流程、提交规范、分支策略
---

# WF-07 GitHub 同步工作流

## 目的

将本地 Wiki 知识库与 GitHub 仓库保持同步，确保内容安全备份、版本可追溯、支持多设备协作。

## 触发条件

- 完成重要文档更新后
- 新增或修改工作流/技能文件后
- 每日工作结束时（如有变更）
- 用户主动要求同步时

## 执行步骤

### 步骤 1：检查状态

1. 进入工作目录：
   ```bash
   cd /e/工作需要/hermes-wiki
   ```
2. 检查 Git 状态：
   ```bash
   git status
   ```
3. 确认：
   - 有哪些文件被修改/新增/删除
   - 是否有未跟踪的文件需要添加
   - 当前分支是否正确（应为 main）

### 步骤 2：暂存变更

1. 添加所有变更：
   ```bash
   git add -A
   ```
2. 或选择性添加：
   ```bash
   git add <具体文件路径>
   ```
3. 确认暂存内容：
   ```bash
   git status
   ```

### 步骤 3：提交变更

使用 Conventional Commits 格式：

```bash
git commit -m "type(scope): 简短描述

详细说明（可选）"
```

**类型说明**：
- `feat`: 新功能/新内容
- `fix`: 修复错误
- `docs`: 文档更新
- `refactor`: 重构/整理
- `chore`: 杂项维护

**示例**：
```bash
git commit -m "docs(工作流): 新增 GitHub 同步工作流文档"
git commit -m "feat(知识库): 添加项目管理知识体系"
git commit -m "fix(模板): 修复复盘模板格式问题"
```

### 步骤 4：拉取远程更新

1. 先拉取远程变更（避免冲突）：
   ```bash
   git pull origin main
   ```
2. 如有冲突，解决后重新提交：
   ```bash
   # 解决冲突文件
   git add <冲突文件>
   git commit -m "fix: 解决合并冲突"
   ```

### 步骤 5：推送到远程

1. 推送到 GitHub：
   ```bash
   git push origin main
   ```
2. 确认推送成功：
   ```bash
   git log --oneline -5
   ```

### 步骤 6：验证同步

1. 检查 GitHub 仓库页面确认更新
2. 验证关键文件内容正确

## 完整同步命令序列

```bash
# 进入目录
cd /e/工作需要/hermes-wiki

# 检查状态
git status

# 添加所有变更
git add -A

# 提交（替换为实际描述）
git commit -m "docs: 同步本周知识库更新"

# 拉取并推送
git pull origin main && git push origin main
```

## 模板路径

```
N/A（使用 Git 原生操作）
```

## 归档路径

```
GitHub 仓库：hermes-wiki
本地路径：E:\工作需要\hermes-wiki
```

## 注意事项

- **提交频率**：小批量多次提交优于大批量少次提交
- **提交信息**：遵循 Conventional Commits，便于生成 changelog
- **冲突处理**：推送前先拉取，及时解决冲突
- **敏感信息**：确保不提交密码、密钥等敏感数据（检查 .gitignore）
- **大文件**：避免提交大型二进制文件，使用 Git LFS 如有需要
- **分支策略**：主分支保持稳定，实验性内容在特性分支进行
- **备份意识**：GitHub 是备份之一，重要内容建议多重备份
