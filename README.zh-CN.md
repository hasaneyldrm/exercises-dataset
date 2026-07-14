[English](README.md) · **简体中文**

<div align="center">

# 💪 Exercises Dataset 动作训练数据集

<p>
  <img src="videos/0025-EIeI8Vf.gif" width="120" alt="杠铃卧推" />
  <img src="videos/0043-qXTaZnJ.gif" width="120" alt="杠铃全蹲" />
  <img src="videos/0032-ila4NZS.gif" width="120" alt="杠铃硬拉" />
  <img src="videos/0652-lBDjFxJ.gif" width="120" alt="正握引体向上" />
  <img src="videos/0294-NbVPDMW.gif" width="120" alt="哑铃肱二头肌弯举" />
  <img src="videos/0334-DsgkuIt.gif" width="120" alt="哑铃侧平举" />
</p>

**一套完整、开箱即用的动作训练数据集，包含 1,324 个动作。每个动作均提供 GIF 动画、180×180 缩略图、分类、身体部位、器械、目标肌肉、肌群等中英文字段，以及 9 种语言的分步训练说明（英语、西班牙语、意大利语、土耳其语、俄语、中文、印地语、波兰语和韩语）。**

[![动作数量](https://img.shields.io/badge/动作数量-1324-blue?style=flat-square)](data/exercises.json)
[![GIF 动画](https://img.shields.io/badge/GIF%20动画-1324-brightgreen?style=flat-square)](videos/)
[![缩略图](https://img.shields.io/badge/缩略图-1324-orange?style=flat-square)](images/)
[![说明语言](https://img.shields.io/badge/说明语言-9-green?style=flat-square)](#-概览)
[![移动应用](https://img.shields.io/badge/App-LogPress-111111?style=flat-square&logo=react)](https://github.com/hasaneyldrm/logpress-public)
[![许可](https://img.shields.io/badge/License-MIT%20%2B%20媒体条款-blue?style=flat-square)](LICENSE)

</div>

> **📱 为 [LogPress](https://github.com/hasaneyldrm/logpress-public) 应用提供数据支持**——LogPress 是一款 AI 辅助训练记录应用，本数据集是其动作数据层。开发健身应用时，可直接将本数据集接入后端。

---

## 📦 数据来源与内容

**本仓库提供：**

- 1,324 个动作，包含分类、身体部位、器械、目标肌肉和肌群数据
- 每个动作一个 GIF 动画和一张 180×180 缩略图（媒体文件 © [Gym visual](https://gymvisual.com/)，许可说明见[许可与使用](#-许可与使用)）
- 与原始英文字段并列的简体中文动作名和健身术语字段
- 9 种语言的分步说明（🇬🇧 英语、🇪🇸 西班牙语、🇮🇹 意大利语、🇹🇷 土耳其语、🇷🇺 俄语、🇨🇳 中文、🇮🇳 印地语、🇵🇱 波兰语、🇰🇷 韩语）
- 交互式动作浏览器（`index.html`）和开发接入指南（`setup.html`）

---

## 📋 目录

- [数据来源与内容](#-数据来源与内容)
- [概览](#-概览)
- [动作浏览器与开发接入](#-动作浏览器与开发接入)
- [文件结构](#-文件结构)
- [统计数据](#-统计数据)
- [数据结构](#-数据结构)
- [动作示例](#-动作示例)
- [使用示例](#-使用示例)
- [许可与使用](#-许可与使用)

---

## 🔍 概览

本数据集收录了 **1,324 个健身动作**，用于教育和研究。内容覆盖多种肌群、器械和动作分类，适合以下场景：

- 开发健身或训练计划应用
- 动作识别、动作推荐等机器学习项目
- 健康与运动研究
- 教学演示和产品原型

每条动作记录包含：

| 内容 | 说明 |
|---|---|
| 唯一 ID | 数字字符串标识，例如 `"0001"` |
| 动作名称 | 英文动作全名和简体中文动作名（`name`、`name_zh`） |
| 分类 | 身体部位分类及对应简体中文字段，当前与 `body_part` 相同 |
| 目标肌肉 | 主要目标肌肉及对应简体中文字段 |
| 肌群 | 协同肌群及对应简体中文字段 |
| 器械 | 所需器械；徒手动作的英文值为 `body weight` |
| 训练说明 | 每个动作的分步训练说明 |
| 可用语言 | 🇬🇧 英语 · 🇪🇸 西班牙语 · 🇮🇹 意大利语 · 🇹🇷 土耳其语 · 🇷🇺 俄语 · 🇨🇳 中文 · 🇮🇳 印地语 · 🇵🇱 波兰语 · 🇰🇷 韩语 |
| 媒体 | 每个动作包含 180×180 缩略图（`image`）和 GIF 动画（`gif_url`）；媒体 © Gym visual，详见[许可与使用](#-许可与使用) |

---

## 🖥️ 动作浏览器与开发接入

仓库包含两个无需服务器即可查看的 HTML 工具。

> **说明：** 动作浏览器会同时显示每个动作的 180×180 缩略图、GIF 动画、元数据和训练说明。

### `index.html`——动作浏览器

完全在客户端运行的动作浏览器，支持：

- 在全部 1,324 个动作中实时搜索
- 按分类、器械和目标肌肉筛选
- 无限滚动网格
- 默认简体中文界面，并可切换为英文；语言偏好会保存在浏览器中
- 使用中文或英文动作名和术语搜索
- 点击动作卡片查看完整详情，并可阅读英语、西班牙语、意大利语、土耳其语、俄语、中文、印地语、波兰语或韩语训练说明

### `setup.html`——开发接入指南

将数据集接入应用的分步指南：

1. **数据库设置**——提供 SQL Server、PostgreSQL、MySQL 和 SQLite 的 `CREATE TABLE` SQL；可完全在浏览器中生成包含 1,324 条 `INSERT` 语句的 `.sql` 文件。数据已嵌入指南，因此通过 `file://` 直接双击打开 `setup.html` 时也能生成文件。
2. **API 接入**——提供 **JavaScript、Python、C#、Java、PHP、Go 和 cURL** 客户端示例。输入 API 基础 URL 后，所有示例会实时更新。
3. **让大模型生成后端**——选择框架和数据库，将结构化提示词粘贴到 ChatGPT、Claude 或 Gemini，即可生成完整 REST API。支持 Express.js、FastAPI、ASP.NET Core、Spring Boot、Laravel 和 Gin。

---

## 📂 文件结构

```text
exercises-dataset/
├── data/
│   ├── exercises.json        # 完整数据集：1,324 条动作记录（JSON 数组）
│   └── exercises.schema.json # 描述每条记录的 JSON Schema（2020-12）
├── scripts/
│   ├── refine-zh-data.mjs    # 检查并规范简体中文字段
│   └── sync-embedded-data.mjs # 同步 HTML 内嵌数据
├── images/                   # 1,324 张 180×180 缩略图（© Gym visual）
├── videos/                   # 1,324 个 180×180 GIF 动画（© Gym visual）
├── index.html                # 交互式动作浏览器（纯客户端，无需服务器）
├── setup.html                # 开发接入指南（数据库导入和 API 接入）
├── NOTICE.md                 # 英文媒体署名与许可条款
├── NOTICE.zh-CN.md           # NOTICE 简体中文参考译文
├── README.zh-CN.md           # 本文件
└── README.md                 # 英文说明
```

### 关键文件

- **`data/exercises.json`**——主数据文件，由 1,324 个动作对象组成。`image` 和 `gif_url` 指向本地 180×180 资源；每条记录包含 `attribution` 媒体署名，`media_id` 保存原始媒体引用 ID。
- **`data/exercises.schema.json`**——使用 [JSON Schema](https://json-schema.org/) Draft 2020-12 正式描述每个字段、类型和约束，可用于验证本数据集或自行补充的数据。
- **`scripts/refine-zh-data.mjs`**——检查全部交付中文字段；加 `--write` 可应用已审核的术语修正，不加参数则只读检查。
- **`scripts/sync-embedded-data.mjs`**——将 `data/exercises.json` 同步嵌入 `index.html` 和 `setup.html`；加 `--check` 可只读确认三份数据完全一致。
- **`images/`、`videos/`**——180×180 缩略图和 GIF 动画（© [Gym visual](https://gymvisual.com/)，经许可使用）。
- **`index.html`**——独立动作浏览器，可直接在现代浏览器中打开。
- **`setup.html`**——数据库设置、API 接入和大模型辅助生成后端的开发指南。
- **`LICENSE`、`NOTICE.md`**——代码和数据采用 MIT License；Gym visual 媒体另受媒体条款约束。中文 [`NOTICE.zh-CN.md`](NOTICE.zh-CN.md) 仅供参考，以英文文件为准。

---

## 📊 统计数据

| 指标 | 数量 |
|---|---:|
| 动作总数 | **1,324** |
| 训练说明语言 | **9** |

### 按身体部位统计

| 身体部位 | 动作数量 |
|---|---:|
| 上臂 | 292 |
| 大腿 | 227 |
| 背部 | 203 |
| 腰腹部 | 169 |
| 胸部 | 163 |
| 肩部 | 143 |
| 小腿 | 59 |
| 前臂 | 37 |
| 有氧 | 29 |
| 颈部 | 2 |

### 按器械统计

| 器械 | 动作数量 |
|---|---:|
| 自重 | 325 |
| 哑铃 | 294 |
| 绳索拉力器 | 157 |
| 杠铃 | 154 |
| 固定器械 | 81 |
| 弹力带 | 54 |
| 史密斯机 | 48 |
| 壶铃 | 41 |
| 负重 | 36 |
| 健身球 | 28 |
| EZ 曲杆 | 23 |
| 其他 | 83 |

> **说明：** 约 25% 的动作不需要任何器械，非常适合居家训练应用。

---

## 🗂️ 数据结构

`data/exercises.json` 中的每条记录都遵循以下结构。仓库也提供可供程序验证的 [JSON Schema](data/exercises.schema.json)。

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | `string` | 唯一数字字符串标识，例如 `"0001"` |
| `name` | `string` | 英文动作全名，例如 `"3/4 sit-up"` |
| `name_zh` | `string` | 简体中文动作名 |
| `category` | `string` | 英文身体部位分类，例如 `"upper arms"`、`"chest"`、`"back"` |
| `category_zh` | `string` | 简体中文分类 |
| `body_part` | `string` | 英文目标身体部位，当前与 `category` 相同 |
| `body_part_zh` | `string` | 简体中文身体部位 |
| `equipment` | `string` | 英文器械名，例如 `"dumbbell"`、`"body weight"` |
| `equipment_zh` | `string` | 简体中文器械名 |
| `instructions.en` | `string` | 英语完整训练说明 |
| `instructions.es` | `string` | 西班牙语完整训练说明 |
| `instructions.it` | `string` | 意大利语完整训练说明 |
| `instructions.tr` | `string` | 土耳其语完整训练说明 |
| `instructions.ru` | `string` | 俄语完整训练说明 |
| `instructions.zh` | `string` | 简体中文完整训练说明 |
| `instructions.hi` | `string` | 印地语完整训练说明 |
| `instructions.pl` | `string` | 波兰语完整训练说明 |
| `instructions.ko` | `string` | 韩语完整训练说明 |
| `instruction_steps.<lang>` | `array[string]` | 按顺序拆分的各语言训练步骤；语言代码为 `en`、`es`、`it`、`tr`、`ru`、`zh`、`hi`、`pl`、`ko` |
| `muscle_group` | `string` | 英文主要协同肌群 |
| `muscle_group_zh` | `string` | 简体中文主要协同肌群 |
| `secondary_muscles` | `array[string]` | 英文辅助肌群数组 |
| `secondary_muscles_zh` | `array[string]` | 简体中文辅助肌群数组 |
| `target` | `string` | 英文主要目标肌肉，例如 `"biceps"`、`"pectoralis major"` |
| `target_zh` | `string` | 简体中文主要目标肌肉 |
| `media_id` | `string` | 原始媒体引用 ID，例如 `"2gPfomN"` |
| `image` | `string` | 180×180 缩略图路径，例如 `"images/0001-2gPfomN.jpg"` |
| `gif_url` | `string` | 180×180 GIF 动画路径，例如 `"videos/0001-2gPfomN.gif"` |
| `attribution` | `string` | 媒体版权声明：`"© Gym visual — https://gymvisual.com/"` |
| `created_at` | `string` | 记录创建时间，采用 ISO 8601 格式 |

### 示例记录

```json
{
  "id": "0001",
  "name": "3/4 sit-up",
  "name_zh": "3/4仰卧起坐",
  "category": "waist",
  "category_zh": "腰腹部",
  "body_part": "waist",
  "body_part_zh": "腰腹部",
  "equipment": "body weight",
  "equipment_zh": "自重",
  "instructions": {
    "en": "Lie flat on your back with your knees bent and feet flat on the ground. ...",
    "es": "Túmbate sobre tu espalda con las rodillas flexionadas y los pies apoyados en el suelo. ...",
    "it": "Sdraiati sulla schiena con le ginocchia piegate e i piedi appoggiati a terra. ...",
    "tr": "Sırt üstü yatın, dizlerinizi bükün ve ayaklarınızı yere düz koyun. ...",
    "ru": "Лягте на спину, согните колени и поставьте ступни на землю. ...",
    "zh": "平躺，膝盖弯曲，双脚平放在地上。...",
    "hi": "अपने घुटनों को मोड़कर और पैरों को ज़मीन पर सपाट रखते हुए अपनी पीठ के बल लेट जाएँ।...",
    "pl": "Połóż się płasko na plecach, ugnij kolana i oprzyj stopy płasko na pod ...",
    "ko": "등을 바닥에 누워 무릎을 구부리고 발을 바닥에 붙입니다. ..."
  },
  "muscle_group": "hip flexors",
  "muscle_group_zh": "髋屈肌",
  "secondary_muscles": ["hip flexors", "lower back"],
  "secondary_muscles_zh": ["髋屈肌", "下背肌群"],
  "target": "abs",
  "target_zh": "腹肌",
  "media_id": "2gPfomN",
  "image": "images/0001-2gPfomN.jpg",
  "gif_url": "videos/0001-2gPfomN.gif",
  "attribution": "© Gym visual — https://gymvisual.com/",
  "created_at": "2026-03-18T12:31:32.854798+00:00"
}
```

---

## 🎬 动作示例

> 每个示例都包含 180×180 缩略图（`image`）和 GIF 动画（`gif_url`），媒体 © [Gym visual](https://gymvisual.com/)。

### 1——杠铃卧推 · 胸部

<img src="videos/0025-EIeI8Vf.gif" width="150" align="right" alt="杠铃卧推" />

> **器械：** 杠铃 · **目标：** 胸肌 · **辅助：** 肱三头肌、肩部肌群 · **媒体 ID：** `EIeI8Vf`

杠铃卧推是胸部训练的基础动作，也是力量举三大项之一。仰卧在训练凳上，将负重杠铃降至胸部后有力推起，可同时调动胸肌、肱三头肌和三角肌前束，是提升上肢推力与胸部肌肉量的重要动作。

**动作要点：** 出杠前收紧并下沉肩胛骨；双脚平放在地面，下背部保持自然弧度，采用约与肩同宽的握距；受控地将杠铃降到胸部中段，再通过脚掌稳定发力向上推起。

### 2——杠铃硬拉 · 大腿

<img src="videos/0032-ila4NZS.gif" width="150" align="right" alt="杠铃硬拉" />

> **器械：** 杠铃 · **目标：** 臀肌 · **辅助：** 腘绳肌、下背肌群 · **媒体 ID：** `ila4NZS`

杠铃硬拉是一项经典的全身力量训练动作，重点锻炼臀肌、腘绳肌和下背部等后侧链肌群，同时要求上背部、斜方肌和握力共同参与。正确的脊柱排列和核心支撑对表现与安全都很重要。

**动作要点：** 让杠铃位于足中部上方，以髋关节折叠下沉，双手握在双腿外侧；收紧核心，整个提拉过程让杠铃贴近小腿；脚掌向下蹬地，顶端夹紧臀部并完全伸髋。

### 3——杠铃全蹲 · 大腿

<img src="videos/0043-qXTaZnJ.gif" width="150" align="right" alt="杠铃全蹲" />

> **器械：** 杠铃 · **目标：** 臀肌 · **辅助：** 股四头肌、腘绳肌、小腿肌群、核心肌群 · **媒体 ID：** `qXTaZnJ`

杠铃全蹲要求整个下肢和核心协调发力。蹲至大腿低于平行位置，与浅蹲相比可更充分地调动臀肌和腘绳肌，是许多力量与增肌计划的基础动作。

**动作要点：** 杠铃可置于斜方肌上部（高杠）或三角肌后束（低杠）；下蹲前收紧核心，膝盖沿脚尖方向打开，以髋部下坐，直到大腿低于与地面平行的位置；整个脚掌稳定发力站起。

### 4——哑铃肱二头肌弯举 · 上臂

<img src="videos/0294-NbVPDMW.gif" width="150" align="right" alt="哑铃肱二头肌弯举" />

> **器械：** 哑铃 · **目标：** 肱二头肌 · **辅助：** 前臂肌群 · **媒体 ID：** `NbVPDMW`

哑铃弯举是常见的手臂孤立训练动作。左右两侧独立训练有助于发现和改善肢体力量不平衡；掌心向上的旋后握法可增强动作顶端的肱二头肌收缩。

**动作要点：** 身体直立，肘部固定在身体两侧；向上弯举时旋后手腕，在顶端夹紧肌肉，再受控下放；避免借助肩部、下背部摆动或惯性完成动作。

### 5——正握引体向上 · 背部

<img src="videos/0652-lBDjFxJ.gif" width="150" align="right" alt="正握引体向上" />

> **器械：** 自重 · **目标：** 背阔肌 · **辅助：** 肱二头肌、前臂肌群 · **媒体 ID：** `lBDjFxJ`

引体向上是发展上肢拉力的代表性自重动作，主要锻炼背阔肌，同时大量调动肱二头肌、三角肌后束和核心稳定肌群。可从弹力带辅助逐步进阶到负重训练。

**动作要点：** 采用与肩同宽或略宽的正握，从完全悬垂开始；先下沉肩胛骨，用背阔肌启动，再将胸部拉向横杆；每次重复之间充分下放，保持完整活动范围。

### 6——哑铃侧平举 · 肩部

<img src="videos/0334-DsgkuIt.gif" width="150" align="right" alt="哑铃侧平举" />

> **器械：** 哑铃 · **目标：** 三角肌 · **辅助：** 斜方肌 · **媒体 ID：** `DsgkuIt`

哑铃侧平举是增加肩部宽度的常用孤立动作，直接锻炼三角肌中束。与大重量相比，受控节奏和严格动作形式更重要。

**动作要点：** 全程保持肘部轻微弯曲；向两侧抬起哑铃，直到手臂与地面平行，不要继续抬高；以肘部而不是手腕引领动作，缓慢受控地下放以增加肌肉受力时间。

---

## 🚀 使用示例

### Python——加载和筛选

```python
import json

with open("data/exercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

print(f"动作总数：{len(exercises)}")

# 英文字段继续用于稳定筛选
chest_exercises = [ex for ex in exercises if ex["category"] == "chest"]
print(f"胸部动作：{len(chest_exercises)}")

bodyweight = [ex for ex in exercises if ex["equipment"] == "body weight"]
print(f"自重动作：{len(bodyweight)}")

# 读取中文元数据和九种语言说明
ex = exercises[0]
print(ex["name_zh"])
print(ex["category_zh"])
print(ex["instructions"]["en"])  # 英语
print(ex["instructions"]["es"])  # 西班牙语
print(ex["instructions"]["it"])  # 意大利语
print(ex["instructions"]["tr"])  # 土耳其语
print(ex["instructions"]["ru"])  # 俄语
print(ex["instructions"]["zh"])  # 中文
print(ex["instructions"]["hi"])  # 印地语
print(ex["instructions"]["pl"])  # 波兰语
print(ex["instructions"]["ko"])  # 韩语
```

### Python——使用 Pandas

```python
import json
import pandas as pd

with open("data/exercises.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# 按动作数量查看主要分类
print(df["category_zh"].value_counts().head(10))

# 所有使用杠铃、锻炼大腿的动作
barbell_legs = df[(df["equipment"] == "barbell") & (df["category"] == "upper legs")]
print(barbell_legs[["name", "name_zh", "target_zh", "equipment_zh"]])
```

### JavaScript / Node.js

```js
const exercises = require("./data/exercises.json");

console.log(`动作总数：${exercises.length}`);

// 只筛选自重动作；原英文字段保持稳定，可作为筛选键
const bodyweight = exercises.filter(ex => ex.equipment === "body weight");
console.log(`自重动作：${bodyweight.length}`);

// 按英文分类键分组，显示中文名称
const byCategory = exercises.reduce((acc, ex) => {
  acc[ex.category] = (acc[ex.category] || []);
  acc[ex.category].push(ex);
  return acc;
}, {});

const ex = exercises[0];
console.log(ex.name_zh);
console.log(ex.instructions.zh);
console.log(ex.instructions.en);
```

### TypeScript——类型安全用法

```typescript
interface Exercise {
  id: string;
  name: string;
  name_zh: string;
  category: string;
  category_zh: string;
  body_part: string;
  body_part_zh: string;
  equipment: string;
  equipment_zh: string;
  instructions: {
    en: string;
    es: string;
    it: string;
    tr: string;
    ru: string;
    zh: string;
    hi: string;
    pl: string;
    ko: string;
  };
  instruction_steps: {
    en: string[];
    es: string[];
    it: string[];
    tr: string[];
    ru: string[];
    zh: string[];
    hi: string[];
    pl: string[];
    ko: string[];
  };
  muscle_group: string;
  muscle_group_zh: string;
  secondary_muscles: string[];
  secondary_muscles_zh: string[];
  target: string;
  target_zh: string;
  media_id: string;
  image: string;
  gif_url: string;
  attribution: string;
  created_at: string;
}

import exercises from "./data/exercises.json";
const data = exercises as Exercise[];

const randomWorkout: Exercise[] = data.slice(0, 6);
console.log("前 6 个动作：", randomWorkout.map(e => e.name_zh));
```

---

## 📄 许可与使用

本仓库包含**开发接入工具和结构化动作训练数据集**，其中包括动作元数据、多语言训练说明译文和 180×180 动作媒体文件。

- **代码、工具、数据结构和训练说明文本**根据 [MIT License](LICENSE) 发布。
- **动作媒体（图片和 GIF）© [Gym visual](https://gymvisual.com/)**，经许可在本仓库中以 180×180 分辨率重新分发。请阅读英文 [`NOTICE.md`](NOTICE.md)、[中文参考译文 `NOTICE.zh-CN.md`](NOTICE.zh-CN.md) 和 [`LICENSE`](LICENSE) 中的媒体例外条款。必须完整保留 `© Gym visual — https://gymvisual.com/` 署名。再次利用受 [Gym visual 使用条款与条件](https://gymvisual.com/content/3-terms-and-conditions-of-use)约束；再次使用前请按其要求取得自己的许可。
- 本仓库不主张拥有动作内容或媒体本身的所有权。

> **法律文本说明：** 中文文档仅为阅读便利提供，不构成新的授权或法律意见。许可和媒体使用条件应以英文 [`LICENSE`](LICENSE)、[`NOTICE.md`](NOTICE.md) 及权利人的原始条款为准。
