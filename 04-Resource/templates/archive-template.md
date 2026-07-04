---
title: "{{date:YYYY-MM-DD}} {{session_title}}"
created: {{date:YYYY-MM-DD}}T{{time:HH:mm}}
updated: {{date:YYYY-MM-DD}}T{{time:HH:mm}}
type: archive
session: "{{session_title}}"
last_archived: {{date:YYYY-MM-DD}}T{{time:HH:mm}}
---

# {{date:YYYY-MM-DD}} {{session_title}}

## 归档规则

- 每个 Hermes 会话 = 一个独立归档文件
- 文件名：`YYYY-MM-DD 会话标题.md`
- 通过 `last_archived` 时间戳去重，只归档新内容
- 格式：问题 → 解决方案 → 解决效果
- 每条带时间戳，按时间排序
- 子会话 ≤500 字

## 归档 1: [子话题]

**问题**: 
**方案**: 
**效果**: 
**时间**: {{date:YYYY-MM-DD}} {{time:HH:mm}}

---
> 更新: {{date:YYYY-MM-DD}}T{{time:HH:mm}}
