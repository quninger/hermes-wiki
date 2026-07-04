# Hermes Agent 模型配置完整清单

> **文档用途**：完整记录所有可用模型的配置信息
> **最后更新**：2026-07-05

---

## 1. 模型清单

### 1.1 免费模型（7个）

| # | 模型名称 | Provider | Base URL | API Key | 上下文 | 功能 | 适用难度 | 使用任务 |
|:-:|:---------|:---------|:---------|:--------|:------:|:-----|:--------:|:---------|
| 1 | **GLM-4-flash** | glm (zai) | `https://open.bigmodel.cn/api/coding/paas/v4` | `f77552ac855d40a296ebc7578492a518.rXQyKe6w1XOctQ1x` | 128k | 文本生成/问答/总结 | 简单~中等 | ⭐子代理主力、检索、格式化、轻量编码 |
| 2 | **GLM-4.7** | glm (zai) | `https://open.bigmodel.cn/api/coding/paas/v4` | `f77552ac855d40a296ebc7578492a518.rXQyKe6w1XOctQ1x` | 128k | 更高质量文本生成 | 中等 | 需要质量时的免费升级 |
| 3 | **GLM-4v-flash** | glm (zai) | `https://open.bigmodel.cn/api/coding/paas/v4` | `f77552ac855d40a296ebc7578492a518.rXQyKe6w1XOctQ1x` | 128k | 视觉理解、图片分析 | 简单~中等 | 图片识别、OCR |
| 4 | **THUDM/GLM-4-9B-0414** | siliconflow | `https://api.siliconflow.cn/v1` | `sk-tyrfnlppaukeznkcpspsfwxilcejsuwgzbkjagybbcuubcjq` | 32k | 中等能力、9B参数 | 简单~中等 | 子代理备选 |
| 5 | **THUDM/GLM-Z1-9B-0414** | siliconflow | `https://api.siliconflow.cn/v1` | `sk-tyrfnlppaukeznkcpspsfwxilcejsuwgzbkjagybbcuubcjq` | 32k | 推理增强、9B参数 | 简单~中等 | 逻辑推理 |
| 6 | **Qwen/Qwen3.5-4B** | siliconflow | `https://api.siliconflow.cn/v1` | `sk-tyrfnlppaukeznkcpspsfwxilcejsuwgzbkjagybbcuubcjq` | 100k | 极轻量、4B参数 | 简单 | 极端降级、简单分类 |
| 7 | **Qwen/Qwen2.5-7B-Instruct** | siliconflow | `https://api.siliconflow.cn/v1` | `sk-tyrfnlppaukeznkcpspsfwxilcejsuwgzbkjagybbcuubcjq` | — | 对话、7B参数 | 简单~中等 | 对话任务 |

### 1.2 付费模型（5个）

| # | 模型名称 | Provider | Base URL | API Key | 上下文 | 功能 | 适用难度 | 使用任务 |
|:-:|:---------|:---------|:---------|:--------|:------:|:-----|:--------:|:---------|
| 8 | **mimo-v2.5** | mimo (xiaomi) | `https://token-plan-cn.xiaomimimo.com/v1` | `tp-cywplbhcrezqum4gtgug6ntwoletuxn8v5r4nn2f573kjh7f` | 200k | 复杂推理、长文理解 | 难~困难 | 主模型、MoA聚合、最终结论 |
| 9 | **deepseek-v4-flash** | code (deepseek) | `https://api.deepseek.com` | `sk-86e05ef1d3024c95816e3958ba59db7e` | 1M | 编码、技术分析 | 中等~难 | 编码/调试、技术分析 |
| 10 | **deepseek-v4-pro** | code (deepseek) | `https://api.deepseek.com` | `sk-86e05ef1d3024c95816e3958ba59db7e` | 1M | 更强编码、架构设计 | 困难 | 复杂架构、多文件重构 |
| 11 | **GLM-5.1** | glm (zai) | `https://open.bigmodel.cn/api/coding/paas/v4` | `f77552ac855d40a296ebc7578492a518.rXQyKe6w1XOctQ1x` | 128k | 高质量推理 | 中等~难 | 付费 |
| 12 | **GLM-5.2** | glm (zai) | `https://open.bigmodel.cn/api/coding/paas/v4` | `f77552ac855d40a296ebc7578492a518.rXQyKe6w1XOctQ1x` | 128k | 最新GLM，综合最强 | 中等~难 | 付费 |

---

## 2. Provider 配置

### 2.1 mimo（小米）

| 配置项 | 值 |
|:-------|:---|
| Provider 名称 | `mimo` |
| Base URL | `https://token-plan-cn.xiaomimimo.com/v1` |
| API Key | `tp-cywplbhcrezqum4gtgug6ntwoletuxn8v5r4nn2f573kjh7f` |
| API Mode | `chat_completions` |
| 模型列表 | `mimo-v2.5` |

### 2.2 code（DeepSeek）

| 配置项 | 值 |
|:-------|:---|
| Provider 名称 | `code` |
| Base URL | `https://api.deepseek.com` |
| API Key | `sk-86e05ef1d3024c95816e3958ba59db7e` |
| API Mode | `chat_completions` |
| 模型列表 | `deepseek-v4-flash`, `deepseek-v4-pro` |

