# Exercises Dataset

**TR:** 433 farklı fitness egzersizine ait kapsamlı bir veri seti. Her egzersiz için ad, kategori, hedef kas grubu, ekipman bilgisi, açıklama, görsel ve animasyon videosu içermektedir.

**EN:** A comprehensive dataset of 433 fitness exercises. Each entry includes name, category, target muscle group, equipment, instructions, thumbnail image, and animation video.

---

## ⚠️ Yasal Uyarı / Disclaimer

> **TR:** Bu repo yalnızca eğitim ve araştırma amaçlıdır. Ticari kullanım kesinlikle yasaktır. Repodaki tüm görseller ve videolar ilgili telif hakkı sahiplerine aittir. İçeriklerinizin kaldırılmasını istiyorsanız lütfen bir issue açın.
>
> **EN:** This repository is provided for **educational and non-commercial purposes only**. All exercise media (images, videos) belong to their respective copyright holders. This dataset must not be used for commercial purposes. If you are the copyright owner and wish to have your content removed, please open an issue or contact the repository owner.

---

## 📂 Klasör Yapısı / File Structure

```
exercises-dataset/
├── data/
│   └── exercises.json   # 433 egzersizin tam veri seti / Full exercise dataset
├── images/              # Egzersiz görselleri (.jpg / .png) / Exercise thumbnails
├── videos/              # Egzersiz animasyon videoları (.mp4) / Exercise animation videos
└── README.md
```

---

## 📊 İstatistikler / Statistics

| | |
|---|---|
| Toplam Egzersiz / Total Exercises | **433** |
| Video Dosyası / Video Files | **372** |
| Görsel Dosyası / Image Files | **364** |

### Kategoriler / Categories

| Kategori / Category | Egzersiz Sayısı / Count |
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
| Diğer / Other | 73 |

### Ekipman / Equipment

| Ekipman / Equipment | Egzersiz Sayısı / Count |
|---|---|
| Machine | 138 |
| None (Bodyweight) | 103 |
| Barbell | 73 |
| Dumbbell | 69 |
| Resistance Band | 13 |
| Kettlebell | 11 |
| Other | 26 |

---

## 🎬 Örnek Egzersizler / Sample Exercises

Her egzersiz bir thumbnail görsel ve bir animasyon videosuna sahiptir.  
Each exercise has a thumbnail image and an animation video.

---

### 1 — Bench Press (Barbell) · Chest

![Bench Press](images/Barbell-Bench-Press_Chest_thumbnail.jpg)

> 📹 `videos/Barbell-Bench-Press_Chest.mp4`

**TR:** Barbell Bench Press, göğüs, omuz ve triceps kaslarını çalıştıran temel bir compound egzersizdir. Ağırlıklı göğüs gelişimi için en etkili hareketlerden biridir.

**EN:** The Barbell Bench Press is a fundamental compound exercise targeting the chest, shoulders, and triceps. It is one of the most effective movements for overall chest development.

---

### 2 — Deadlift (Barbell) · Hamstrings / Back

![Deadlift](images/Barbell-Deadlift_Hips-FIX_thumbnail.jpg)

> 📹 `videos/Barbell-Deadlift_Hips-FIX.mp4`

**TR:** Barbell Deadlift, arka zincir kaslarını (hamstring, glute, sırt alt) bütünsel olarak çalıştıran en temel güç egzersizlerinden biridir. Doğru form, bel sağlığı açısından kritiktir.

**EN:** The Barbell Deadlift is one of the most fundamental strength exercises, engaging the entire posterior chain (hamstrings, glutes, lower back). Proper form is critical for lower back safety.

---

### 3 — Full Squat (Barbell) · Quadriceps

![Squat](images/Barbell-Full-Squat_Thighs_thumbnail.jpg)

> 📹 `videos/Barbell-Full-Squat_Thighs.mp4`

**TR:** Barbell Full Squat, kuadriseps, hamstring ve glute kaslarını derinlemesine çalıştıran egzersizlerin kralıdır. Tüm vücut güç ve kas kütlesi gelişimi için temel harekettir.

**EN:** The Barbell Full Squat is considered the king of exercises, deeply engaging the quadriceps, hamstrings, and glutes. It is a cornerstone movement for total body strength and muscle mass development.

---

### 4 — Bicep Curl (Dumbbell) · Biceps

![Bicep Curl](images/Dumbbell-Biceps-Curl_Upper-Arms_thumbnail.jpg)

> 📹 `videos/Dumbbell-Biceps-Curl_Upper-Arms.mp4`

