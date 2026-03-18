<div align="center">

# 💪 Exercises Dataset

<p>
  <img src="images/Barbell-Bench-Press_Chest_thumbnail.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/Barbell-Full-Squat_Thighs_thumbnail.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/Barbell-Deadlift_Hips-FIX_thumbnail.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/Dumbbell-Biceps-Curl_Upper-Arms_thumbnail.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/Pull-up_Back_thumbnail@3x.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/Jump-Squat_Thighs_thumbnail@3x.jpg" width="140" style="border-radius:8px; margin:4px;" />
</p>

**A comprehensive, ready-to-use fitness exercise dataset with 433 exercises — each with animation videos, thumbnail images, muscle group info, equipment data, and full instructions.**

[![Exercises](https://img.shields.io/badge/Exercises-433-blue?style=flat-square)](data/exercises.json)
[![Videos](https://img.shields.io/badge/Animation%20Videos-372-green?style=flat-square)](videos/)
[![Images](https://img.shields.io/badge/Thumbnails-364-orange?style=flat-square)](images/)
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
- [File Structure](#-file-structure)
- [Statistics](#-statistics)
- [Data Schema](#-data-schema)
- [Sample Exercises](#-sample-exercises)
- [Usage Examples](#-usage-examples)
- [License](#-license)

---

## 🔍 Overview

This dataset is a curated collection of **433 fitness exercises** sourced for educational and research purposes. It covers a wide range of muscle groups, equipment types, and exercise categories — making it ideal for:

- Building fitness or workout planning applications
- Machine learning projects involving exercise recognition or recommendation
- Health and wellness research
- Educational demonstrations and prototypes

Each exercise entry contains:

| Field | Description |
|---|---|
| Unique ID | UUID to identify each exercise |
| Name | Full descriptive exercise name |
| Category | Primary muscle group targeted |
| Target | Specific target muscle |
| Muscle Group | Secondary / supporting muscles |
| Equipment | Equipment required (or `None` for bodyweight) |
| Instructions | Step-by-step exercise instructions |
| Thumbnail | Static `.jpg` / `.png` preview image |
| Animation Video | `.mp4` animation showing the movement |

---

## 📂 File Structure

```
exercises-dataset/
├── data/
│   └── exercises.json       # Full dataset — 433 exercise records (JSON array)
├── images/                  # Exercise thumbnail images (.jpg / .png)
├── videos/                  # Exercise animation videos (.mp4)
└── README.md
```

### Key Files

- **`data/exercises.json`** — The primary data file. A JSON array of 433 exercise objects. Each record contains all metadata fields plus paths to the corresponding image and video files.
- **`images/`** — 364 thumbnail images. Files are named descriptively (e.g. `Barbell-Bench-Press_Chest_thumbnail.jpg`). Some exercises share a thumbnail with slightly different names (e.g. `@3x` suffix for higher resolution variants).
- **`videos/`** — 372 `.mp4` animation files demonstrating the exercise movement. Named consistently with the exercise name and category (e.g. `Barbell-Bench-Press_Chest.mp4`).

---

## 📊 Statistics

| Metric | Count |
|---|---|
| Total Exercises | **433** |
| Animation Videos | **372** |
| Thumbnail Images | **364** |

### Exercises by Category (Muscle Group)

| Category | Exercise Count |
|---|---|
| Quadriceps | 53 |
| Chest | 51 |
| Abdominals | 48 |
| Full Body | 41 |
| Shoulders | 34 |
| Biceps | 32 |
| Triceps | 28 |
| Cardio | 22 |
| Hamstrings | 21 |
| Glutes | 19 |
| Calves | 11 |
| Back | ~31 |
| Other | ~42 |

### Exercises by Equipment

| Equipment | Exercise Count |
|---|---|
| Machine | 138 |
| None (Bodyweight) | 103 |
| Barbell | 73 |
| Dumbbell | 69 |
| Resistance Band | 13 |
| Kettlebell | 11 |
| Other | 26 |

> **Note:** ~24% of exercises require no equipment at all — great for at-home workout applications.

---

## 🗂️ Data Schema

Each record in `data/exercises.json` follows this structure:

| Field | Type | Description |
|---|---|---|
| `id` | `string` (UUID) | Unique identifier for the exercise |
| `name` | `string` | Full exercise name (e.g. `"Bicep Curl (Dumbbell)"`) |
| `category` | `string` | Muscle group category (lowercase, e.g. `"chest"`, `"biceps"`) |
| `equipment` | `string` | Required equipment (e.g. `"Barbell"`, `"None"`) |
| `instructions` | `string` | Detailed step-by-step instructions |
| `muscle_group` | `string` | Secondary / synergist muscle group |
| `target` | `string` | Primary target muscle (e.g. `"Biceps"`, `"Pectoralis Major"`) |
| `image` | `string` | Relative path to the thumbnail image file |
| `gif_url` | `string` | Relative path to the animation video file (`.mp4`) |
| `created_at` | `string` | ISO 8601 timestamp of record creation |

### Sample Record

```json
{
  "id": "166f0156-f963-44cc-8170-4041f649554e",
  "name": "Bicep Curl (Dumbbell)",
  "category": "biceps",
  "equipment": "Dumbbell",
  "instructions": "Stand upright holding a dumbbell in each hand at arm's length. Keep your elbows close to your torso and rotate the palms of your hands until they are facing forward. Curl the weights while contracting your biceps, exhaling as you raise. Continue until your biceps are fully contracted and the dumbbells are at shoulder level. Hold briefly, then lower back down under control.",
  "muscle_group": "forearms",
  "target": "Biceps",
  "image": "images/Dumbbell-Biceps-Curl_Upper-Arms_thumbnail.jpg",
  "gif_url": "videos/Dumbbell-Biceps-Curl_Upper-Arms.mp4",
  "created_at": "2025-03-05 08:27:36.029938+00"
}
```

---

## 🎬 Sample Exercises

Each exercise below includes a thumbnail preview. The corresponding animation video (`.mp4`) is located in the `videos/` folder.

---

### 1 — Barbell Bench Press · Chest

<img src="images/Barbell-Bench-Press_Chest_thumbnail.jpg" width="320" />

> **Animation:** `videos/Barbell-Bench-Press_Chest.mp4`  
> **Equipment:** Barbell · **Target:** Pectoralis Major · **Secondary:** Shoulders, Triceps

The Barbell Bench Press is the cornerstone of chest training and one of the "Big Three" powerlifting movements. Lying flat on a bench, you lower a loaded barbell to your chest and press it back up explosively. It simultaneously recruits the pectoralis major, anterior deltoids, and triceps brachii, making it the single most effective exercise for upper body pushing strength and chest mass development.

**Key cues:** Retract and depress your scapulae before unracking. Keep your feet flat on the floor, arch your lower back naturally, and maintain a shoulder-width grip. Lower the bar under control to mid-chest and drive up through the heels.

---

### 2 — Barbell Deadlift · Hamstrings / Back

<img src="images/Barbell-Deadlift_Hips-FIX_thumbnail.jpg" width="320" />

> **Animation:** `videos/Barbell-Deadlift_Hips-FIX.mp4`  
> **Equipment:** Barbell · **Target:** Hamstrings, Glutes · **Secondary:** Erector Spinae, Traps, Forearms

The Barbell Deadlift is widely regarded as the ultimate full-body strength exercise. It engages virtually every major muscle in the posterior chain — hamstrings, glutes, and lower back — while also demanding significant contribution from the upper back, traps, and grip. Proper spinal alignment and bracing technique are critical for both performance and safety.

**Key cues:** Set up with the bar over your mid-foot. Hinge at the hips, grip just outside your legs, brace your core hard, and keep the bar in contact with your shins throughout the lift. Drive the floor away, lock out at the top by squeezing glutes and extending hips fully.

---

### 3 — Barbell Full Squat · Quadriceps

<img src="images/Barbell-Full-Squat_Thighs_thumbnail.jpg" width="320" />

> **Animation:** `videos/Barbell-Full-Squat_Thighs.mp4`  
> **Equipment:** Barbell · **Target:** Quadriceps · **Secondary:** Glutes, Hamstrings, Core

Often called "the king of all exercises," the Barbell Full Squat demands coordinated strength across the entire lower body and core. Breaking parallel maximizes glute and hamstring activation compared to partial squats. It is the foundation of nearly every strength and hypertrophy program.

**Key cues:** Bar on upper traps (high bar) or rear deltoids (low bar). Brace your core before descent, push knees out in line with toes, sit into your hips, and descend until your thighs pass parallel to the floor. Drive through the whole foot to stand.

---

### 4 — Dumbbell Bicep Curl · Biceps

<img src="images/Dumbbell-Biceps-Curl_Upper-Arms_thumbnail.jpg" width="320" />

> **Animation:** `videos/Dumbbell-Biceps-Curl_Upper-Arms.mp4`  
> **Equipment:** Dumbbell · **Target:** Biceps Brachii · **Secondary:** Brachialis, Forearms

The Dumbbell Bicep Curl is the most recognized isolation exercise for the arms. Training each side independently helps identify and correct strength imbalances between limbs. The supinated (palms-up) grip maximizes biceps contraction at the top of the movement.

**Key cues:** Stand tall with elbows pinned to your sides. Supinate your wrists as you curl up, squeeze at the top, and lower under control without swinging. Avoid using momentum from the shoulders or lower back.

---

### 5 — Pull-up · Back / Biceps

<img src="images/Pull-up_Back_thumbnail@3x.jpg" width="320" />

> **Animation:** `videos/Pull-up_Back.mp4`  
> **Equipment:** None (bodyweight) · **Target:** Latissimus Dorsi · **Secondary:** Biceps, Rear Delts, Core

The Pull-up is the gold standard bodyweight exercise for upper body pulling strength. It primarily develops the latissimus dorsi — creating the coveted V-taper — while heavily involving the biceps, rear deltoids, and core stabilizers. It scales from beginner (band-assisted) to advanced (weighted).

**Key cues:** Dead hang from an overhand grip, shoulder-width or slightly wider. Initiate with your lats by depressing your shoulder blades, then pull your chest toward the bar. Lower fully between reps to maintain range of motion.

---

### 6 — Jump Squat · Quadriceps / Cardio

<img src="images/Jump-Squat_Thighs_thumbnail@3x.jpg" width="320" />

> **Animation:** `videos/Jump-Squat_Thighs.mp4`  
> **Equipment:** None (bodyweight) · **Target:** Quadriceps, Glutes · **Secondary:** Hamstrings, Calves, Core

The Jump Squat is a plyometric power exercise that trains the explosive strength of the lower body. It elevates heart rate rapidly, making it equally effective as a cardiovascular drill and a power development tool. Used in HIIT, athletic conditioning, and circuit training.

**Key cues:** Descend into a half-squat position, then explode upward as powerfully as possible. Land softly with slightly bent knees to absorb impact, immediately transitioning into the next rep. Keep your chest up throughout.

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
# -> Chest exercises: 51

# Filter by equipment
bodyweight = [ex for ex in exercises if ex["equipment"] == "None"]
print(f"Bodyweight exercises: {len(bodyweight)}")
# -> Bodyweight exercises: 103

# Get all unique categories
categories = sorted({ex["category"] for ex in exercises})
print("Categories:", categories)
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

# All barbell exercises targeting quadriceps
barbell_quads = df[(df["equipment"] == "Barbell") & (df["category"] == "quadriceps")]
print(barbell_quads[["name", "target", "equipment"]])
```

### JavaScript / Node.js

```js
const exercises = require("./data/exercises.json");

console.log(`Total exercises: ${exercises.length}`);

// Bodyweight exercises only
const bodyweight = exercises.filter(ex => ex.equipment === "None");
console.log(`Bodyweight exercises: ${bodyweight.length}`);
// -> Bodyweight exercises: 103

// Group exercises by category
const byCategory = exercises.reduce((acc, ex) => {
  acc[ex.category] = (acc[ex.category] || []);
  acc[ex.category].push(ex);
  return acc;
}, {});

console.log("Categories:", Object.keys(byCategory));
```

### TypeScript — Type-safe Usage

```typescript
interface Exercise {
  id: string;
  name: string;
  category: string;
  equipment: string;
  instructions: string;
  muscle_group: string;
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
- All images and videos are property of their respective copyright owners.
- For commercial use, please contact the original content owners directly.

If you are a copyright holder and wish to have your content removed, please [open an issue](../../issues).
