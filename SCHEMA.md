# Wiki Schema

## Domain
AI Agent / 前端工程 Agent 方向 — 框架、模型、架构、最佳实践、求职面经

## Conventions
- 文件名: 小写英文 + 连字符 (e.g. `langgraph-agent.md`)
- 每页用 YAML frontmatter
- 使用 `[[wikilinks]]` 互链（每页至少 2 个出链）
- 更新页面时 bump `updated` 日期
- 新页面必须加入 `index.md`
- 每次操作追加到 `log.md`

## Frontmatter
```yaml
---
title: 页面标题
created: 2026-06-14
updated: 2026-06-14
type: entity | concept | comparison | query | summary
tags: [标签列表]
sources: [raw/articles/来源文件名.md]
---
```

## Tag Taxonomy
- 框架: langchain, langgraph, crewai, autogen, hermes
- 模型: gpt, claude, deepseek, qwen, llama
- 技术: rag, memory, tool-use, streaming, websocket
- 工程: deploy, eval, guardrail, ci-cd
- 求职: interview, resume, project, salary

## Entity Pages
一人/一公司/一模型一页，包含：概述、关键事实、关系、来源

## Concept Pages
一个概念一页，包含：定义、现状、开放问题、相关概念

## Comparison Pages
对比分析，表格优先，含结论和来源

## Update Policy
新信息冲突时注明双方观点 + 日期，标记 `contradictions: [page]`