### 2.3 glm（智谱）

| 配置项 | 值 |
|:-------|:---|
| Provider 名称 | `glm` |
| Base URL | `https://open.bigmodel.cn/api/coding/paas/v4` |
| API Key | `f77552ac855d40a296ebc7578492a518.rXQyKe6w1XOctQ1x` |
| API Mode | `chat_completions` |
| 模型列表 | `glm-4-flash`, `glm-4.7`, `glm-4v-flash`, `glm-5.1`, `glm-5.2`, `glm-5v-turbo` |

### 2.4 siliconflow（硅基流动）

| 配置项 | 值 |
|:-------|:---|
| Provider 名称 | `siliconflow` |
| Base URL | `https://api.siliconflow.cn/v1` |
| API Key | `sk-tyrfnlppaukeznkcpspsfwxilcejsuwgzbkjagybbcuubcjq` |
| API Mode | `chat_completions` |
| 模型列表 | `Qwen/Qwen3.5-4B`, `THUDM/GLM-4-9B-0414`, `THUDM/GLM-Z1-9B-0414` |

---

## 3. 系统配置

### 3.1 主模型

| 配置项 | 值 |
|:-------|:---|
| Provider | `mimo` |
| Default Model | `mimo-v2.5` |
| Base URL | `https://token-plan-cn.xiaomimimo.com/v1` |

### 3.2 Delegation（委派）

| 配置项 | 值 | 说明 |
|:-------|:---|:-----|
| model | `glm-4-flash` | 所有子代理统一免费 |
| provider | `zai` | |
| max_concurrent_children | `3` | 最多3路并行 |
| max_spawn_depth | `1` | 禁止嵌套委派 |

### 3.3 Fallback（降级链）

| 优先级 | Provider | Model |
|:------:|:---------|:------|
| 1 | zai | glm-4-flash |
| 2 | siliconflow | Qwen/Qwen3.5-4B |
| 3 | siliconflow | THUDM/GLM-Z1-9B-0414 |
| 4 | siliconflow | THUDM/GLM-4-9B-0414 |

### 3.4 Auxiliary（辅助工具）

| 工具 | Provider | Model |
|:-----|:---------|:------|
| approval | zai | glm-4-flash |
| compression | zai | glm-4-flash |
| curator | zai | glm-4-flash |
| kanban_decomposer | zai | glm-4-flash |
| mcp | zai | glm-4-flash |
| profile_describer | zai | glm-4-flash |
| skills_hub | zai | glm-4-flash |
| title_generation | zai | glm-4-flash |
| triage_specifier | zai | glm-4-flash |
| vision | zai | glm-4-flash |
| web_extract | zai | glm-4-flash |

### 3.5 MoA Presets

| Preset | 参考模型 | 聚合模型 | 用途 |
|:------:|:---------|:---------|:-----|
| lightweight | glm-4-flash | deepseek-v4-flash | 快速对比 |
| standard | glm-4-flash + deepseek-v4-flash | mimo-v2.5-pro | 标准决策 |
| deep | deepseek-v4-flash + mimo-v2.5-pro | mimo-v2.5-pro | 深度评审 |

---

## 4. 环境变量（~/.hermes/.env）

| 变量 | 值 |
|:-----|:---|
| `WIKI_PATH` | `E:\工作需要\hermes-wiki` |
| `CAMOFOX_URL` | `http://localhost:9377` |
| `API_SERVER_ENABLED` | `true` |
| `API_SERVER_PORT` | `8642` |
| `API_SERVER_HOST` | `127.0.0.1` |
| `API_SERVER_KEY` | `hermes-local-dev-key-change-me` |
| `XIAOMI_API_KEY` | `tp-cywplbhcrezqum4gtgug6ntwoletuxn8v5r4nn2f573kjh7f` |
| `GLM_API_KEY` | `f77552ac855d40a296ebc7578492a518.rXQyKe6w1XOctQ1x` |
| `OBSIDIAN_VAULT_PATH` | `E:\工作需要\hermes-wiki` |

---

## 5. 调用示例

### 5.1 GLM 模型（免费）

```bash
curl -X POST "https://open.bigmodel.cn/api/coding/paas/v4/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer f77552ac855d40a296ebc7578492a518.rXQyKe6w1XOctQ1x" \
  -d '{"model":"glm-4-flash","messages":[{"role":"user","content":"hi"}],"max_tokens":10}'
```

### 5.2 SiliconFlow 模型（免费）

```bash
curl -X POST "https://api.siliconflow.cn/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-tyrfnlppaukeznkcpspsfwxilcejsuwgzbkjagybbcuubcjq" \
  -d '{"model":"THUDM/GLM-4-9B-0414","messages":[{"role":"user","content":"hi"}],"max_tokens":10}'
```

### 5.3 Hermes CLI

```bash
# GLM
hermes chat --model glm-4-flash -q "任务" -Q

# SiliconFlow
hermes chat --provider siliconflow --model "THUDM/GLM-4-9B-0414" -q "任务" -Q

# MoA
hermes chat --provider moa -m lightweight -q "任务" -Q
hermes chat --provider moa -m standard -q "任务" -Q
hermes chat --provider moa -m deep -q "任务" -Q
```

---

> **文档版本**：1.0
> **最后更新**：2026-07-05
