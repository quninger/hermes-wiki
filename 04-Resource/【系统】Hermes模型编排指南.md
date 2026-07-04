# Hermes Agent 模型编排指南

> **文档用途**：指导其他 Agent 实例建立模型编排系统
> **核心目标**：在输出质量不变的前提下减少付费——简单任务用免费模型，困难任务用付费模型
> **适用环境**：Hermes Agent（Nous Research）
> **最后更新**：2026-07-05

---

## 目录

1. [执行优先级](#1-执行优先级)
2. [可用模型清单](#2-可用模型清单)
3. [五种编排方案](#3-五种编排方案)
4. [难度评分系统](#4-难度评分系统)
5. [配置要求](#5-配置要求)
6. [delegate_task 规范](#6-delegate_task-规范)
7. [MoA 使用规范](#7-moa-使用规范)
8. [成本优化策略](#8-成本优化策略)
9. [常见陷阱](#9-常见陷阱)
10. [验证检查清单](#10-验证检查清单)

---

## 1. 执行优先级

收到用户任务后，**必须**按以下顺序决策，不得跳过：

1. 评估任务难度（1-10分）
2. 选择编排方案（方案1-5）
3. 选择模型
4. 执行任务
5. 付费模型收口质量
6. 恢复会话默认模型

---

## 2. 可用模型清单

### 2.1 免费模型（7个）

| 模型名称 | Provider | Base URL | 能力 | 适用复杂度 | 建议任务 |
|:---------|:---------|:---------|:-----|:----------:|:---------|
| **GLM-4-flash** | glm (zai) | `open.bigmodel.cn/api/coding/paas/v4` | 文本生成/问答/总结 | 简单~中等 | ⭐子代理主力、检索、格式化 |
| **GLM-4.7** | glm (zai) | 同上 | 更高质量文本生成 | 中等 | 需要质量时的免费升级 |
| **GLM-4v-flash** | glm (zai) | 同上 | 视觉理解、图片分析 | 简单~中等 | 图片识别、OCR |
| **THUDM/GLM-4-9B-0414** | siliconflow | `api.siliconflow.cn/v1` | 中等能力、9B参数 | 简单~中等 | 子代理备选 |
| **THUDM/GLM-Z1-9B-0414** | siliconflow | 同上 | 推理增强、9B参数 | 简单~中等 | 逻辑推理 |
| **Qwen/Qwen3.5-4B** | siliconflow | 同上 | 极轻量、4B参数 | 简单 | 极端降级、简单分类 |
| **Qwen/Qwen2.5-7B-Instruct** | siliconflow | 同上 | 对话、7B参数 | 简单~中等 | 对话任务 |

### 2.2 付费模型（5个）

| 模型名称 | Provider | Base URL | 能力 | 适用复杂度 | 建议任务 |
|:---------|:---------|:---------|:-----|:----------:|:---------|
| **mimo-v2.5** | mimo (xiaomi) | `token-plan-cn.xiaomimimo.com/v1` | 复杂推理、长文理解 | 难~困难 | 主模型、MoA聚合 |
| **deepseek-v4-flash** | code (deepseek) | `api.deepseek.com` | 编码、技术分析 | 中等~难 | 编码/调试、技术分析 |
| **deepseek-v4-pro** | code (deepseek) | 同上 | 更强编码、架构设计 | 困难 | 复杂架构、多文件重构 |
| **GLM-5.1** | glm (zai) | `open.bigmodel.cn/api/coding/paas/v4` | 高质量推理 | 中等~难 | 付费 |
| **GLM-5.2** | glm (zai) | 同上 | 最新GLM，综合最强 | 中等~难 | 付费 |

### 2.3 外部工具（1个）

| 工具 | 用途 | 适用复杂度 |
|:-----|:-----|:----------:|
| **Cursor CLI** | 极困难编码任务 | 困难 |

---

## 3. 五种编排方案

### 方案1：直接执行（分数1-5）

**触发**：任务简单，预计≤5次工具调用

**执行**：主代理直接调用 terminal/file/web

**禁止**：delegate_task、MoA

**适用**：简单问答、文件读写、格式转换

### 方案2：并行批量（分数6-7/10）

**触发**：多个独立子任务，可并行

**执行**：

```python
delegate_task(tasks=[
    {"goal": "子任务A", "context": "...", "toolsets": ["web"]},
    {"goal": "子任务B", "context": "...", "toolsets": ["terminal","file"]},
])
# 所有子代理自动使用 delegation.model（glm-4-flash，免费）
```

**规则**：
- 所有子代理统一使用 glm-4-flash（免费）
- 禁止批量任务全部用 DeepSeek
- 父代理只读子代理摘要，禁止全文贴入

### 方案3：串行分步（分数7-9）

**触发**：步骤有依赖，需要前一步结果

**执行**：

```
Step1: delegate_task(glm-4-flash) → 收集/探索（免费）
Step2: 主代理读 Step1 摘要 → 决策后执行（付费模型）
```

**规则**：
- 收集/探索步骤 → glm-4-flash（免费）
- 实现/安全/架构步骤 → 主代理（付费）亲自做
- 每步完成再开下一步

### 方案4：MoA 多视角聚合（仅分析/评审）

**触发**：同一问题需要多模型视角后做决策

**执行**：

```bash
hermes chat --provider moa -m lightweight -q "任务" -Q  # GLM→DeepSeek
hermes chat --provider moa -m standard -q "任务" -Q   # GLM+DeepSeek→Mimo
hermes chat --provider moa -m deep -q "任务" -Q       # DeepSeek+Mimo→Mimo
```

**禁止**：批量文件修改、流水线、机械数据收集

**适用**：架构选型、安全评审、方案A/B对比

### 方案5：混合流水线（机械+推理）

**触发**：前半段机械、后半段需推理

**执行**：

```
execute_code（机械收集，零LLM）
    → delegate_task(glm-4-flash)（可选：初筛分类）
        → 主代理（付费）综合/写最终输出
```

**规则**：能写Python脚本的，必须 execute_code，禁止为循环/格式化开 delegate

---

## 4. 难度评分系统

### 4.1 评分维度（1-10分）

| 维度 | 低(1-3) | 中(4-7) | 高(8-10) |
|:-----|:--------|:--------|:---------|
| 工具调用次数 | ≤2 | 3-8 | >8或需并行 |
| 涉及文件数 | 0-1 | 2-5 | >5或跨模块 |
| 推理深度 | 事实/解释 | 多步探索 | 架构/安全/复杂bug |
| 可脚本化 | 是 | 部分 | 否 |
| 输出风险 | 低 | 中 | 高（生产代码） |

**综合分** = 各维度上限的加权直觉分；边界取更高分（宁可用付费，不可用免费砸质量）。

### 4.2 分数→路由（强制）

| 分数 | 方案 | 子任务模型 | 主模型 |
|:----:|:----:|:----------:|:------:|
| 1-3 | 1 | 不delegate | 主代理 |
| 4-5 | 1/5 | execute_code优先 | 主代理 |
| 6-7 | 2/3 | **glm-4-flash（免费）** | 主代理 |
| 8-9 | 3/4 | glm收集→deepseek实现 | 主代理 |
| 10 | 2+3 | 混合；必要Cursor CLI | 主代理 |

### 4.3 典型任务速查

| 用户意图 | 分数 | 方案 | 模型 |
|----------|:----:|:----:|:-----|
| 解释概念/短问答 | 1-2 | 1 | 主代理 |
| 读1个文件说明 | 2-3 | 1 | 主代理 |
| 批量重命名/JSON解析 | 3-4 | 5 | execute_code |
| 调研3个技术方案 | 6-7 | 2 | 3×glm并行→综合 |
| 修单个测试失败 | 5-6 | 1/3 | DeepSeek |
| 多文件refactor | 8-9 | 3 | glm探索→DeepSeek实现 |
| 架构/security评审 | 8-9 | 4 | MoA standard/deep |

---

## 5. 配置要求

### 5.1 必须配置（~/.hermes/config.yaml）

```yaml
model:
  provider: mimo          # 或你的主模型provider
  default: mimo-v2.5      # 或你的主模型

delegation:
  model: glm-4-flash      # ⭐ 所有子代理统一免费
  provider: zai
  max_concurrent_children: 3
  max_spawn_depth: 1

auxiliary:
  vision: { provider: zai, model: glm-4-flash }
  compression: { provider: zai, model: glm-4-flash }
  web_extract: { provider: zai, model: glm-4-flash }
  approval: { provider: zai, model: glm-4-flash }
  # ... 所有 auxiliary 全设 glm-4-flash

fallback_providers:
  - { provider: zai, model: glm-4-flash }
  - { provider: siliconflow, model: Qwen/Qwen3.5-4B }
  - { provider: siliconflow, model: THUDM/GLM-Z1-9B-0414 }
  - { provider: siliconflow, model: THUDM/GLM-4-9B-0414 }
```

### 5.2 必须配置的 API Keys（~/.hermes/.env）

```bash
GLM_API_KEY=你的智谱APIKey
SILICONFLOW_API_KEY=你的SiliconFlow APIKey
```

### 5.3 验证配置

```bash
hermes config show    # 检查配置
hermes moa list       # 检查MoA presets
```

---

## 6. delegate_task 规范

### 6.1 官方能力（已确认）

| 能力 | 支持 |
|:-----|:----:|
| 并行批量（最多3路） | ✅ |
| 工具集选择（toolsets） | ✅ |
| 每任务独立model | ❌（继承父模型） |
| 串行依赖（depends_on） | ❌（不存在） |
| DAG有向无环图 | ❌（不存在） |

### 6.2 所有子代理统一使用 delegation.model

通过 config.yaml 设置 `delegation.model: glm-4-flash`，所有 `delegate_task` 子代理自动使用免费模型。

### 6.3 context 必填项

每个 delegate_task 的 context **必须**包含：
- 项目绝对路径
- 技术栈与环境
- 相关文件路径
- 验收标准
- 禁止/约束

### 6.4 禁止项

- 禁止 leaf 子代理再 delegate（max_spawn_depth: 1）
- 禁止 1-2 次工具调用开 delegate
- 禁止 子代理长输出全文返回（只返回摘要+结论）

---

## 7. MoA 使用规范

### 7.1 MoA 是什么

MoA（Mixture of Agents）是专用并行合议封装：**同一问题→多模型并行→聚合输出**。

### 7.2 MoA 调用方式

```bash
hermes chat --provider moa -m lightweight -q "任务" -Q
hermes chat --provider moa -m standard -q "任务" -Q
hermes chat --provider moa -m deep -q "任务" -Q
```

### 7.3 MoA Presets

| Preset | 参考模型 | 聚合模型 | 用途 |
|:------:|:---------|:---------|:-----|
| lightweight | GLM-4-flash | DeepSeek | 快速对比 |
| standard | GLM + DeepSeek | Mimo | 标准决策 |
| deep | DeepSeek + Mimo | Mimo | 深度评审 |

### 7.4 MoA 禁止场景

- ❌ 批量文件修改
- ❌ 流水线任务
- ❌ 机械数据收集
- ❌ 简单问答

### 7.5 MoA 适用场景

- ✅ 架构选型
- ✅ 安全评审
- ✅ 方案A/B对比
- ✅ 风险清单

---

## 8. 成本优化策略

### 8.1 核心原则

**免费模型负责探索和副作用；付费模型负责编排、实现与最终结论。**

### 8.2 成本对比

| 场景 | 旧方案 | 新方案 | 省多少 |
|:-----|:------:|:------:|:------:|
| 并行调研3方案 | 3×mimo | 3×**glm** | ~100% |
| 串行搜索+分析 | 2×mimo | 1×**glm** + 1×mimo | ~50% |
| 所有auxiliary | auto→mimo | **glm** | ~100% |

### 8.3 质量门禁（输出前自检）

- [ ] 关键结论是否经过付费模型审核？
- [ ] 免费模型产出的代码是否已跑测试？
- [ ] 是否误把 MoA 用于流水线任务？
- [ ] 会话模型是否已恢复？

若免费层结果不确定，必须升级：父代理亲自读关键文件或重跑 delegate(deepseek)。

---

## 9. 常见陷阱

| 陷阱 | 后果 | 避免方法 |
|:-----|:-----|:---------|
| 用MoA做流水线 | 昂贵且错误 | MoA仅用于多视角分析 |
| 所有子代理用DeepSeek | 浪费付费tokens | 设delegation.model=glm |
| 跳过难度评分 | 过度委派或质量不足 | 强制1-10分评分 |
| 子代理长输出全文返回 | 上下文爆炸 | 只返回摘要+结论 |
| 为1-2次工具调用开delegate | 浪费资源 | 直接执行 |
| 不恢复会话模型 | 后续任务误走MoA | 任务结束后恢复 |

---

## 10. 验证检查清单

每个任务结束时，确认：

- [ ] 已评估难度分数并选择对应方案
- [ ] 简单/中等子任务使用 glm，未滥用 DeepSeek
- [ ] delegate_task 均含完整 context
- [ ] 子 Agent 输出已压缩为摘要
- [ ] 关键结论由付费模型收口
- [ ] MoA 仅用于多视角分析，且已恢复会话模型
- [ ] 未为机械任务开 delegate 或 MoA

---

## 附录 A：一句话执行原则

**免费模型（GLM / SiliconFlow）负责探索和副作用；付费模型（MiMo / DeepSeek）负责编排、实现与最终结论；MoA 只做多视角分析，不做流水线。**

## 附录 B：官方文档引用

- [Delegation 基础文档](https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation)
- [委托与并行工作指南](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/delegation-patterns)
- [MoA 功能文档](https://hermes-agent.nousresearch.com/docs/user-guide/features/mixture-of-agents)
- [Fallback Providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers)

## 附录 C：关键发现（本次会话验证）

| 发现 | 验证方式 | 影响 |
|:-----|:---------|:-----|
| delegate_task 不支持per-task model | 官方文档+实测 | 通过config全局设delegation.model |
| delegate_task 不支持depends_on | 官方文档+实测 | 主代理多次调度实现串行 |
| MoA不能做流水线 | 官方文档 | MoA仅用于同一问题多模型聚合 |
| SiliconFlow API key需独立申请 | 实测 | config中需正确配置 |
| GLM-5.x/5v-turbo非免费 | 实测确认 | 从免费清单移除 |
| `hermes chat --provider moa` 可用 | 实测确认 | MoA通过terminal调用 |
| `hermes chat --model` 可切换模型 | 实测确认 | 临时切换模型用CLI |

---

> **文档版本**：1.0
> **最后更新**：2026-07-05
> **维护者**：Hermes Agent @ Nous Research
