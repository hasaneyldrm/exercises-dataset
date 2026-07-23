<div align="center">

# 💪 Exercises Dataset

[English](README.md) · **简体中文** · [日本語](README.ja.md)

<p>
  <img src="videos/0025-EIeI8Vf.gif" width="120" alt="杠铃卧推" />
  <img src="videos/0043-qXTaZnJ.gif" width="120" alt="杠铃深蹲" />
  <img src="videos/0032-ila4NZS.gif" width="120" alt="杠铃硬拉" />
  <img src="videos/0652-lBDjFxJ.gif" width="120" alt="引体向上" />
  <img src="videos/0294-NbVPDMW.gif" width="120" alt="哑铃弯举" />
  <img src="videos/0334-DsgkuIt.gif" width="120" alt="哑铃侧平举" />
</p>

**一个全面且开箱即用的健身动作数据集，包含 1,324 个动作。每个动作都配有动画 GIF、180×180 缩略图、类别、身体部位、器械、目标肌肉和肌群数据，以及 10 种语言（英语、西班牙语、意大利语、土耳其语、俄语、中文、印地语、波兰语、韩语、法语）的分步说明。**

[![动作数](https://img.shields.io/badge/Exercises-1324-blue?style=flat-square)](data/exercises.json)
[![动画 GIF](https://img.shields.io/badge/Animation%20GIFs-1324-brightgreen?style=flat-square)](videos/)
[![缩略图](https://img.shields.io/badge/Thumbnails-1324-orange?style=flat-square)](images/)
[![语言](https://img.shields.io/badge/Languages-10-green?style=flat-square)](#-概览)
[![移动应用](https://img.shields.io/badge/App-LogPress-111111?style=flat-square&logo=react)](https://github.com/hasaneyldrm/logpress-public)
[![许可证](https://img.shields.io/badge/License-MIT%20%2B%20media%20terms-blue?style=flat-square)](LICENSE)

</div>

> **📱 为 [LogPress](https://github.com/hasaneyldrm/logpress-public) 应用提供数据支持**——LogPress 是一款 AI 辅助的训练记录器，本数据集是它的动作数据层。正在构建自己的健身应用？可以直接把它接入后端。

---

## 📦 数据来源

**本仓库提供：**

- 1,324 个动作，包含类别、身体部位、器械、目标肌肉和肌群数据
- 每个动作都有动画 GIF 和 180×180 缩略图（媒体内容 © [Gym visual](https://gymvisual.com/)——参见[许可与使用](#-许可与使用)）
- 10 种语言的分步说明（🇬🇧 英语、🇪🇸 西班牙语、🇮🇹 意大利语、🇹🇷 土耳其语、🇷🇺 俄语、🇨🇳 中文、🇮🇳 印地语、🇵🇱 波兰语、🇰🇷 韩语、🇫🇷 法语）
- 交互式浏览器（`index.html`）和开发者设置指南（`setup.html`）

---

## 📋 目录

- [数据来源](#-数据来源)
- [概览](#-概览)
- [交互式浏览器与开发者设置](#-交互式浏览器与开发者设置)
- [文件结构](#-文件结构)
- [统计信息](#-统计信息)
- [数据架构](#-数据架构)
- [示例动作](#-示例动作)
- [使用示例](#-使用示例)
- [许可与使用](#-许可与使用)

---

## 🔍 概览

本数据集是一个为教育和研究用途整理的集合，包含 **1,324 个健身动作**。它覆盖多种肌群、器械类型和动作类别，非常适合：

- 构建健身或训练计划应用
- 涉及动作识别或推荐的机器学习项目
- 健康与运动研究
- 教学演示和原型开发

每条动作记录包含：

| 字段 | 说明 |
|---|---|
| 唯一 ID | 数字标识符（例如 `"0001"`） |
| 名称 | 完整、描述性的动作名称 |
| 类别 | 主要锻炼的肌群 |
| 目标 | 具体目标肌肉 |
| 肌群 | 辅助肌或协同肌 |
| 器械 | 所需器械（徒手动作为 `body weight`） |
| 说明 | 每个动作的分步说明 |
| 可用语言 | 🇬🇧 英语 · 🇪🇸 西班牙语 · 🇮🇹 意大利语 · 🇹🇷 土耳其语 · 🇷🇺 俄语 · 🇨🇳 中文 · 🇮🇳 印地语 · 🇵🇱 波兰语 · 🇰🇷 韩语 · 🇫🇷 法语 |
| 媒体 | 每个动作都有 180×180 缩略图（`image`）和动画 GIF（`gif_url`）——媒体内容 © Gym visual，参见[许可与使用](#-许可与使用) |

---

## 🖥️ 交互式浏览器与开发者设置

本仓库包含两个开箱即用的 HTML 工具——无需服务器，直接用浏览器打开即可。

> **注意：**浏览器会同时显示每个动作的 180×180 缩略图、动画 GIF、元数据和说明。

### `index.html`——动作浏览器

一个完全在客户端运行的动作浏览器，支持：
- 在全部 1,324 个动作中实时搜索
- 按类别、器械和目标肌肉筛选
- 无限滚动网格
- 点击任意卡片，查看完整详情以及英语、西班牙语、意大利语、土耳其语、俄语、中文、印地语、波兰语、韩语或法语说明

### `setup.html`——开发者设置指南

将数据集集成到自己应用中的分步指南：

1. **数据库设置**——提供适用于 SQL Server、PostgreSQL、MySQL 和 SQLite 的 `CREATE TABLE` SQL。可完全在浏览器中生成包含全部 1,324 条 INSERT 语句、可直接运行的 `.sql` 文件。
2. **API 集成**——提供可复制粘贴的 **JavaScript、Python、C#、Java、PHP、Go 和 cURL** 客户端代码，演示如何调用后端 API。输入基础 URL 后，所有示例会实时更新。
3. **询问你的 LLM**——提供结构化提示词（可选择框架和数据库），将其粘贴到 ChatGPT、Claude 或 Gemini，即可一次生成完整、可用于生产环境的 REST API。支持 Express.js、FastAPI、ASP.NET Core、Spring Boot、Laravel 和 Gin。

---

## 📂 文件结构

```
exercises-dataset/
├── data/
│   ├── exercises.json        # Full dataset — 1,324 exercise records (JSON array)
│   └── exercises.schema.json # JSON Schema (2020-12) describing every record
├── images/                  # 1,324 × 180×180 thumbnails  (© Gym visual)
├── videos/                  # 1,324 × 180×180 animation GIFs  (© Gym visual)
├── index.html               # Interactive exercise browser (client-side, no server needed)
├── setup.html               # Developer setup guide (DB import + API integration)
├── NOTICE.md                # Media attribution & license terms
└── README.md
```

### 关键文件

- **`data/exercises.json`**——主要数据文件。它是一个包含 1,324 个动作对象及其全部元数据的 JSON 数组。`image` 和 `gif_url` 指向本地 180×180 资源，每条记录都带有 `attribution` 字段；`media_id` 保存原始媒体引用 ID。
- **`data/exercises.schema.json`**——一个 [JSON Schema](https://json-schema.org/)（Draft 2020-12），正式描述每个字段、字段类型和约束。可使用任何标准 JSON Schema 验证器来校验本数据集或你添加的数据。
- **`images/`、`videos/`**——180×180 缩略图和动画 GIF（© [Gym visual](https://gymvisual.com/)，经许可使用）。
- **`index.html`**——独立的动作浏览器，可直接在任何现代浏览器中打开。
- **`setup.html`**——数据库设置、API 集成和 LLM 辅助后端生成的开发者指南。
- **`LICENSE`、`NOTICE.md`**——MIT（代码/数据）以及 Gym visual 的媒体条款。

---

## 📊 统计信息

| 指标 | 数量 |
|---|---|
| 动作总数 | **1,324** |
| 说明语言 | **10** |

### 按身体部位统计动作

| 身体部位 | 动作数量 |
|---|---|
| 上臂 | 292 |
| 大腿 | 227 |
| 背部 | 203 |
| 腰腹 | 169 |
| 胸部 | 163 |
| 肩部 | 143 |
| 小腿 | 59 |
| 前臂 | 37 |
| 有氧 | 29 |
| 颈部 | 2 |

### 按器械统计动作

| 器械 | 动作数量 |
|---|---|
| 自重 | 325 |
| 哑铃 | 294 |
| 拉力器 | 157 |
| 杠铃 | 154 |
| 杠杆式器械 | 81 |
| 弹力带 | 54 |
| 史密斯机 | 48 |
| 壶铃 | 41 |
| 负重 | 36 |
| 健身球 | 28 |
| EZ 杠铃 | 23 |
| 其他 | 83 |

> **注意：**约 25% 的动作完全不需要器械，非常适合居家训练应用。

---

## 🗂️ 数据架构

`data/exercises.json` 中的每条记录都采用以下结构。同时提供了机器可读的 [JSON Schema](data/exercises.schema.json) 以供验证。

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | `string` | 唯一数字标识符（例如 `"0001"`） |
| `name` | `string` | 完整动作名称（例如 `"3/4 Sit-up"`） |
| `category` | `string` | 身体部位类别（例如 `"upper arms"`、`"chest"`、`"back"`） |
| `body_part` | `string` | 与 `category` 相同——目标身体部位 |
| `equipment` | `string` | 所需器械（例如 `"dumbbell"`、`"body weight"`） |
| `instructions.en` | `string` | 完整的英语分步说明 |
| `instructions.es` | `string` | 完整的西班牙语分步说明 |
| `instructions.it` | `string` | 完整的意大利语分步说明 |
| `instructions.tr` | `string` | 完整的土耳其语分步说明 |
| `instructions.ru` | `string` | 完整的俄语分步说明 |
| `instructions.zh` | `string` | 完整的中文分步说明 |
| `instructions.hi` | `string` | 完整的印地语分步说明 |
| `instructions.pl` | `string` | 完整的波兰语分步说明 |
| `instructions.ko` | `string` | 完整的韩语分步说明 |
| `instructions.fr` | `string` | 完整的法语分步说明 |
| `instruction_steps.<lang>` | `array[string]` | 按语言拆分为有序步骤数组的同一组说明（`en`、`es`、`it`、`tr`、`ru`、`zh`、`hi`、`pl`、`ko`、`fr`） |
| `muscle_group` | `string` | 主要协同肌群 |
| `secondary_muscles` | `array[string]` | 参与动作的其他肌肉 |
| `target` | `string` | 主要目标肌肉（例如 `"biceps"`、`"pectoralis major"`） |
| `media_id` | `string` | 原始媒体引用 ID（例如 `"2gPfomN"`） |
| `image` | `string` | 180×180 缩略图的路径（例如 `"images/0001-2gPfomN.jpg"`） |
| `gif_url` | `string` | 180×180 动画 GIF 的路径（例如 `"videos/0001-2gPfomN.gif"`） |
| `attribution` | `string` | 媒体版权声明——`"© Gym visual — https://gymvisual.com/"` |
| `created_at` | `string` | 记录创建时间的 ISO 8601 时间戳 |

### 示例记录

```json
{
  "id": "0001",
  "name": "3/4 sit-up",
  "category": "waist",
  "body_part": "waist",
  "equipment": "body weight",
  "instructions": {
    "en": "Lie flat on your back with your knees bent and feet flat on the ground. Place your hands behind your head with your elbows pointing outwards. Engaging your abs, slowly lift your upper body off the ground, curling forward until your torso is at a 45-degree angle. Pause for a moment at the top, then slowly lower your upper body back down to the starting position. Repeat for the desired number of repetitions.",
    "es": "Túmbate sobre tu espalda con las rodillas flexionadas y los pies apoyados en el suelo. ...",
    "it": "Sdraiati sulla schiena con le ginocchia piegate e i piedi appoggiati a terra. ...",
    "tr": "Sırt üstü yatın, dizlerinizi bükün ve ayaklarınızı yere düz koyun. ...",
    "ru": "Лягте на спину, согните колени и поставьте ступни на землю. ...",
    "zh": "平躺，膝盖弯曲，双脚平放在地上。...",
    "hi": "अपने घुटनों को मोड़कर और पैरों को ज़मीन पर सपाट रखते हुए अपनी पीठ के बल लेट जाएँ।...",
    "pl": "Połóż się płasko na plecach, ugnij kolana i oprzyj stopy płasko na pod ...",
    "ko": "등을 바닥에 누워 무릎을 구부리고 발을 바닥에 붙입니다. ...",
    "fr": "Allonge-toi sur le dos, les genoux fléchis et les pieds à plat au sol. ..."
  },
  "muscle_group": "hip flexors",
  "secondary_muscles": ["hip flexors", "lower back"],
  "target": "abs",
  "media_id": "2gPfomN",
  "image": "images/0001-2gPfomN.jpg",
  "gif_url": "videos/0001-2gPfomN.gif",
  "attribution": "© Gym visual — https://gymvisual.com/",
  "created_at": "2026-03-18T12:31:32.854798+00:00"
}
```

---

## 🎬 示例动作

> 每个示例都附带 180×180 缩略图（`image`）和动画 GIF（`gif_url`），© [Gym visual](https://gymvisual.com/)。

### 1——杠铃卧推 · 胸部

<img src="videos/0025-EIeI8Vf.gif" width="150" align="right" alt="杠铃卧推" />

> **器械：**杠铃 · **目标：**胸肌 · **辅助：**肱三头肌、肩部 · **媒体 ID：**`EIeI8Vf`

杠铃卧推是胸部训练的基石，也是力量举“三大项”之一。练习时平躺在卧推凳上，将负重杠铃下放至胸部，再爆发式推起。它会同时调动胸肌、肱三头肌和三角肌前束，是提升上肢推力和增加胸部肌肉量最有效的单项训练之一。

**动作要点：**出杠前先收紧并下沉肩胛骨。双脚平放在地面，下背部保持自然拱起，握距与肩同宽。控制杠铃下放至胸部中段，再通过脚跟发力向上推起。

### 2——杠铃硬拉 · 大腿/背部

<img src="videos/0032-ila4NZS.gif" width="150" align="right" alt="杠铃硬拉" />

> **器械：**杠铃 · **目标：**臀肌 · **辅助：**腘绳肌、下背部 · **媒体 ID：**`ila4NZS`

杠铃硬拉被广泛认为是终极全身力量训练。它几乎会调动后侧链的所有主要肌群——臀肌、腘绳肌和下背部——同时也需要上背部、斜方肌和握力大量参与。正确的脊柱排列和核心绷紧技巧对训练表现与安全都至关重要。

**动作要点：**起始时让杠铃位于脚掌中部上方。髋部后移俯身，在双腿外侧握杠，强力收紧核心，并在整个提拉过程中让杠铃贴近胫骨。用脚蹬地，站至顶端时夹紧臀部并完全伸展髋关节完成锁定。

### 3——杠铃全蹲 · 大腿

<img src="videos/0043-qXTaZnJ.gif" width="150" align="right" alt="杠铃全蹲" />

> **器械：**杠铃 · **目标：**臀肌 · **辅助：**股四头肌、腘绳肌、小腿、核心 · **媒体 ID：**`qXTaZnJ`

杠铃全蹲常被称为“动作之王”，需要整个下肢与核心协调发力。与半蹲相比，蹲至低于平行位置能最大程度调动臀肌和腘绳肌。它是几乎所有力量与增肌计划的基础。

**动作要点：**将杠铃放在上斜方肌（高杠位）或三角肌后束（低杠位）。下蹲前收紧核心，膝盖沿脚尖方向向外打开，坐髋下沉，直到大腿低于与地面平行的位置。用整个脚掌发力站起。

### 4——哑铃肱二头肌弯举 · 上臂

<img src="videos/0294-NbVPDMW.gif" width="150" align="right" alt="哑铃肱二头肌弯举" />

> **器械：**哑铃 · **目标：**肱二头肌 · **辅助：**前臂 · **媒体 ID：**`NbVPDMW`

哑铃肱二头肌弯举是最广为人知的手臂孤立训练。分别训练两侧有助于发现并纠正肢体之间的力量差异。旋后握法（掌心向上）能在动作顶端最大程度收缩肱二头肌。

**动作要点：**身体直立，肘部贴紧身体两侧。向上弯举时旋后手腕，在顶端夹紧肌肉，再控制下放，不要摆动。避免借助肩部或下背部的惯性。

### 5——引体向上 · 背部

<img src="videos/0652-lBDjFxJ.gif" width="150" align="right" alt="引体向上" />

> **器械：**自重 · **目标：**背阔肌 · **辅助：**肱二头肌、前臂 · **媒体 ID：**`lBDjFxJ`

引体向上是衡量上肢拉力的黄金标准徒手动作。它主要锻炼背阔肌，塑造理想的 V 形背部，同时也会大量调动肱二头肌、三角肌后束和核心稳定肌群。它可以从初学者的弹力带辅助逐步进阶到负重训练。

**动作要点：**以与肩同宽或略宽的正握方式完全悬垂。先下压肩胛骨，通过背阔肌启动，然后将胸部拉向横杠。每次重复之间都要完全下放，以保持完整动作幅度。

### 6——哑铃侧平举 · 肩部

<img src="videos/0334-DsgkuIt.gif" width="150" align="right" alt="哑铃侧平举" />

> **器械：**哑铃 · **目标：**三角肌 · **辅助：**斜方肌 · **媒体 ID：**`DsgkuIt`

哑铃侧平举是增加肩宽的常用孤立动作。它直接针对三角肌外侧（中束），这部分肌肉决定了宽肩外观。受控的节奏和严格的动作规范远比负重量重要。

**动作要点：**站立时肘部始终保持轻微弯曲。向身体两侧抬起哑铃，直到手臂与地面平行，不要抬得更高。以肘部而非手腕引领动作，再缓慢、受控地下放，以最大限度增加肌肉受力时间。

---

## 🚀 使用示例

### Python——加载并筛选

```python
import json

with open("data/exercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

print(f"Total exercises loaded: {len(exercises)}")

# Filter by category
chest_exercises = [ex for ex in exercises if ex["category"] == "chest"]
print(f"Chest exercises: {len(chest_exercises)}")
# -> Chest exercises: 163

# Filter by equipment
bodyweight = [ex for ex in exercises if ex["equipment"] == "body weight"]
print(f"Bodyweight exercises: {len(bodyweight)}")
# -> Bodyweight exercises: 325

# Get all unique categories
categories = sorted({ex["category"] for ex in exercises})
print("Categories:", categories)

# Access multilingual instructions
ex = exercises[0]
print(ex["instructions"]["en"])  # English
print(ex["instructions"]["es"])  # Spanish
print(ex["instructions"]["it"])  # Italian
print(ex["instructions"]["tr"])  # Turkish
print(ex["instructions"]["ru"])  # Russian
print(ex["instructions"]["zh"])  # Chinese
print(ex["instructions"]["hi"])  # Hindi
print(ex["instructions"]["pl"])  # Polish
print(ex["instructions"]["ko"])  # Korean
print(ex["instructions"]["fr"])  # French
```

### Python——使用 Pandas 加载

```python
import json
import pandas as pd

with open("data/exercises.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Top categories by exercise count
print(df["category"].value_counts().head(10))

# All barbell exercises targeting upper legs
barbell_quads = df[(df["equipment"] == "barbell") & (df["category"] == "upper legs")]
print(barbell_quads[["name", "target", "equipment"]])
```

### JavaScript / Node.js

```js
const exercises = require("./data/exercises.json");

console.log(`Total exercises: ${exercises.length}`);

// Bodyweight exercises only
const bodyweight = exercises.filter(ex => ex.equipment === "body weight");
console.log(`Bodyweight exercises: ${bodyweight.length}`);
// -> Bodyweight exercises: 325

// Group exercises by category
const byCategory = exercises.reduce((acc, ex) => {
  acc[ex.category] = (acc[ex.category] || []);
  acc[ex.category].push(ex);
  return acc;
}, {});

// Access multilingual instructions
const ex = exercises[0];
console.log(ex.instructions.en); // English
console.log(ex.instructions.es); // Spanish
console.log(ex.instructions.it); // Italian
console.log(ex.instructions.tr); // Turkish
console.log(ex.instructions.ru); // Russian
console.log(ex.instructions.zh); // Chinese
console.log(ex.instructions.hi); // Hindi
console.log(ex.instructions.pl); // Polish
console.log(ex.instructions.ko); // Korean
console.log(ex.instructions.fr); // French
```

### TypeScript——类型安全的用法

```typescript
interface Exercise {
  id: string;
  name: string;
  category: string;
  body_part: string;
  equipment: string;
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
    fr: string;
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
    fr: string[];
  };
  muscle_group: string;
  secondary_muscles: string[];
  target: string;
  media_id: string;
  image: string;
  gif_url: string;
  attribution: string;
  created_at: string;
}

import exercises from "./data/exercises.json";
const data = exercises as Exercise[];

const randomWorkout: Exercise[] = data.slice(0, 6);
console.log("First 6 exercises:", randomWorkout.map(e => e.name));
```

---

## 📄 许可与使用

本仓库是一个**开发者设置向导和结构化动作数据集**，包括动作元数据、多语言说明译文以及 180×180 动作媒体文件。

- **代码、工具、数据集结构和说明文本**采用 [MIT License](LICENSE) 发布。
- **动作媒体（图片和 GIF）版权所有 © [Gym visual](https://gymvisual.com/)**，并在获得许可后以 180×180 分辨率在此重新分发——参见 [`NOTICE.md`](NOTICE.md) 和 [`LICENSE`](LICENSE) 中的媒体例外条款。必须保留 `© Gym visual — https://gymvisual.com/` 署名。再利用受 [Gym visual 的条款与条件](https://gymvisual.com/content/3-terms-and-conditions-of-use)约束；在重新利用这些媒体之前，请在那里取得自己的许可。
- 本仓库**不声称拥有**底层动作内容或媒体。
