---
title: "【系统】Hermes Agent 模型编排建立方案"
created: 2026-07-04
updated: 2026-07-04
type: concept
tags: [agent, model-orchestration, moa, delegate, setup, 系统级]
workflow: WF-03
archive: true
github: allow
privacy: false
---

# Hermes Agent 模型编排建立方案

> **文档用途**：指导 Agent 在全新系统中建立模型编排方案
> **适用对象**：所有 Hermes Agent 实例
> **核心目标**：实现多模型分工协作，发挥各模型特长，降低成本

---

# 第一章：理解模型编排

## 1.1 什么是模型编排

模型编排是指根据任务特性，选择最合适的模型或模型组合来执行任务，而不是所有任务都用同一个模型。

## 1.2 为什么要模型编排

| 问题 | 不编排的后果 | 编排后的效果 |
|:-----|:-------------|:-------------|
| 轻量任务用大模型 | 浪费成本 | GLM 免费处理 |
| 复杂任务用小模型 | 质量差 | Mimo 深度处理 |
| 需要多视角分析 | 单一视角 | MoA 多模型聚合 |
| 大量并行任务 | 串行慢 | delegate 并行加速 |

## 1.3 三层编排架构

```
第一层：主模型规划
    │ 收到任务 → 分析复杂度 → 决定编排策略
    ▼
第二层：编排选择
    │
    ├── MoA（多模型聚合）
    │   多个不同模型各自分析 → 聚合模型合并
    │
    ├── delegate（同模型并行）
    │   同一模型多个分身 → 各做不同子任务
    │
    └── 混合模式
        轻量模型并行预处理 → MoA 深度聚合
    ▼
第三层：执行 + 聚合 + 归档
```

---

# 第二章：模型能力画像

在建立编排方案前，必须先理解每个模型的能力边界。

## 2.1 模型能力矩阵

| 模型 | 擅长 | 不擅长 | 成本 | 推荐用途 |
|:----:|:-----|:-------|:----:|:---------|
| **GLM** | 文本总结、信息提取、格式转换、轻量压缩 | 复杂推理、长文分析 | 免费 | 轻量工兵 |
| **DeepSeek** | 编码、技术分析、中等推理、代码审查 | 创意写作 | 低 | 技术专家 |
| **Mimo** | 通用对话、复杂推理、长文理解、架构设计 | — | 中 | 总指挥 |

## 2.2 模型选择决策树

```
任务到来
├── 总结/提取/压缩/格式化？ → GLM（免费）
├── 编码/调试/技术分析？ → DeepSeek
├── 复杂推理/架构设计/长文理解？ → Mimo
├── 需要多视角？ → MoA（多模型聚合）
├── 需要并行？ → delegate（同模型并行）
└── 需要预处理+深度分析？ → 混合模式
```

---

# 第三章：建立 MoA 配置

## 3.1 什么是 MoA

MoA（Mixture of Agents）是 Hermes 内置的多模型聚合系统：

```
同一个 prompt
    │
    ├──→ 参考模型1（如 GLM）
    ├──→ 参考模型2（如 DeepSeek）
    │         （并行执行）
    ▼
聚合模型（如 Mimo）
    │
    ▼
最终输出（整合所有参考模型的视角）
```

## 3.2 配置 MoA Presets

在 `config.yaml` 中添加 `moa:` 配置：

```yaml
moa:
  default_preset: standard
  presets:
    # Preset 1: 轻量聚合
    # 用途：文本压缩、信息提取、快速总结
    # GLM 做参考（免费），DeepSeek 聚合
    lightweight:
      reference_models:
        - provider: glm
          model: glm-4-flash
      aggregator:
        provider: code
        model: deepseek-v4-flash
      max_tokens: 2048
      reference_max_tokens: 500
      fanout: per_iteration

    # Preset 2: 标准聚合
    # 用途：技术调研、多维度分析、方案对比
    # GLM + DeepSeek 做参考，Mimo 聚合
    standard:
      reference_models:
        - provider: glm
          model: glm-4-flash
        - provider: code
          model: deepseek-v4-flash
      aggregator:
        provider: xiaomi
        model: mimo-v2.5-pro
      max_tokens: 4096
      reference_max_tokens: 800
      fanout: per_iteration

    # Preset 3: 深度聚合
    # 用途：复杂推理、架构设计、长文档分析
    # DeepSeek + Mimo 做参考，Mimo 聚合
    deep:
      reference_models:
        - provider: code
          model: deepseek-v4-flash
        - provider: xiaomi
          model: mimo-v2.5-pro
      aggregator:
        provider: xiaomi
        model: mimo-v2.5-pro
      max_tokens: 8192
      reference_max_tokens: 1500
      fanout: per_iteration
```

