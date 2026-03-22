<div align="center">

# 💪 Exercises Dataset

<p>
  <img src="images/0025-EIeI8Vf.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/0043-qXTaZnJ.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/0032-ila4NZS.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/0294-NbVPDMW.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/0652-lBDjFxJ.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/0334-DsgkuIt.jpg" width="140" style="border-radius:8px; margin:4px;" />
</p>

**A comprehensive, ready-to-use fitness exercise dataset with 1,324 exercises — each with animation GIFs, thumbnail images, muscle group info, equipment data, and full bilingual instructions.**

[![Exercises](https://img.shields.io/badge/Exercises-1324-blue?style=flat-square)](data/exercises.json)
[![Videos](https://img.shields.io/badge/Animation%20GIFs-1324-green?style=flat-square)](videos/)
[![Images](https://img.shields.io/badge/Thumbnails-1324-orange?style=flat-square)](images/)
[![License](https://img.shields.io/badge/License-Educational%20Only-red?style=flat-square)](#-license)

</div>

---

## ⚠️ Disclaimer

> This repository is provided for **educational and non-commercial research purposes only**.
> All exercise media (images, videos) belong to their respective copyright holders.
> **Commercial use is strictly prohibited.**
> If you are a copyright owner and wish to have your content removed, please [open an issue](../../issues) or contact the repository owner.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Interactive Browser & Developer Setup](#-interactive-browser--developer-setup)
- [File Structure](#-file-structure)
- [Statistics](#-statistics)
- [Data Schema](#-data-schema)
- [Sample Exercises](#-sample-exercises)
- [Usage Examples](#-usage-examples)
- [License](#-license)

---

## 🔍 Overview

This dataset is a curated collection of **1,324 fitness exercises** sourced for educational and research purposes. It covers a wide range of muscle groups, equipment types, and exercise categories — making it ideal for:

- Building fitness or workout planning applications
- Machine learning projects involving exercise recognition or recommendation
- Health and wellness research
- Educational demonstrations and prototypes

Each exercise entry contains:

| Field | Description |
|---|---|
| Unique ID | Numeric identifier (e.g. `"0001"`) |
| Name | Full descriptive exercise name |
| Category | Primary muscle group targeted |
| Target | Specific target muscle |
| Muscle Group | Supporting / synergist muscles |
| Equipment | Equipment required (or `body weight` for bodyweight) |
| Instructions (EN) | Step-by-step instructions in English |
| Instructions (TR) | Step-by-step instructions in Turkish |
| Thumbnail | Static `.jpg` preview image |
| Animation GIF | `.gif` animation showing the movement |

---

## 🖥️ Interactive Browser & Developer Setup

This repository includes two ready-to-use HTML tools — no server required, just open in a browser.

### `index.html` — Exercise Browser

A fully client-side exercise explorer with:
- Live search across all 1,324 exercises
- Filter by category, equipment, and target muscle
- Infinite scroll grid with thumbnail previews
- Click any card to see full details, GIF animation, and bilingual instructions

### `setup.html` — Developer Setup Guide

A step-by-step guide for integrating the dataset into your own application:

1. **Database Setup** — `CREATE TABLE` SQL for SQL Server, PostgreSQL, MySQL, and SQLite. Generate a ready-to-run `.sql` file with all 1,324 INSERT statements, built entirely in your browser.
2. **API Integration** — Copy-paste client code in **JavaScript, Python, C#, Java, PHP, Go, and cURL** showing how to call your backend API. Enter your base URL and all examples update live.
3. **Ask Your LLM** — A structured prompt (choose your framework + database) that you can paste into ChatGPT, Claude, or Gemini to generate a complete, production-ready REST API in one shot. Supports Express.js, FastAPI, ASP.NET Core, Spring Boot, Laravel, and Gin.

---

## 📂 File Structure

```
exercises-dataset/
├── data/
│   └── exercises.json       # Full dataset — 1,324 exercise records (JSON array)
├── images/                  # Exercise thumbnail images (.jpg) — 1,324 files
├── videos/                  # Exercise animation GIFs (.gif) — 1,324 files
├── index.html               # Interactive exercise browser (client-side, no server needed)
├── setup.html               # Developer setup guide (DB import + API integration)
└── README.md
```

### Key Files

- **`data/exercises.json`** — The primary data file. A JSON array of 1,324 exercise objects with all metadata and paths to corresponding media files.
- **`images/`** — 1,324 thumbnail JPGs named with the exercise ID (e.g. `0001-2gPfomN.jpg`).
- **`videos/`** — 1,324 GIF animations demonstrating each movement (e.g. `0001-2gPfomN.gif`).
- **`index.html`** — Standalone exercise browser. Open directly in any modern browser.
- **`setup.html`** — Developer guide for DB setup, API integration, and LLM-assisted backend generation.

---

## 📊 Statistics

| Metric | Count |
|---|---|
| Total Exercises | **1,324** |
| Animation GIFs | **1,324** |
| Thumbnail Images | **1,324** |

### Exercises by Body Part

| Body Part | Exercise Count |
|---|---|
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

### Exercises by Equipment

| Equipment | Exercise Count |
|---|---|
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

> **Note:** ~25% of exercises require no equipment at all — great for at-home workout applications.

---

## 🗂️ Data Schema

Each record in `data/exercises.json` follows this structure:

| Field | Type | Description |
|---|---|---|
| `id` | `string` | Unique numeric identifier (e.g. `"0001"`) |
| `name` | `string` | Full exercise name (e.g. `"3/4 Sit-up"`) |
| `category` | `string` | Body part category (e.g. `"upper arms"`, `"chest"`, `"back"`) |
| `body_part` | `string` | Same as `category` — body part targeted |
| `equipment` | `string` | Required equipment (e.g. `"dumbbell"`, `"body weight"`) |
| `instructions.en` | `string` | Full step-by-step instructions in English |
| `instructions.tr` | `string` | Full step-by-step instructions in Turkish |
| `muscle_group` | `string` | Primary synergist muscle group |
| `secondary_muscles` | `array[string]` | Additional muscles involved |
| `target` | `string` | Primary target muscle (e.g. `"biceps"`, `"pectoralis major"`) |
| `image` | `string` | Relative path to the thumbnail image (e.g. `"images/0001-2gPfomN.jpg"`) |
| `gif_url` | `string` | Relative path to the animation GIF (e.g. `"videos/0001-2gPfomN.gif"`) |
| `created_at` | `string` | ISO 8601 timestamp of record creation |

### Sample Record

```json
{
  "id": "0001",
  "name": "3/4 sit-up",
  "category": "waist",
  "body_part": "waist",
  "equipment": "body weight",
  "instructions": {
    "en": "Lie flat on your back with your knees bent and feet flat on the ground. Place your hands behind your head with your elbows pointing outwards. Engaging your abs, slowly lift your upper body off the ground, curling forward until your torso is at a 45-degree angle. Pause for a moment at the top, then slowly lower your upper body back down to the starting position. Repeat for the desired number of repetitions.",
    "tr": "Sırt üstü yatın, dizlerinizi bükün ve ayaklarınızı yere düz koyun. Ellerinizi başınızın arkasına, dirsekleriniz dışa bakacak şekilde yerleştirin. Karın kaslarınızı kasarak üst vücudunuzu yerden kaldırın ve gövdeniz 45 derecelik açıya gelene kadar öne doğru kıvırın. Bir an için bu pozisyonda bekleyin, ardından yavaşça başlangıç konumuna geri dönün. İstenen tekrar sayısı için hareketi tekrarlayın."
  },
  "muscle_group": "hip flexors",
  "secondary_muscles": ["hip flexors", "lower back"],
  "target": "abs",
  "image": "images/0001-2gPfomN.jpg",
  "gif_url": "videos/0001-2gPfomN.gif",
  "created_at": "2026-03-18 12:31:32.854798+00:00"
}
```

---

## 🎬 Sample Exercises

---

### 1 — Barbell Bench Press · Chest

<img src="images/0025-EIeI8Vf.jpg" width="320" />

> **Animation:** `videos/0025-EIeI8Vf.gif`
> **Equipment:** Barbell · **Target:** Pectorals · **Secondary:** Triceps, Shoulders

The Barbell Bench Press is the cornerstone of chest training and one of the "Big Three" powerlifting movements. Lying flat on a bench, you lower a loaded barbell to your chest and press it back up explosively. It simultaneously recruits the pectorals, triceps, and anterior deltoids, making it the single most effective exercise for upper body pushing strength and chest mass development.

**Key cues:** Retract and depress your scapulae before unracking. Keep your feet flat on the floor, arch your lower back naturally, and maintain a shoulder-width grip. Lower the bar under control to mid-chest and drive up through the heels.

---

### 2 — Barbell Deadlift · Upper Legs / Back

<img src="images/0032-ila4NZS.jpg" width="320" />

> **Animation:** `videos/0032-ila4NZS.gif`
> **Equipment:** Barbell · **Target:** Glutes · **Secondary:** Hamstrings, Lower Back

The Barbell Deadlift is widely regarded as the ultimate full-body strength exercise. It engages virtually every major muscle in the posterior chain — glutes, hamstrings, and lower back — while also demanding significant contribution from the upper back, traps, and grip. Proper spinal alignment and bracing technique are critical for both performance and safety.

**Key cues:** Set up with the bar over your mid-foot. Hinge at the hips, grip just outside your legs, brace your core hard, and keep the bar in contact with your shins throughout the lift. Drive the floor away, lock out at the top by squeezing glutes and extending hips fully.

---

### 3 — Barbell Full Squat · Upper Legs

<img src="images/0043-qXTaZnJ.jpg" width="320" />

> **Animation:** `videos/0043-qXTaZnJ.gif`
> **Equipment:** Barbell · **Target:** Glutes · **Secondary:** Quadriceps, Hamstrings, Calves, Core

Often called "the king of all exercises," the Barbell Full Squat demands coordinated strength across the entire lower body and core. Breaking parallel maximizes glute and hamstring activation compared to partial squats. It is the foundation of nearly every strength and hypertrophy program.

**Key cues:** Bar on upper traps (high bar) or rear deltoids (low bar). Brace your core before descent, push knees out in line with toes, sit into your hips, and descend until your thighs pass parallel to the floor. Drive through the whole foot to stand.

---

### 4 — Dumbbell Biceps Curl · Upper Arms

<img src="images/0294-NbVPDMW.jpg" width="320" />

> **Animation:** `videos/0294-NbVPDMW.gif`
> **Equipment:** Dumbbell · **Target:** Biceps · **Secondary:** Forearms

The Dumbbell Biceps Curl is the most recognized isolation exercise for the arms. Training each side independently helps identify and correct strength imbalances between limbs. The supinated (palms-up) grip maximizes biceps contraction at the top of the movement.

**Key cues:** Stand tall with elbows pinned to your sides. Supinate your wrists as you curl up, squeeze at the top, and lower under control without swinging. Avoid using momentum from the shoulders or lower back.

---

### 5 — Pull-up · Back

<img src="images/0652-lBDjFxJ.jpg" width="320" />

> **Animation:** `videos/0652-lBDjFxJ.gif`
> **Equipment:** Body Weight · **Target:** Lats · **Secondary:** Biceps, Forearms

The Pull-up is the gold standard bodyweight exercise for upper body pulling strength. It primarily develops the latissimus dorsi — creating the coveted V-taper — while heavily involving the biceps, rear deltoids, and core stabilizers. It scales from beginner (band-assisted) to advanced (weighted).

**Key cues:** Dead hang from an overhand grip, shoulder-width or slightly wider. Initiate with your lats by depressing your shoulder blades, then pull your chest toward the bar. Lower fully between reps to maintain range of motion.

---

### 6 — Dumbbell Lateral Raise · Shoulders

<img src="images/0334-DsgkuIt.jpg" width="320" />

> **Animation:** `videos/0334-DsgkuIt.gif`
> **Equipment:** Dumbbell · **Target:** Delts · **Secondary:** Traps

The Dumbbell Lateral Raise is the go-to isolation exercise for building shoulder width. It directly targets the lateral (middle) head of the deltoid, which is responsible for the broad-shouldered look. Controlled tempo and strict form matter far more than load.

**Key cues:** Stand with a slight bend in your elbows throughout. Raise the dumbbells out to the sides until your arms are parallel to the floor — no higher. Lead with your elbows, not your wrists. Lower slowly under control to maximize time under tension.

---

## 🚀 Usage Examples

### Python — Load and Filter

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

# Access bilingual instructions
ex = exercises[0]
print(ex["instructions"]["en"])  # English
print(ex["instructions"]["tr"])  # Turkish
```

### Python — Load with Pandas

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

// Access bilingual instructions
const ex = exercises[0];
console.log(ex.instructions.en); // English
console.log(ex.instructions.tr); // Turkish
```

### TypeScript — Type-safe Usage

```typescript
interface Exercise {
  id: string;
  name: string;
  category: string;
  body_part: string;
  equipment: string;
  instructions: {
    en: string;
    tr: string;
  };
  muscle_group: string;
  secondary_muscles: string[];
  target: string;
  image: string;
  gif_url: string;
  created_at: string;
}

import exercises from "./data/exercises.json";
const data = exercises as Exercise[];

const shuffled = data.sort(() => Math.random() - 0.5);
const randomWorkout: Exercise[] = shuffled.slice(0, 6);
console.log("Random 6-exercise workout:", randomWorkout.map(e => e.name));
```

---

## 📄 License

This project is for **educational and non-commercial purposes only**.

- You **may** use this dataset for personal projects, research, and learning.
- You **may not** use this dataset or its media for any commercial application or product.
- All images and videos are property of their respective copyright holders.
- For commercial use, please contact the original content owners directly.

If you are a copyright holder and wish to have your content removed, please [open an issue](../../issues).
