---
name: find-fitness-exercises
description: Search the hasaneyldrm/exercises-dataset collection for fitness exercises by natural-language query, body part, equipment, target muscle, or supporting muscle, then return concise reference examples with multilingual steps, thumbnails, animation GIFs, source links, and attribution. Use when a user asks to find, compare, identify, or demonstrate exercises, including Chinese requests such as “找几个哑铃练胸动作” or “推荐徒手练背动作”.
---

# Find Fitness Exercises

Use the bundled deterministic search script to ground exercise matches in the 1,324-record dataset. Do not invent an exercise, instruction, equipment requirement, or media URL.

## Search workflow

1. Extract the user's query, body-part, equipment, target-muscle, language, and result-count constraints. Default to the user's language and 5 results.
2. Run `scripts/search_exercises.py` from this skill directory. Prefer JSON when composing a tailored answer:

   ```bash
   python scripts/search_exercises.py "哑铃练胸" --equipment 哑铃 --body-part 胸部 --lang zh --limit 5 --format json
   ```

   For a ready-to-present result, request Markdown:

   ```bash
   python scripts/search_exercises.py "bodyweight back" --equipment "body weight" --lang en --format markdown
   ```

3. Present the strongest matches. For each result, include the name, target, equipment, a brief match reason, 2–4 key steps when available, the animation or thumbnail link, and the dataset-provided attribution.
4. State any inferred constraints. If results are weak or empty, relax only an inferred constraint, rerun once, and tell the user what changed.
5. Keep dataset lookup separate from programming advice. Give sets, reps, load, progression, injury modifications, or a full workout only when requested and label them as general guidance.

## Script options

- Use `--body-part`, `--equipment`, and `--target` for hard filters. Chinese aliases such as `胸部`, `自重`, `哑铃`, `腹肌`, and `二头肌` are accepted.
- Use `--lang en|es|it|tr|ru|zh|hi|pl|ko|fr` to select instruction language.
- Use `--limit 1..20` and `--format json|markdown` to control output.
- Use `--list-values` to inspect canonical filter values.
- Use `--dataset PATH` for a custom local copy. Otherwise the script finds this repository's `data/exercises.json` or downloads the upstream file into a temporary cache.

## Response guardrails

- Preserve `© Gym visual — https://gymvisual.com/` on every response that displays or links media.
- Link back to `https://github.com/hasaneyldrm/exercises-dataset` as the data source.
- Treat the animations and instructions as references, not individualized medical advice. Tell the user to stop if an exercise causes pain and seek qualified help when injury, pregnancy, rehabilitation, or a medical condition is involved.
- Read [references/dataset-notes.md](references/dataset-notes.md) when explaining coverage, fields, provenance, or licensing.