## 3.3 使用 MoA

### 方式一：单次执行

```
/moa lightweight 请总结以下文本的要点：...
/moa standard 对比 Vue3 和 React 的优缺点：...
/moa deep 分析这个架构方案的可行性：...
```

### 方式二：会话级切换

从模型选择器中选择 "Mixture of Agents" 提供商，选择对应 preset。

### 方式三：代码中调用

```python
# 通过 CLI 命令
terminal("hermes moa '你的prompt'")
```

---

# 第四章：建立 delegate_task 模式

## 4.1 什么是 delegate_task

delegate_task 是 Hermes 的子代理委派系统，用于将任务拆分给多个并行执行的子代理。

```
主代理
    │
    ├──→ 子代理1（处理子任务A）
    ├──→ 子代理2（处理子任务B）
    ├──→ 子代理3（处理子任务C）
    │         （并行执行）
    ▼
主代理汇总结果
```

## 4.2 delegate_task 限制

| 限制 | 说明 |
|:-----|:-----|
| 模型选择 | ❌ 不能指定不同模型，子代理继承父模型 |
| 最大并行 | 3 个子代理 |
| 嵌套深度 | 1 层（子代理不能再委派） |
| 结果返回 | 异步，结果作为新消息进入对话 |

## 4.3 delegate_task 使用模式

### 模式一：批量并行

```javascript
delegate_task({
  tasks: [
    { goal: "分析任务A的方案", role: "leaf" },
    { goal: "分析任务B的方案", role: "leaf" },
    { goal: "分析任务C的方案", role: "leaf" }
  ]
})
// 3个子代理同时执行，结果一起返回
```

### 模式二：串行执行

```javascript
// 第一步：规划
delegate_task({ goal: "分析任务，输出执行计划", role: "leaf" })
// 等待结果返回...

// 第二步：执行（根据规划结果）
delegate_task({ goal: "按计划执行任务", role: "leaf" })
// 等待结果返回...

// 第三步：主代理汇总归档
```

### 模式三：Orchestrator 模式

```javascript
delegate_task({
  goal: "协调完成复杂任务",
  role: "orchestrator"
})
// Orchestrator 子代理可以自己再委派（受限于 max_spawn_depth）
```

---

# 第五章：建立混合模式

## 5.1 什么是混合模式

混合模式结合 MoA 和 delegate_task 的优势：

- **delegate_task**：用轻量模型（GLM）并行预处理
- **MoA**：用多视角模型深度分析

## 5.2 混合模式流程

```
长文档/大项目
    │
    ▼
第一步（delegate 并行）：
    ├──→ GLM 子代理1：提取第1-3章摘要
    ├──→ GLM 子代理2：提取第4-6章摘要
    ├──→ GLM 子代理3：提取第7-9章摘要
    │         （轻量模型并行压缩）
    ▼
第二步（MoA 聚合）：
    所有摘要 → DeepSeek 深度分析 → Mimo 聚合输出
```

## 5.3 混合模式实现

```javascript
// 第一步：delegate 并行预处理（用 GLM）
// 注意：delegate_task 不能指定模型，需要主代理直接执行轻量任务
// 或者通过 MoA lightweight preset 处理

// 主代理直接执行轻量预处理
const summary1 = await extractSummary(doc1)  // GLM 或主代理
const summary2 = await extractSummary(doc2)
const summary3 = await extractSummary(doc3)

// 第二步：MoA 深度聚合
const finalResult = await moa("standard", `分析以下摘要并给出综合结论：\n${summary1}\n${summary2}\n${summary3}`)
```

