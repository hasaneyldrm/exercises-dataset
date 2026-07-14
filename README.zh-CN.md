[English](README.md) · **简体中文**

<div align="center">

# 💪 Exercises Dataset 动作训练数据集

<p>
  <img src="videos/0025-EIeI8Vf.gif" width="120" alt="杠铃卧推" />
  <img src="videos/0043-qXTaZnJ.gif" width="120" alt="杠铃全蹲" />
  <img src="videos/0032-ila4NZS.gif" width="120" alt="杠铃硬拉" />
  <img src="videos/0652-lBDjFxJ.gif" width="120" alt="引体向上" />
  <img src="videos/0294-NbVPDMW.gif" width="120" alt="哑铃肱二头肌弯举" />
  <img src="videos/0334-DsgkuIt.gif" width="120" alt="哑铃侧平举" />
</p>

**一套包含 1,324 个健身动作的开箱即用数据集。每个动作均提供 GIF 动画、180×180 缩略图、分类、身体部位、器械、目标肌肉、肌群信息，以及英语、西班牙语、意大利语、土耳其语、俄语、中文、印地语、波兰语和韩语共 9 种语言的训练说明。**

[![动作数量](https://img.shields.io/badge/动作数量-1324-blue?style=flat-square)](data/exercises.json)
[![GIF 动画](https://img.shields.io/badge/GIF%20动画-1324-brightgreen?style=flat-square)](videos/)
[![缩略图](https://img.shields.io/badge/缩略图-1324-orange?style=flat-square)](images/)
[![说明语言](https://img.shields.io/badge/说明语言-9-green?style=flat-square)](#数据内容)
[![许可](https://img.shields.io/badge/License-MIT%20%2B%20媒体条款-blue?style=flat-square)](LICENSE)

</div>

本仓库同时提供可扩展的浏览器多语言系统。简体中文动作名、健身术语、页面文案和精修训练步骤全部集中在 [`locales/zh-CN.js`](locales/zh-CN.js)，不会向基础 JSON 增加 `_zh` 字段，也不会改变原有 Schema。

简体中文语言包已完成两轮独立逐条复核：对照规范英文数据检查全部 1,324 个动作名、7,662 条训练步骤、107 个术语标签和 90 条页面文案；英文来源存在歧义时再核对对应图片或 GIF。只有语义明确或两轮结论一致的问题才会修正，尚不能确定的源数据歧义不作猜测性改写。

## 数据内容

- 1,324 个动作及其分类、身体部位、器械、目标肌肉和协同肌群
- 每个动作一张 180×180 缩略图和一个 GIF 动画
- 9 种语言的完整说明与分步说明
- 可直接打开的动作浏览器 `index.html`
- 数据库导入、API 示例和大模型提示词页面 `setup.html`
- 覆盖全部 1,324 个动作的简体中文语言包

媒体文件 © [Gym visual](https://gymvisual.com/)，许可和署名要求请阅读 [`NOTICE.md`](NOTICE.md)；[`NOTICE.zh-CN.md`](NOTICE.zh-CN.md) 仅为辅助译文。

## 动作浏览器与开发接入

### `index.html`

直接双击打开即可使用，支持：

- 英文和简体中文界面，首次访问跟随浏览器语言，之后记住用户选择
- 使用中英文动作名、分类、器械和肌肉术语搜索
- 按分类、器械和目标肌肉筛选，切换语言不会丢失筛选状态
- 无限滚动、响应式卡片和动作详情弹窗
- 查看数据集中已有的 9 种语言训练步骤
- 中文模式优先显示语言包中精修后的中文动作名和步骤

### `setup.html`

`setup.html` 按上游方式在生成 SQL 时读取 `data/exercises.json`，因此应与仓库中的数据、语言包和媒体文件一起部署到 Web 服务器。页面不再重复内嵌整份动作数据。

setup 支持 SQL Server、PostgreSQL、MySQL 和 SQLite，可导出：

- 1,324 条基础动作记录
- manifest 中所有已注册非基础语言包的显式翻译
- 使用 `(exercise_id, locale)` 作为主键的通用 `exercise_translations` 表

SQL Server 使用 `NVARCHAR` 和 `N'…'` Unicode 字面量，MySQL 使用 `utf8mb4`，PostgreSQL 使用 `JSONB`，SQLite 使用 UTF-8 文本和 JSON 字符串。

## 可扩展语言包

```text
locales/
├── runtime.js    # 共享 i18n 运行时、回退和语言记忆
├── manifest.js   # 已注册语言及文件路径
├── en.js         # 英文页面文案，动作内容使用基础数据
└── zh-CN.js      # 完整简体中文语言包
```

每种语言只维护一个经典 UTF-8 JavaScript 文件，结构如下：

```js
window.ExercisesI18n.registerLocale({
  code: 'zh-CN',
  label: '简体中文',
  instructionCode: 'zh',
  dir: 'ltr',
  complete: true,
  ui: {
    index: {},
    setup: {}
  },
  instructionLabels: {},
  taxonomy: {
    categories: {},
    bodyParts: {},
    equipment: {},
    targets: {},
    muscles: {}
  },
  records: {
    '0001': {
      name: '3/4 仰卧起坐',
      steps: ['平躺，膝盖弯曲，双脚平放在地上。']
    }
  }
});
```

新增语言时：

1. 复制 `locales/en.js`，文件名使用 BCP 47 代码，例如 `fr-FR.js`。
2. 只在该文件中翻译 index、setup、术语和动作内容。
3. 在 `locales/manifest.js` 增加一行语言代码、显示名和文件路径。

不需要修改 `index.html` 或 `setup.html`。语言包可以逐步完成；缺失项目会逐项回退英文，SQL 只导出明确提供的翻译，不会把英文回退内容标记成目标语言。

## 文件结构

```text
exercises-dataset/
├── data/
│   ├── exercises.json        # 1,324 条规范基础记录
│   └── exercises.schema.json # JSON Schema 2020-12
├── locales/                  # 浏览器 i18n 运行时和语言包
├── images/                   # 1,324 张 180×180 缩略图
├── videos/                   # 1,324 个 GIF 动画
├── index.html                # 动作浏览器
├── setup.html                # 数据库和 API 接入指南
├── README.md                 # 英文说明
├── README.zh-CN.md           # 本文件
├── NOTICE.md                 # 权威英文媒体声明
├── NOTICE.zh-CN.md           # 中文辅助译文
└── LICENSE
```

## 基础数据结构

[`data/exercises.json`](data/exercises.json) 是规范数据源，保留上游原始字段：

| 字段 | 说明 |
|---|---|
| `id` | 四位动作 ID，例如 `"0001"` |
| `name` | 规范英文动作名 |
| `category`、`body_part` | 英文身体部位分类 |
| `equipment` | 英文器械名称 |
| `instructions.<lang>` | 各语言完整训练说明 |
| `instruction_steps.<lang>` | 各语言分步说明数组 |
| `muscle_group` | 主要协同肌群 |
| `secondary_muscles` | 辅助肌群数组 |
| `target` | 主要目标肌肉 |
| `media_id` | 原始媒体引用 ID |
| `image`、`gif_url` | 本地缩略图和 GIF 路径 |
| `attribution` | 媒体版权署名 |
| `created_at` | ISO 8601 创建时间 |

中文动作名和术语不写入基础 JSON，而是在浏览器运行时按动作 ID 和英文 canonical value 叠加。因此现有 JSON 使用方、Schema 和英文筛选值都保持兼容。

## 通用翻译表

setup 生成的数据库结构在上游 `exercises` 表之外增加：

```text
exercise_translations
- exercise_id
- locale
- name
- category
- body_part
- equipment
- target
- muscle_group
- secondary_muscles
- instructions
- instruction_steps
- PRIMARY KEY (exercise_id, locale)
- FOREIGN KEY (exercise_id) REFERENCES exercises(id)
```

英文仍由 `exercises` 表承载。当前完整中文包会写入 1,324 条 `locale = 'zh-CN'` 的翻译记录；以后新增语言不会要求增加新的数据库列。

## 使用基础 JSON

Python：

```python
import json

with open("data/exercises.json", "r", encoding="utf-8") as file:
    exercises = json.load(file)

print(len(exercises))
print(exercises[0]["name"])
print(exercises[0]["instructions"]["zh"])
```

Node.js：

```js
const exercises = require('./data/exercises.json');

console.log(exercises.length);
console.log(exercises[0].name);
console.log(exercises[0].instruction_steps.zh);
```

## 许可与使用

- 代码、数据结构和训练说明采用 [`LICENSE`](LICENSE) 中的 MIT License。
- 图片和 GIF 动画归 [Gym visual](https://gymvisual.com/) 所有，经许可仅以 180×180 分辨率重新分发。
- 使用媒体时必须保留 `© Gym visual — https://gymvisual.com/` 署名，并遵守 Gym visual 的条款。
- 中文 [`NOTICE.zh-CN.md`](NOTICE.zh-CN.md) 仅供参考；涉及许可时以英文 [`NOTICE.md`](NOTICE.md)、[`LICENSE`](LICENSE) 和权利人的原始条款为准。
