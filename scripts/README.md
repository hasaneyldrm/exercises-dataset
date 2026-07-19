# Portuguese (pt-PT) translation pipeline

Adds `pt` (European Portuguese) instructions to all 1,324 exercises in
`data/exercises.json`, matching the structure of the French PR (commit
`6f3031b`).

## Files

- `glossary_pt.json` — pinned PT-PT fitness terminology. The translator must
  use these exact mappings whenever the English source contains the term.
- `1_extract_unique.py` — dedup all `instruction_steps.en` across the dataset
  into `en_strings.json` (the unique strings to translate).
- `2_translate.py` — translate `en_strings.json` to `translations.json` via
  any OpenAI-compatible endpoint. Resumable.
- `3_apply.py` — rebuild `data/exercises.json` with `pt` inserted after `fr`,
  enforcing 6 invariants. `--check` mode validates the current file.
- `4_sync_index_html.py` — regenerate the inline `EXERCISES` JSON inside
  `index.html` from the updated `data/exercises.json`.

## End-to-end

```bash
# 1. Extract unique English strings
python3 scripts/1_extract_unique.py

# 2. Translate to pt-PT (any OpenAI-compatible endpoint)
OPENAI_API_KEY=sk-... python3 scripts/2_translate.py

# 3. Apply translations to data/exercises.json (enforces invariants)
python3 scripts/3_apply.py

# 4. Sync the inline JSON copy inside index.html
python3 scripts/4_sync_index_html.py

# 5. Verify
python3 scripts/3_apply.py --check
```

## Environment

| Var | Default | Notes |
|---|---|---|
| `OPENAI_API_KEY` | — | required |
| `OPENAI_BASE_URL` | `https://api.openai.com/v1` | any OpenAI-compatible endpoint |
| `OPENAI_MODEL` | `gpt-4o-mini` | Anthropic via OpenRouter: `anthropic/claude-sonnet-4` |
| `BATCH_SIZE` | `50` | strings per request |
| `MAX_RETRIES` | `4` | exponential backoff on 429/5xx |
| `REQUEST_TIMEOUT` | `120` | seconds |

## Invariants (enforced by `3_apply.py`)

1. Result validates against `data/exercises.schema.json`.
2. `pt` step count == `en` step count, every record.
3. `instructions.pt` == `' '.join(instruction_steps.pt)`, every record.
4. Pre-existing fields byte-identical (only `pt` keys added).
5. No empty strings in `pt`; none left in English.
6. `pt` is the last key in both `instructions` and `instruction_steps` (after
   `fr`).

## Notes

- Machine translations, reviewed programmatically rather than by a native
  speaker. Spot-check 5–10 exercises in `index.html` before opening the PR.
- The glossary pins ~150 fitness terms so terminology stays consistent across
  all 1,324 records rather than varying sentence by sentence.
- Register: impersonal 3rd-person without subject pronoun — `Deite-se`,
  `Mantenha`, `Repita`. Avoids the `tu`/`você` split, reads as PT-PT.