---

# 第六章：建立编排决策逻辑

## 6.1 主模型编排决策树

主模型收到任务后，按以下逻辑决策：

```
任务到来
│
├── 第一层：任务分析
│   ├── 任务复杂度？（轻量/中等/复杂）
│   ├── 需要多视角？（是/否）
│   ├── 需要并行处理？（是/否）
│   ├── 需要预处理？（是/否）
│   └── 数据量大小？（小/中/大）
│
├── 第二层：编排选择
│   │
│   ├── 简单任务 → 主模型直接执行
│   │
│   ├── 需要多视角 → MoA
│   │   ├── 轻量分析 → MoA lightweight
│   │   ├── 标准分析 → MoA standard
│   │   └── 深度分析 → MoA deep
│   │
│   ├── 需要并行 → delegate_task
│   │   ├── 2个子任务 → delegate 2路
│   │   └── 3个子任务 → delegate 3路
│   │
│   └── 需要预处理+深度分析 → 混合模式
│       ├── 大文档 → GLM并行压缩 → MoA聚合
│       └── 多源信息 → GLM并行提取 → MoA综合
│
└── 第三层：执行 + 聚合 + 归档
```

## 6.2 编排决策表

| 任务特征 | 推荐编排 | 模型组合 | 示例 |
|:---------|:---------|:---------|:-----|
| 总结/提取/压缩 | 主模型直接 或 MoA lightweight | GLM → DeepSeek | 文本摘要、信息提取 |
| 编码/调试 | 主模型直接 | DeepSeek | bug修复、脚本开发 |
| 技术调研 | MoA standard | GLM+DeepSeek → Mimo | 框架对比、方案评估 |
| 多维度分析 | MoA standard | GLM+DeepSeek → Mimo | 产品评估、竞品分析 |
| 复杂推理 | MoA deep | DeepSeek+Mimo → Mimo | 架构设计、算法分析 |
| 批量文件处理 | delegate_task | DeepSeek ×3 | 多文件代码审查 |
| 大文档分析 | 混合模式 | GLM并行压缩 → MoA | 长报告分析 |
| 多源信息整合 | 混合模式 | GLM并行提取 → MoA | 多平台数据汇总 |

---

# 第七章：在 SOUL.md 中写入编排规则

将以下内容写入 Agent 的 SOUL.md（系统提示词）：

```markdown
# 模型编排规则（WF-12 · 三层架构）

## 三层编排架构

### 第一层：主模型规划
主模型收到任务 → 分析复杂度 → 决定编排策略（直接执行 / MoA / delegate / 混合）

### 第二层：编排选择
| 场景 | 选择 | 说明 |
|------|------|------|
| 需要多视角分析 | MoA | 多个不同模型各自分析，聚合模型合并 |
| 需要并行处理 | delegate_task | 同模型多个分身，各做不同子任务 |
| 需要预处理+深度分析 | 混合模式 | GLM并行压缩 → MoA深度聚合 |
| 简单任务 | 直接执行 | 不编排 |

### 第三层：执行 + 聚合 + 归档

## MoA Preset
- **lightweight**: GLM(参考) → DeepSeek(聚合) — 文本压缩、信息提取
- **standard**: GLM+DeepSeek(参考) → Mimo(聚合) — 技术调研、多维度分析
- **deep**: DeepSeek+Mimo(参考) → Mimo(聚合) — 复杂推理、架构设计

## 模型能力画像
| 模型 | 擅长 | 成本 |
|------|------|------|
| GLM | 总结、提取、压缩、格式化 | 免费 |
| DeepSeek | 编码、技术分析、中等推理 | 低 |
| Mimo | 通用对话、复杂推理、长文理解 | 中 |

## 降级链
mimo → deepseek → glm-4-flash(免费) → siliconflow(免费)

## 编码任务
- 🟢 普通 → deepseek（原生工具）
- 🔴 困难 → Cursor CLI（cursor-agent.cmd --print --force --trust）

> 详细模型编排方案见：04-Resource/工作流/WF-12-模型编排.md
```

---

