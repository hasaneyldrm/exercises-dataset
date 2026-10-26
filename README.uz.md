# O‘zbek tili / Uzbek language support

This repository has an **Uzbek (Latin script, `uz`) localization overlay** for the exercise dataset. It is additive: the original `data/exercises.json` and other 10 languages stay unchanged.

## Current translation coverage

- **1,324/1,324 exercises:** `category_uz`, `body_part_uz`, `equipment_uz`, `muscle_group_uz`, `target_uz`, `secondary_muscles_uz` available in `data/exercises_uz.json`.
- **2/1,324 exercises:** reviewed `name_uz`, `instructions_uz` and `instruction_steps_uz` (IDs `0001` and `0002`).
- **1,322/1,324 exercises:** machine-translated (Gemini 3.8 Flash, EN→UZ) `name_uz`, `instructions_uz` and `instruction_steps_uz`; not yet reviewed by a native speaker.
- **1,322 exercise names and instructions still need translation and review.** The uploaded archive included only two examples, not a full translation. Do **not** advertise 11 complete instruction languages yet.

## Files

- `data/uzbek_dictionary.json`: Uzbek labels for the complete set of source categories, equipment and muscles, plus user-interface strings.
- `data/exercises_uz.json`: one row per source exercise, keyed by `id`, with localized metadata and any reviewed name/step text.
- `data/exercises_uz_sample.json`: two sample records **derived from the actual source dataset** with added Uzbek strings. The original archive's samples had incompatible `name`, `instructions` and `instruction_steps` types.
- `data/exercises.schema.json`: optional `_uz` fields and `uz` language keys; original fields and 10 required languages are preserved.
- `scripts/add_uzbek_to_dataset.py`: merge the overlay with the source dataset; can optionally machine-translate missing names and instructions.

## Merge reviewed content (offline; no API)

Run from the repository root:

```bash
python3 scripts/add_uzbek_to_dataset.py --mode offline \
  --input data/exercises.json --output data/exercises-with-uz.json
```

This adds all metadata translations and the two reviewed exercises. It does **not** invent translations for missing instructions. To write into the existing file, set `--output data/exercises.json` (uses atomic replacement).

## Generate a machine-translated draft (online)

```bash
python3 scripts/add_uzbek_to_dataset.py --mode auto \
  --input data/exercises.json --output data/exercises-with-uz.json \
  --require-complete
```

The online mode uses the unofficial Google Translate endpoint, which may be throttled, blocked or unavailable. It uses a local cache at `data/uz_translation_cache.json` and retries failed requests; failures abort rather than silently mixing English with Uzbek. Machine translations, especially exercise technique and safety instructions, **must be reviewed by a proficient Uzbek speaker** before merging into the published dataset. No translation service, quality guarantee, or automatic full translation is bundled in this repo.

## Integration

Join the two JSON arrays by `id`. Apply `*_uz` metadata values from the overlay; for records with `instruction_steps_uz` and `instructions_uz`, map them to `instruction_steps.uz` and `instructions.uz` respectively. `name_uz` stays a separate field because `name` is a **string**, not a language dictionary.

Do not replace the original `name` with an object, or write step arrays into `instructions.uz`. These were breaking bugs in the original ZIP script/schema.

## Dictionary fixes

The original archive used `thighs` and `skierg`, while the source contains `upper legs` and `skierg machine`. The corrected dictionary also includes `elliptical machine`, `stepmill machine`, `tire` and `upper body ergometer`. The sample translations have been adapted to the *actual* English instructions, with Latin Uzbek characters throughout.