**TR:** Dumbbell Bicep Curl, biseps kaslarını izole eden klasik bir egzersizdir. Her iki kolu bağımsız çalıştırarak kas dengesini geliştirir ve kol hacmini artırır.

**EN:** The Dumbbell Bicep Curl is a classic isolation exercise targeting the biceps. Training each arm independently helps correct muscle imbalances and increases arm size.

---

### 5 — Pull-up · Back / Biceps

![Pull-up](images/Pull-up_Back_thumbnail@3x.jpg)

> 📹 `videos/Pull-up_Back.mp4`

**TR:** Pull-up, sırt ve biseps kaslarını çalıştıran en etkili vücut ağırlığı egzersizlerinden biridir. Latissimus dorsi kasını genişletir ve üst vücut çekme gücünü artırır.

**EN:** The Pull-up is one of the most effective bodyweight exercises for the back and biceps. It widens the latissimus dorsi and significantly improves upper body pulling strength.

---

### 6 — Jump Squat · Quadriceps / Cardio

![Jump Squat](images/Jump-Squat_Thighs_thumbnail@3x.jpg)

> 📹 `videos/Jump-Squat_Thighs.mp4`

**TR:** Jump Squat, kuadriseps, hamstring ve glute kaslarını patlayıcı şekilde çalıştıran bir pliometrik egzersizdir. Kardiyovasküler kapasiteyi artırırken güç ve hız gelişimine de katkı sağlar.

**EN:** The Jump Squat is a plyometric exercise that explosively engages the quadriceps, hamstrings, and glutes. It improves cardiovascular capacity while also developing power and speed.

---

## 🗂️ Veri Yapısı / Data Schema

`data/exercises.json` dosyasındaki her kayıt aşağıdaki alanları içermektedir:  
Each record in `data/exercises.json` contains the following fields:

| Alan / Field | Tür / Type | Açıklama / Description |
|---|---|---|
| `id` | string (UUID) | Egzersizin benzersiz kimliği / Unique exercise identifier |
| `name` | string | Egzersiz adı / Exercise name |
| `category` | string | Kas grubu kategorisi / Muscle group category |
| `equipment` | string | Kullanılan ekipman / Equipment used |
| `instructions` | string | Egzersiz açıklaması (TR) / Exercise instructions (TR) |
| `muscle_group` | string | İkincil kas grubu / Secondary muscle group |
| `target` | string | Birincil hedef kas / Primary target muscle |
| `image` | string | Görsel dosya yolu / Image file path |
| `gif_url` | string | Video dosya yolu / Video file path |
| `created_at` | string | Oluşturulma tarihi / Creation timestamp |

### Örnek Kayıt / Sample Record

```json
{
  "id": "166f0156-f963-44cc-8170-4041f649554e",
  "name": "Bicep Curl (Dumbbell)",
  "category": "biceps",
  "equipment": "Dumbbell",
  "instructions": "Bicep curl, özellikle üst koldaki biseps kaslarını güçlendiren temel bir izolasyon hareketidir...",
  "muscle_group": "forearms",
  "target": "Biceps",
  "image": "images/Dumbbell-Biceps-Curl_Upper-Arms_thumbnail.jpg",
  "gif_url": "videos/Dumbbell-Biceps-Curl_Upper-Arms.mp4",
  "created_at": "2025-03-05 08:27:36.029938+00"
}
```

---

## 🚀 Kullanım / Usage

### Python

```python
import json

with open("data/exercises.json", "r", encoding="utf-8") as f:
    exercises = json.load(f)

# Tüm göğüs egzersizlerini getir / Get all chest exercises
chest_exercises = [ex for ex in exercises if ex["category"] == "chest"]

print(f"Göğüs egzersizi sayısı: {len(chest_exercises)}")
# -> Göğüs egzersizi sayısı: 51
```

### JavaScript / Node.js

```js
const exercises = require("./data/exercises.json");

// Ekipmansız egzersizler / Bodyweight exercises
const bodyweight = exercises.filter(ex => ex.equipment === "None");

console.log(`Bodyweight egzersiz sayısı: ${bodyweight.length}`);
// -> Bodyweight egzersiz sayısı: 103
```

---

## 📄 Lisans / License

**TR:** Bu proje yalnızca **eğitim amaçlıdır**. Ticari kullanım için orijinal içerik sahipleriyle iletişime geçiniz.

**EN:** This project is for **educational purposes only**. For commercial use, please contact the original content owners.