# 第八章：验证编排方案

## 8.1 验证清单

| 测试项 | 预期 | 验证方法 |
|:-------|:-----|:---------|
| MoA lightweight 可用 | GLM 参考 + DeepSeek 聚合 | `/oa lightweight 测试prompt` |
| MoA standard 可用 | GLM+DeepSeek 参考 + Mimo 聚合 | `/moa standard 测试prompt` |
| MoA deep 可用 | DeepSeek+Mimo 参考 + Mimo 聚合 | `/moa deep 测试prompt` |
| delegate_task 并行 | 3个子代理同时执行 | delegate_task({tasks: [3个任务]}) |
| 混合模式可用 | GLM预处理 + MoA聚合 | 先提取再分析 |
| 降级链生效 | 模型失败自动切换 | 模拟模型不可用 |

## 8.2 测试用例

### 测试 1：轻量任务（MoA lightweight）

```
输入：请总结以下文本的要点：[长文本]
预期：GLM 提取要点 → DeepSeek 整理输出
验证：输出包含结构化要点
```

### 测试 2：技术调研（MoA standard）

```
输入：对比 Vue3 和 React 的优缺点
预期：GLM 快速对比 + DeepSeek 深度分析 → Mimo 综合
验证：输出包含多维度对比表格
```

### 测试 3：并行处理（delegate_task）

```
输入：同时分析3个代码文件的潜在问题
预期：3个子代理并行执行，结果一起返回
验证：3份分析报告同时到达
```

### 测试 4：混合模式

```
输入：分析这份100页报告的核心观点
预期：GLM 分段压缩 → MoA 深度分析
验证：输出包含压缩摘要 + 深度分析
```

---

# 第九章：维护与优化

## 9.1 定期评估

| 周期 | 检查项 | 动作 |
|:----:|:-------|:-----|
| 每周 | MoA 执行效果 | 对比单模型 vs MoA 质量 |
| 每月 | 模型成本 | 分析各模型 token 消耗 |
| 每季 | Preset 配置 | 根据使用情况调整 |

## 9.2 优化建议

1. **轻量任务优先用 GLM**：总结、提取、格式化等用 GLM 免费处理
2. **复杂任务用 MoA**：需要多视角时用 MoA，不要单模型硬撑
3. **并行任务用 delegate**：独立子任务用 delegate 并行，不要串行
4. **大文档用混合模式**：先 GLM 压缩，再 MoA 分析
5. **定期清理 Memory**：避免上下文膨胀影响编排效果

---

# 附录 A：config.yaml 完整配置示例

```yaml
model:
  base_url: https://token-plan-cn.xiaomimimo.com/v1
  default: mimo-v2.5-pro
  provider: xiaomi

providers:
  mimo:
    api_key: your-mimo-key
    base_url: https://token-plan-cn.xiaomimimo.com/v1
  code:
    api_key: your-deepseek-key
    base_url: https://api.deepseek.com/v1
  glm:
    api_key: your-glm-key
    base_url: https://open.bigmodel.cn/api/paas/v4

moa:
  default_preset: standard
  presets:
    lightweight:
      reference_models:
        - provider: glm
          model: glm-4-flash
      aggregator:
        provider: code
        model: deepseek-v4-flash
      max_tokens: 2048
      reference_max_tokens: 500
    standard:
      reference_models:
        - provider: glm
          model: glm-4-flash
        - provider: code
          model: deepseek-v4-flash
      aggregator:
        provider: xiaomi
        model: mimo-v2.5-pro
      max_tokens: 4096
      reference_max_tokens: 800
    deep:
      reference_models:
        - provider: code
          model: deepseek-v4-flash
        - provider: xiaomi
          model: mimo-v2.5-pro
      aggregator:
        provider: xiaomi
        model: mimo-v2.5-pro
      max_tokens: 8192
      reference_max_tokens: 1500

delegation:
  max_concurrent_children: 3
  max_spawn_depth: 1
  orchestrator_enabled: true
```

---

> **最后更新**: 2026-07-04
> **维护者**: Hermes Agent @ Nous Research
> **适用范围**: 所有 Hermes Agent 实例
