<div align="center">

# 💪 Exercises Dataset

<<<<<<< HEAD
<p>
  <img src="images/0025-EIeI8Vf.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/0043-qXTaZnJ.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/0032-ila4NZS.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/0294-NbVPDMW.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/0652-lBDjFxJ.jpg" width="140" style="border-radius:8px; margin:4px;" />
  <img src="images/0334-DsgkuIt.jpg" width="140" style="border-radius:8px; margin:4px;" />
</p>

**A comprehensive, ready-to-use fitness exercise dataset with 1,324 exercises — each with animation GIFs, thumbnail images, muscle group info, equipment data, and full multilingual instructions (English, Spanish, Italian, Turkish).**

[![Exercises](https://img.shields.io/badge/Exercises-1324-blue?style=flat-square)](data/exercises.json)
[![Videos](https://img.shields.io/badge/Animation%20GIFs-1324-green?style=flat-square)](videos/)
[![Images](https://img.shields.io/badge/Thumbnails-1324-orange?style=flat-square)](images/)
[![License](https://img.shields.io/badge/License-Educational%20Only-red?style=flat-square)](#-license)
=======
**A developer setup wizard + structured, multilingual exercise dataset — scaffold your own exercise app backend (DB schema, API code, LLM prompt) over 1,324 exercises with category, body-part, equipment, target and muscle-group data and step-by-step instructions in 6 languages (English, Spanish, Italian, Turkish, Russian, Chinese). Exercise media is not included.**

[![Exercises](https://img.shields.io/badge/Exercises-1324-blue?style=flat-square)](data/exercises.json)
[![Languages](https://img.shields.io/badge/Languages-6-green?style=flat-square)](#-overview)
[![Format](https://img.shields.io/badge/Format-JSON-orange?style=flat-square)](data/exercises.json)
[![Media](https://img.shields.io/badge/Media-not%20included-lightgrey?style=flat-square)](#-notice--exercise-media-is-not-included)
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

</div>

---

<<<<<<< HEAD
## ⚠️ Disclaimer

> This repository is provided for **educational and non-commercial research purposes only**.
> All exercise media (images, videos) belong to their respective copyright holders.
> **Commercial use is strictly prohibited.**
> If you are a copyright owner and wish to have your content removed, please [open an issue](../../issues) or contact the repository owner.
=======
## ⚠️ Notice — exercise media is not included

> **This repository is a developer setup wizard and structured exercise dataset.** The exercise **media (thumbnail images and animation GIFs) is not included here.**
>
> There are **multiple, conflicting ownership claims** over this media, so it is **not redistributed in this repository.** Each record keeps a `media_id` (the original ExerciseDB media reference); the dataset itself ships exercise metadata and multilingual instruction translations (EN, ES, IT, TR, RU, ZH).
>
> **If you are the rights holder of this media, please [open an issue](../../issues) or contact the maintainer.**
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

---

## 📦 Data Source & Attribution

<<<<<<< HEAD
The exercise **media (images & animation GIFs)** and the **base exercise data** in this repository
originate from **[ExerciseDB v1 by AscendAPI](https://oss.exercisedb.dev)** ([API docs](https://oss.exercisedb.dev/docs)).

Each media file is named `{index}-{exerciseId}.{ext}`, where `exerciseId` is the original ExerciseDB v1 id.
The same asset is served from AscendAPI's CDN — e.g. [`static.exercisedb.dev/media/EIeI8Vf.gif`](https://static.exercisedb.dev/media/EIeI8Vf.gif)
is byte-for-byte identical to this repo's `videos/0025-EIeI8Vf.gif`. The assets were obtained via a
[Kaggle re-host by *omarxadel*](https://www.kaggle.com/datasets/omarxadel/fitness-exercises-dataset).

**Added in this repository** on top of the original ExerciseDB data:

- 🇪🇸 Spanish, 🇮🇹 Italian, 🇹🇷 Turkish and 🇸🇦 Arabic translations of the instructions
- the interactive browser (`index.html`) and developer setup guide (`setup.html`)
- formatting, cleanup, and 1:1 media alignment

> **License & credit:** The exercise media and base data belong to **AscendAPI / ExerciseDB** — please review
> [ExerciseDB's terms](https://oss.exercisedb.dev/docs) before any reuse. Everything here is provided for
> **educational, non-commercial use only**. Original-source attribution was added following issue [#5](../../issues/5)
> (thanks to [@shinkaidev](https://github.com/shinkaidev) for the report). If you are a rights holder and want your
> content removed, please [open an issue](../../issues).
=======
The base exercise **data** in this repository originates from **[ExerciseDB v1 by AscendAPI](https://oss.exercisedb.dev)** ([API docs](https://oss.exercisedb.dev/docs)), obtained via a [Kaggle re-host by *omarxadel*](https://www.kaggle.com/datasets/omarxadel/fitness-exercises-dataset).

The associated **media (images & animation GIFs) is _not_ included** in this repository — see the [notice](#-notice--exercise-media-is-not-included) above. Each record's `media_id` is the original ExerciseDB v1 media id (e.g. `2gPfomN`); the official CDN serves the corresponding asset at `static.exercisedb.dev/media/{media_id}.gif` for anyone entitled to use it.

**Added in this repository** on top of the base data:

- 🇪🇸 Spanish, 🇮🇹 Italian, 🇹🇷 Turkish, 🇷🇺 Russian, 🇨🇳 Chinese and 🇸🇦 Arabic translations of the instructions
- the interactive browser (`index.html`) and developer setup guide (`setup.html`)
- formatting and cleanup

> Original-source attribution was added following issue [#5](../../issues/5) (thanks to [@shinkaidev](https://github.com/shinkaidev) for the report). If you are a rights holder and want anything removed or clarified, please [open an issue](../../issues).
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

---

## 📋 Table of Contents

- [Data Source & Attribution](#-data-source--attribution)
- [Overview](#-overview)
- [Interactive Browser & Developer Setup](#-interactive-browser--developer-setup)
- [File Structure](#-file-structure)
- [Statistics](#-statistics)
- [Data Schema](#-data-schema)
- [Sample Exercises](#-sample-exercises)
- [Usage Examples](#-usage-examples)
<<<<<<< HEAD
- [License](#-license)
=======
- [License & Use](#-license--use)
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

---

## 🔍 Overview

<<<<<<< HEAD
This dataset is a curated collection of **1,324 fitness exercises** sourced for educational and research purposes. It covers a wide range of muscle groups, equipment types, and exercise categories — making it ideal for:
=======
This dataset is a curated collection of **1,324 fitness exercises** for educational and research purposes. It covers a wide range of muscle groups, equipment types, and exercise categories — making it ideal for:
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

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
| Instructions | Step-by-step instructions for each exercise |
<<<<<<< HEAD
| Available Languages | 🇬🇧 English · 🇪🇸 Spanish · 🇮🇹 Italian · 🇹🇷 Turkish · 🇸🇦 Arabic |
| Thumbnail | Static `.jpg` preview image |
| Animation GIF | `.gif` animation showing the movement |
=======
| Available Languages | 🇬🇧 English · 🇪🇸 Spanish · 🇮🇹 Italian · 🇹🇷 Turkish · 🇷🇺 Russian · 🇨🇳 Chinese · 🇸🇦 Arabic |
| Media ID | Reference id of the original ExerciseDB media (the media itself is **not** bundled — see [notice](#-notice--exercise-media-is-not-included)) |
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

---

## 🖥️ Interactive Browser & Developer Setup

This repository includes two ready-to-use HTML tools — no server required, just open in a browser.

<<<<<<< HEAD
=======
> **Note:** since the media is not bundled, the browser displays exercise **metadata and instructions** only; thumbnail and GIF slots are empty.

>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
### `index.html` — Exercise Browser

A fully client-side exercise explorer with:
- Live search across all 1,324 exercises
- Filter by category, equipment, and target muscle
<<<<<<< HEAD
- Infinite scroll grid with thumbnail previews
- Click any card to see full details, GIF animation, and instructions in English, Spanish, Italian, or Turkish
=======
- Infinite scroll grid
- Click any card to see full details and instructions in English, Spanish, Italian, Turkish, Russian, or Chinese
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

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
<<<<<<< HEAD
├── images/                  # Exercise thumbnail images (.jpg) — 1,324 files
├── videos/                  # Exercise animation GIFs (.gif) — 1,324 files
=======
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
├── index.html               # Interactive exercise browser (client-side, no server needed)
├── setup.html               # Developer setup guide (DB import + API integration)
└── README.md
```

### Key Files

<<<<<<< HEAD
- **`data/exercises.json`** — The primary data file. A JSON array of 1,324 exercise objects with all metadata and paths to corresponding media files.
- **`images/`** — 1,324 thumbnail JPGs named with the exercise ID (e.g. `0001-2gPfomN.jpg`).
- **`videos/`** — 1,324 GIF animations demonstrating each movement (e.g. `0001-2gPfomN.gif`).
- **`index.html`** — Standalone exercise browser. Open directly in any modern browser.
- **`setup.html`** — Developer guide for DB setup, API integration, and LLM-assisted backend generation.

=======
- **`data/exercises.json`** — The primary data file. A JSON array of 1,324 exercise objects with all metadata. The `image` and `gif_url` fields are `null`; `media_id` holds the original ExerciseDB media reference.
- **`index.html`** — Standalone exercise browser. Open directly in any modern browser.
- **`setup.html`** — Developer guide for DB setup, API integration, and LLM-assisted backend generation.

> **Media** (`images/`, `videos/`) is intentionally **not** part of this repository — see the [notice](#-notice--exercise-media-is-not-included).

>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
---

## 📊 Statistics

| Metric | Count |
|---|---|
| Total Exercises | **1,324** |
<<<<<<< HEAD
| Animation GIFs | **1,324** |
| Thumbnail Images | **1,324** |
=======
| Instruction Languages | **6** |
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

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
| `instructions.es` | `string` | Full step-by-step instructions in Spanish |
| `instructions.it` | `string` | Full step-by-step instructions in Italian |
| `instructions.tr` | `string` | Full step-by-step instructions in Turkish |
<<<<<<< HEAD
| `muscle_group` | `string` | Primary synergist muscle group |
| `secondary_muscles` | `array[string]` | Additional muscles involved |
| `target` | `string` | Primary target muscle (e.g. `"biceps"`, `"pectoralis major"`) |
| `image` | `string` | Relative path to the thumbnail image (e.g. `"images/0001-2gPfomN.jpg"`) |
| `gif_url` | `string` | Relative path to the animation GIF (e.g. `"videos/0001-2gPfomN.gif"`) |
=======
| `instructions.ru` | `string` | Full step-by-step instructions in Russian |
| `instructions.zh` | `string` | Full step-by-step instructions in Chinese |
| `muscle_group` | `string` | Primary synergist muscle group |
| `secondary_muscles` | `array[string]` | Additional muscles involved |
| `target` | `string` | Primary target muscle (e.g. `"biceps"`, `"pectoralis major"`) |
| `media_id` | `string` | Original ExerciseDB media reference id (e.g. `"2gPfomN"`) — media not bundled |
| `image` | `null` | Reserved for a thumbnail path; `null` (media not included) |
| `gif_url` | `null` | Reserved for an animation path; `null` (media not included) |
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
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
<<<<<<< HEAD
    "es": "Túmbate sobre tu espalda con las rodillas flexionadas y los pies apoyados en el suelo. Coloca las manos detrás de la cabeza con los codos apuntando hacia afuera. Activando el abdomen, levanta lentamente la parte superior del cuerpo del suelo, curvándote hacia adelante hasta que tu torso forme un ángulo de 45 grados. Haz una pausa por un momento en la parte superior, luego baja lentamente la parte superior del cuerpo de vuelta a la posición inicial. Repite el número de repeticiones deseado.",
    "it": "Sdraiati sulla schiena con le ginocchia piegate e i piedi appoggiati a terra. Metti le mani dietro la testa con i gomiti rivolti verso l'esterno. Coinvolgendo gli addominali, solleva lentamente la parte superiore del corpo da terra, piegandoti in avanti finché il busto non forma un angolo di 45 gradi. Fermati per un momento in alto, quindi abbassa lentamente la parte superiore del corpo fino alla posizione di partenza. Ripetere per il numero di ripetizioni desiderato.",
    "tr": "Sırt üstü yatın, dizlerinizi bükün ve ayaklarınızı yere düz koyun. Ellerinizi başınızın arkasına, dirsekleriniz dışa bakacak şekilde yerleştirin. Karın kaslarınızı kasarak üst vücudunuzu yerden kaldırın ve gövdeniz 45 derecelik açıya gelene kadar öne doğru kıvırın. Bir an için bu pozisyonda bekleyin, ardından yavaşça başlangıç konumuna geri dönün. İstenen tekrar sayısı için hareketi tekrarlayın."
=======
    "es": "Túmbate sobre tu espalda con las rodillas flexionadas y los pies apoyados en el suelo. ...",
    "it": "Sdraiati sulla schiena con le ginocchia piegate e i piedi appoggiati a terra. ...",
    "tr": "Sırt üstü yatın, dizlerinizi bükün ve ayaklarınızı yere düz koyun. ...",
    "ru": "Лягте на спину, согните колени и поставьте ступни на землю. ...",
    "zh": "平躺，膝盖弯曲，双脚平放在地上。..."
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
  },
  "muscle_group": "hip flexors",
  "secondary_muscles": ["hip flexors", "lower back"],
  "target": "abs",
<<<<<<< HEAD
  "image": "images/0001-2gPfomN.jpg",
  "gif_url": "videos/0001-2gPfomN.gif",
  "created_at": "2026-03-18 12:31:32.854798+00:00"
=======
  "media_id": "2gPfomN",
  "image": null,
  "gif_url": null,
  "created_at": "2026-03-18T12:31:32.854798+00:00"
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
}
```

---

## 🎬 Sample Exercises

<<<<<<< HEAD
---

### 1 — Barbell Bench Press · Chest

<img src="images/0025-EIeI8Vf.jpg" width="320" />

> **Animation:** `videos/0025-EIeI8Vf.gif`
> **Equipment:** Barbell · **Target:** Pectorals · **Secondary:** Triceps, Shoulders
=======
> Media is not bundled (see [notice](#-notice--exercise-media-is-not-included)); the `media_id` of each example is shown for reference.

### 1 — Barbell Bench Press · Chest

> **Equipment:** Barbell · **Target:** Pectorals · **Secondary:** Triceps, Shoulders · **Media ID:** `EIeI8Vf`
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

The Barbell Bench Press is the cornerstone of chest training and one of the "Big Three" powerlifting movements. Lying flat on a bench, you lower a loaded barbell to your chest and press it back up explosively. It simultaneously recruits the pectorals, triceps, and anterior deltoids, making it the single most effective exercise for upper body pushing strength and chest mass development.

**Key cues:** Retract and depress your scapulae before unracking. Keep your feet flat on the floor, arch your lower back naturally, and maintain a shoulder-width grip. Lower the bar under control to mid-chest and drive up through the heels.

<<<<<<< HEAD
---

### 2 — Barbell Deadlift · Upper Legs / Back

<img src="images/0032-ila4NZS.jpg" width="320" />

> **Animation:** `videos/0032-ila4NZS.gif`
> **Equipment:** Barbell · **Target:** Glutes · **Secondary:** Hamstrings, Lower Back
=======
### 2 — Barbell Deadlift · Upper Legs / Back

> **Equipment:** Barbell · **Target:** Glutes · **Secondary:** Hamstrings, Lower Back · **Media ID:** `ila4NZS`
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

The Barbell Deadlift is widely regarded as the ultimate full-body strength exercise. It engages virtually every major muscle in the posterior chain — glutes, hamstrings, and lower back — while also demanding significant contribution from the upper back, traps, and grip. Proper spinal alignment and bracing technique are critical for both performance and safety.

**Key cues:** Set up with the bar over your mid-foot. Hinge at the hips, grip just outside your legs, brace your core hard, and keep the bar in contact with your shins throughout the lift. Drive the floor away, lock out at the top by squeezing glutes and extending hips fully.

<<<<<<< HEAD
---

### 3 — Barbell Full Squat · Upper Legs

<img src="images/0043-qXTaZnJ.jpg" width="320" />

> **Animation:** `videos/0043-qXTaZnJ.gif`
> **Equipment:** Barbell · **Target:** Glutes · **Secondary:** Quadriceps, Hamstrings, Calves, Core
=======
### 3 — Barbell Full Squat · Upper Legs

> **Equipment:** Barbell · **Target:** Glutes · **Secondary:** Quadriceps, Hamstrings, Calves, Core · **Media ID:** `qXTaZnJ`
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

Often called "the king of all exercises," the Barbell Full Squat demands coordinated strength across the entire lower body and core. Breaking parallel maximizes glute and hamstring activation compared to partial squats. It is the foundation of nearly every strength and hypertrophy program.

**Key cues:** Bar on upper traps (high bar) or rear deltoids (low bar). Brace your core before descent, push knees out in line with toes, sit into your hips, and descend until your thighs pass parallel to the floor. Drive through the whole foot to stand.

<<<<<<< HEAD
---

### 4 — Dumbbell Biceps Curl · Upper Arms

<img src="images/0294-NbVPDMW.jpg" width="320" />

> **Animation:** `videos/0294-NbVPDMW.gif`
> **Equipment:** Dumbbell · **Target:** Biceps · **Secondary:** Forearms
=======
### 4 — Dumbbell Biceps Curl · Upper Arms

> **Equipment:** Dumbbell · **Target:** Biceps · **Secondary:** Forearms · **Media ID:** `NbVPDMW`
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

The Dumbbell Biceps Curl is the most recognized isolation exercise for the arms. Training each side independently helps identify and correct strength imbalances between limbs. The supinated (palms-up) grip maximizes biceps contraction at the top of the movement.

**Key cues:** Stand tall with elbows pinned to your sides. Supinate your wrists as you curl up, squeeze at the top, and lower under control without swinging. Avoid using momentum from the shoulders or lower back.

<<<<<<< HEAD
---

### 5 — Pull-up · Back

<img src="images/0652-lBDjFxJ.jpg" width="320" />

> **Animation:** `videos/0652-lBDjFxJ.gif`
> **Equipment:** Body Weight · **Target:** Lats · **Secondary:** Biceps, Forearms
=======
### 5 — Pull-up · Back

> **Equipment:** Body Weight · **Target:** Lats · **Secondary:** Biceps, Forearms · **Media ID:** `lBDjFxJ`
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

The Pull-up is the gold standard bodyweight exercise for upper body pulling strength. It primarily develops the latissimus dorsi — creating the coveted V-taper — while heavily involving the biceps, rear deltoids, and core stabilizers. It scales from beginner (band-assisted) to advanced (weighted).

**Key cues:** Dead hang from an overhand grip, shoulder-width or slightly wider. Initiate with your lats by depressing your shoulder blades, then pull your chest toward the bar. Lower fully between reps to maintain range of motion.

<<<<<<< HEAD
---

### 6 — Dumbbell Lateral Raise · Shoulders

<img src="images/0334-DsgkuIt.jpg" width="320" />

> **Animation:** `videos/0334-DsgkuIt.gif`
> **Equipment:** Dumbbell · **Target:** Delts · **Secondary:** Traps
=======
### 6 — Dumbbell Lateral Raise · Shoulders

> **Equipment:** Dumbbell · **Target:** Delts · **Secondary:** Traps · **Media ID:** `DsgkuIt`
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c

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

# Access multilingual instructions
ex = exercises[0]
print(ex["instructions"]["en"])  # English
print(ex["instructions"]["es"])  # Spanish
print(ex["instructions"]["it"])  # Italian
print(ex["instructions"]["tr"])  # Turkish
<<<<<<< HEAD
=======
print(ex["instructions"]["ru"])  # Russian
print(ex["instructions"]["zh"])  # Chinese
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
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

// Access multilingual instructions
const ex = exercises[0];
console.log(ex.instructions.en); // English
console.log(ex.instructions.es); // Spanish
console.log(ex.instructions.it); // Italian
console.log(ex.instructions.tr); // Turkish
<<<<<<< HEAD
=======
console.log(ex.instructions.ru); // Russian
console.log(ex.instructions.zh); // Chinese
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
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
    es: string;
    it: string;
    tr: string;
<<<<<<< HEAD
=======
    ru: string;
    zh: string;
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
  };
  muscle_group: string;
  secondary_muscles: string[];
  target: string;
<<<<<<< HEAD
  image: string;
  gif_url: string;
=======
  media_id: string | null;
  image: string | null;
  gif_url: string | null;
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
  created_at: string;
}

import exercises from "./data/exercises.json";
const data = exercises as Exercise[];

<<<<<<< HEAD
const shuffled = data.sort(() => Math.random() - 0.5);
const randomWorkout: Exercise[] = shuffled.slice(0, 6);
console.log("Random 6-exercise workout:", randomWorkout.map(e => e.name));
=======
const randomWorkout: Exercise[] = data.slice(0, 6);
console.log("First 6 exercises:", randomWorkout.map(e => e.name));
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
```

---

<<<<<<< HEAD
## 📄 License

This project is for **educational and non-commercial purposes only**.

- You **may** use this dataset for personal projects, research, and learning.
- You **may not** use this dataset or its media for any commercial application or product.
- All images and videos are property of their respective copyright holders.
- For commercial use, please contact the original content owners directly.

> **Data source:** Media and base exercise data originate from [ExerciseDB v1 by AscendAPI](https://oss.exercisedb.dev) (obtained via a [Kaggle re-host](https://www.kaggle.com/datasets/omarxadel/fitness-exercises-dataset)) — see the [Data Source & Attribution](#-data-source--attribution) section above and [ExerciseDB's terms](https://oss.exercisedb.dev/docs) for reuse.

If you are a copyright holder and wish to have your content removed, please [open an issue](../../issues).
=======
## 📄 License & Use

This repository is a **developer setup wizard and structured exercise dataset** — exercise metadata and multilingual instruction translations. Exercise media is **not included**.

- The base exercise data originates from **ExerciseDB v1** (see [Data Source & Attribution](#-data-source--attribution)); review [ExerciseDB's terms](https://oss.exercisedb.dev/docs) before any reuse.
- **Exercise media (images & GIFs) is not included** in this repository — see the [notice](#-notice--exercise-media-is-not-included).
- This repository does **not** claim ownership of the underlying exercise content.
- If you are a rights holder and wish to have anything removed or clarified, please [open an issue](../../issues) or contact the maintainer.
>>>>>>> 225b17d6fe25f00fb80a5dcb60ba428b7332824c
