<div align="center">

[English](README.md) | [简体中文](README.zh-CN.md)

# Exercises Dataset 中文说明

**一个面向开发者的健身动作数据集与集成向导。项目提供 1,324 条结构化健身动作记录，包含分类、身体部位、器械、目标肌群、协同肌群、多语言分步说明，并附带可直接在浏览器中打开的动作浏览器和后端接入指南。动作图片和 GIF 动画不包含在本仓库中。**

[![Exercises](https://img.shields.io/badge/Exercises-1324-blue?style=flat-square)](data/exercises.json)
[![Languages](https://img.shields.io/badge/Languages-6-green?style=flat-square)](#项目概览)
[![Format](https://img.shields.io/badge/Format-JSON-orange?style=flat-square)](data/exercises.json)
[![Media](https://img.shields.io/badge/Media-not%20included-lightgrey?style=flat-square)](#重要说明本仓库不包含动作媒体资源)

</div>

---

## 重要说明：本仓库不包含动作媒体资源

> **本仓库提供的是开发者集成向导和结构化健身动作数据集。** 动作对应的**缩略图和 GIF 动画不包含在本仓库中**。
>
> 由于相关媒体资源存在多方且相互冲突的所有权声明，本项目不会重新分发这些媒体文件。每条记录会保留 `media_id`，它是原始 ExerciseDB 媒体引用；仓库本身只提供动作元数据以及英语、西班牙语、意大利语、土耳其语、俄语和中文的动作说明。
>
> **如果你是相关媒体资源的权利人，请[提交 issue](../../issues) 或联系维护者。**

---

## 数据来源与署名

本仓库的基础动作**数据**来源于 **[AscendAPI 的 ExerciseDB v1](https://oss.exercisedb.dev)**（[API 文档](https://oss.exercisedb.dev/docs)），并通过 *omarxadel* 在 Kaggle 上重新托管的 [fitness exercises dataset](https://www.kaggle.com/datasets/omarxadel/fitness-exercises-dataset) 获取。

相关**媒体资源（图片和 GIF 动画）不包含在本仓库中**，详见上方说明。每条记录中的 `media_id` 是原始 ExerciseDB v1 媒体 ID，例如 `2gPfomN`；有权使用该媒体的用户可通过官方 CDN 路径 `static.exercisedb.dev/media/{media_id}.gif` 获取对应资源。

在基础数据之上，本仓库额外提供：

- 西班牙语、意大利语、土耳其语、俄语和中文的动作说明翻译
- 交互式动作浏览器 `index.html`
- 开发者集成向导 `setup.html`
- 数据格式整理和清理

> 原始来源署名是在 [#5](../../issues/5) 中补充的，感谢 [@shinkaidev](https://github.com/shinkaidev) 的反馈。如果你是权利人，并希望删除或澄清任何内容，请[提交 issue](../../issues)。

---

## 目录

- [重要说明：本仓库不包含动作媒体资源](#重要说明本仓库不包含动作媒体资源)
- [数据来源与署名](#数据来源与署名)
- [项目概览](#项目概览)
- [交互式浏览器与开发者向导](#交互式浏览器与开发者向导)
- [文件结构](#文件结构)
- [数据统计](#数据统计)
- [数据结构](#数据结构)
- [示例动作](#示例动作)
- [使用示例](#使用示例)
- [许可与使用](#许可与使用)

---

## 项目概览

该数据集包含 **1,324 个健身动作**，适合教育、研究、原型开发和应用集成等场景。它覆盖多种身体部位、器械类型和动作分类，可用于：

- 构建健身、训练计划或动作库应用
- 开展动作识别、推荐或检索相关的机器学习项目
- 健康、运动与康复相关研究
- 教学演示和产品原型

每条动作记录包含以下信息：

| 字段 | 说明 |
|---|---|
| 唯一 ID | 数字字符串标识符，例如 `"0001"` |
| 名称 | 完整动作名称 |
| 分类 | 主要身体部位分类 |
| 目标肌肉 | 动作主要训练的目标肌肉 |
| 肌群 | 辅助或协同发力肌群 |
| 器械 | 所需器械；徒手动作为 `body weight` |
| 动作说明 | 每个动作的分步说明 |
| 可用语言 | English、Spanish、Italian、Turkish、Russian、Chinese |
| 媒体 ID | 原始 ExerciseDB 媒体引用 ID；媒体文件本身不打包在仓库中 |

---

## 交互式浏览器与开发者向导

仓库包含两个可直接使用的 HTML 工具，不需要后端服务，使用现代浏览器打开即可。

> 注意：由于仓库不包含媒体资源，浏览器主要展示动作元数据和动作说明；缩略图和 GIF 资源槽位不会随仓库一起提供。

### `index.html`：动作浏览器

这是一个完全前端运行的动作浏览器，支持：

- 在全部 1,324 个动作中实时搜索
- 按分类、器械和目标肌肉筛选
- 通过无限滚动浏览动作卡片
- 点击卡片查看动作详情，以及英语、西班牙语、意大利语、土耳其语、俄语或中文说明

### `setup.html`：开发者集成向导

该页面用于帮助你把数据集接入自己的应用：

1. **数据库初始化**：提供 SQL Server、PostgreSQL、MySQL 和 SQLite 的 `CREATE TABLE` SQL，并可在浏览器中生成包含 1,324 条 `INSERT` 语句的 `.sql` 文件。
2. **API 接入示例**：提供 JavaScript、Python、C#、Java、PHP、Go 和 cURL 客户端示例。输入你的 API base URL 后，示例代码会自动更新。
3. **LLM 后端生成提示词**：可选择后端框架和数据库，将结构化提示词复制到 ChatGPT、Claude 或 Gemini 中，用于生成完整 REST API。支持 Express.js、FastAPI、ASP.NET Core、Spring Boot、Laravel 和 Gin。

---

## 文件结构

```text
exercises-dataset/
├── data/
│   └── exercises.json       # 完整数据集，包含 1,324 条动作记录
├── index.html               # 交互式动作浏览器，纯前端运行
├── setup.html               # 数据库导入、API 接入和后端生成向导
├── README.md                # 英文说明
└── README.zh-CN.md          # 中文说明
```

### 关键文件

- **`data/exercises.json`**：主数据文件。它是一个 JSON 数组，包含 1,324 个动作对象及其元数据。`image` 和 `gif_url` 字段不代表仓库内包含真实媒体文件；请结合 `media_id` 和上方媒体说明判断使用方式。
- **`index.html`**：独立动作浏览器，可直接在现代浏览器中打开。
- **`setup.html`**：面向开发者的数据库导入、API 集成和 LLM 辅助后端生成指南。

> `images/`、`videos/` 等媒体目录不属于本仓库交付内容，详见[重要说明](#重要说明本仓库不包含动作媒体资源)。

---

## 数据统计

| 指标 | 数量 |
|---|---:|
| 动作总数 | **1,324** |
| 动作说明语言数 | **6** |

### 按身体部位统计

| 身体部位 | 动作数量 |
|---|---:|
| Upper Arms | 292 |
| Upper Legs | 227 |
| Back | 203 |
| Waist | 169 |
| Chest | 163 |
| Shoulders | 143 |
| Lower Legs | 59 |
| Lower Arms | 37 |
| Cardio | 29 |
| Neck | 2 |

### 按器械统计

| 器械 | 动作数量 |
|---|---:|
| Body Weight | 325 |
| Dumbbell | 294 |
| Cable | 157 |
| Barbell | 154 |
| Leverage Machine | 81 |
| Band | 54 |
| Smith Machine | 48 |
| Kettlebell | 41 |
| Weighted | 36 |
| Stability Ball | 28 |
| EZ Barbell | 23 |
| Other | 83 |

> 约四分之一的动作不需要器械，适合居家训练应用或无器械训练计划场景。

---

## 数据结构

`data/exercises.json` 中的每条记录遵循以下结构：

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | `string` | 唯一数字字符串标识符，例如 `"0001"` |
| `name` | `string` | 动作名称，例如 `"3/4 sit-up"` |
| `category` | `string` | 身体部位分类，例如 `"upper arms"`、`"chest"`、`"back"` |
| `body_part` | `string` | 目标身体部位，通常与 `category` 相同 |
| `equipment` | `string` | 所需器械，例如 `"dumbbell"`、`"body weight"` |
| `instructions.en` | `string` | 英文动作说明 |
| `instructions.es` | `string` | 西班牙语动作说明 |
| `instructions.it` | `string` | 意大利语动作说明 |
| `instructions.tr` | `string` | 土耳其语动作说明 |
| `instructions.ru` | `string` | 俄语动作说明 |
| `instructions.zh` | `string` | 中文动作说明 |
| `muscle_group` | `string` | 主要协同肌群 |
| `secondary_muscles` | `array[string]` | 其他参与肌肉 |
| `target` | `string` | 主要目标肌肉，例如 `"biceps"`、`"pectoralis major"` |
| `media_id` | `string` | 原始 ExerciseDB 媒体引用 ID，例如 `"2gPfomN"` |
| `image` | `string` 或 `null` | 缩略图路径占位或引用；仓库不随附媒体文件 |
| `gif_url` | `string` 或 `null` | GIF 动画路径占位或引用；仓库不随附媒体文件 |
| `created_at` | `string` | ISO 8601 格式的记录创建时间 |

### 示例记录

```json
{
  "id": "0001",
  "name": "3/4 sit-up",
  "category": "waist",
  "body_part": "waist",
  "equipment": "body weight",
  "instructions": {
    "en": "Lie flat on your back with your knees bent and feet flat on the ground. ...",
    "es": "Túmbate sobre tu espalda con las rodillas flexionadas y los pies apoyados en el suelo. ...",
    "it": "Sdraiati sulla schiena con le ginocchia piegate e i piedi appoggiati a terra. ...",
    "tr": "Dizleriniz bükülü ve ayaklarınız yere düz basacak şekilde sırt üstü yatın. ...",
    "ru": "Лягте на спину, согните колени и поставьте ступни на землю. ...",
    "zh": "平躺，膝盖弯曲，双脚平放在地上。..."
  },
  "muscle_group": "hip flexors",
  "secondary_muscles": ["hip flexors", "lower back"],
  "target": "abs",
  "media_id": "2gPfomN",
  "image": "images/0001-2gPfomN.jpg",
  "gif_url": "videos/0001-2gPfomN.gif",
  "created_at": "2026-03-18T12:31:32.854798+00:00"
}
```

---

## 示例动作

> 媒体文件不包含在仓库中，以下示例仅列出 `media_id` 作为引用。

### 1. Barbell Bench Press / Chest

**器械：** Barbell
**目标肌肉：** Pectorals
**辅助肌肉：** Triceps、Shoulders
**Media ID：** `EIeI8Vf`

杠铃卧推是胸部训练和力量举项目中的经典动作。训练者平躺在卧推凳上，将杠铃下降至胸部附近，再向上推起。该动作会同时调动胸大肌、肱三头肌和三角肌前束，适合提升上肢推举力量和胸部肌肉量。

**关键提示：** 起杠前收紧并下沉肩胛骨，双脚踩实地面，保持自然腰弓，握距约为肩宽。下放时控制杠铃到胸部中段，再稳定推起。

### 2. Barbell Deadlift / Upper Legs、Back

**器械：** Barbell
**目标肌肉：** Glutes
**辅助肌肉：** Hamstrings、Lower Back
**Media ID：** `ila4NZS`

杠铃硬拉是典型的全身力量训练动作，重点训练臀部、腘绳肌和下背部等后链肌群，同时也需要上背部、斜方肌和握力参与。保持脊柱中立和核心支撑对动作表现与安全都很重要。

**关键提示：** 杠铃位于足中部上方，髋部后移，双手握在腿外侧，核心收紧，并让杠铃在上拉过程中尽量贴近小腿。站起至顶端时充分伸髋并收紧臀部。

### 3. Barbell Full Squat / Upper Legs

**器械：** Barbell
**目标肌肉：** Glutes
**辅助肌肉：** Quadriceps、Hamstrings、Calves、Core
**Media ID：** `qXTaZnJ`

杠铃深蹲需要下肢和核心协调发力，是力量与增肌训练中的基础动作。完整深度的深蹲通常能更充分地调动臀部和腘绳肌，也常被用于多种训练计划。

**关键提示：** 杠铃可放在上斜方肌或三角肌后束位置。下蹲前收紧核心，膝盖沿脚尖方向移动，髋部坐回并下蹲至合适深度，再通过全脚掌发力站起。

### 4. Dumbbell Biceps Curl / Upper Arms

**器械：** Dumbbell
**目标肌肉：** Biceps
**辅助肌肉：** Forearms
**Media ID：** `NbVPDMW`

哑铃弯举是常见的手臂孤立训练动作。两侧独立训练有助于发现并改善左右力量差异；掌心向上的握法能强化肱二头肌在动作顶端的收缩。

**关键提示：** 保持站姿稳定，肘部贴近身体两侧。弯举时旋后手腕并在顶端挤压收缩，下放时保持控制，避免借助肩部或躯干摆动。

### 5. Pull-up / Back

**器械：** Body Weight
**目标肌肉：** Lats
**辅助肌肉：** Biceps、Forearms
**Media ID：** `lBDjFxJ`

引体向上是训练上肢拉力的经典自重动作，主要发展背阔肌，同时需要肱二头肌、前臂和核心稳定肌群参与。它可以通过弹力带辅助或负重方式适配不同训练水平。

**关键提示：** 采用正握，握距略宽于肩。从悬垂开始，先下沉肩胛，再将胸部拉向横杠；每次重复之间充分下放，以保持动作幅度。

---

## 使用示例

### Python：加载并筛选

```python
import json

with open("data/exercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

print(f"Total exercises loaded: {len(exercises)}")

# 按身体部位分类筛选
chest_exercises = [ex for ex in exercises if ex["category"] == "chest"]
print(f"Chest exercises: {len(chest_exercises)}")

# 筛选徒手动作
bodyweight = [ex for ex in exercises if ex["equipment"] == "body weight"]
print(f"Bodyweight exercises: {len(bodyweight)}")

# 获取全部分类
categories = sorted({ex["category"] for ex in exercises})
print("Categories:", categories)

# 读取多语言动作说明
ex = exercises[0]
print(ex["instructions"]["en"])  # English
print(ex["instructions"]["es"])  # Spanish
print(ex["instructions"]["it"])  # Italian
print(ex["instructions"]["tr"])  # Turkish
print(ex["instructions"]["ru"])  # Russian
print(ex["instructions"]["zh"])  # Chinese
```

### Python：使用 Pandas 分析

```python
import json
import pandas as pd

with open("data/exercises.json", "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# 查看动作数量最多的分类
print(df["category"].value_counts().head(10))

# 查看所有杠铃下肢动作
barbell_upper_legs = df[
    (df["equipment"] == "barbell") & (df["category"] == "upper legs")
]
print(barbell_upper_legs[["name", "target", "equipment"]])
```

### JavaScript / Node.js

```js
const exercises = require("./data/exercises.json");

console.log(`Total exercises: ${exercises.length}`);

// 只保留徒手动作
const bodyweight = exercises.filter((ex) => ex.equipment === "body weight");
console.log(`Bodyweight exercises: ${bodyweight.length}`);

// 按分类分组
const byCategory = exercises.reduce((acc, ex) => {
  acc[ex.category] = acc[ex.category] || [];
  acc[ex.category].push(ex);
  return acc;
}, {});

// 读取多语言动作说明
const ex = exercises[0];
console.log(ex.instructions.en); // English
console.log(ex.instructions.es); // Spanish
console.log(ex.instructions.it); // Italian
console.log(ex.instructions.tr); // Turkish
console.log(ex.instructions.ru); // Russian
console.log(ex.instructions.zh); // Chinese
```

### TypeScript：类型安全使用

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
  };
  muscle_group: string;
  secondary_muscles: string[];
  target: string;
  media_id: string | null;
  image: string | null;
  gif_url: string | null;
  created_at: string;
}

import exercises from "./data/exercises.json";

const data = exercises as Exercise[];
const firstSix = data.slice(0, 6);

console.log("First 6 exercises:", firstSix.map((exercise) => exercise.name));
```

---

## 许可与使用

本仓库是一个**开发者集成向导和结构化健身动作数据集**，主要提供动作元数据和多语言动作说明。动作媒体资源**不包含**在仓库中。

- 基础动作数据来源于 **ExerciseDB v1**，复用前请查看[数据来源与署名](#数据来源与署名)以及 [ExerciseDB 文档](https://oss.exercisedb.dev/docs)。
- 本仓库不包含动作图片或 GIF 动画，详见[重要说明](#重要说明本仓库不包含动作媒体资源)。
- 本仓库不声明拥有底层动作内容的所有权。
- 如果你是权利人，并希望删除或澄清任何内容，请[提交 issue](../../issues) 或联系维护者。