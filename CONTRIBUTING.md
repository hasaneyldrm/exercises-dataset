# Contributing

Thanks for helping improve the exercises dataset. Keep changes small, reviewable, and focused on data quality, tooling, or documentation.

## Before opening a PR

1. Confirm your change is allowed by the media license in `LICENSE` and `NOTICE.md`.
2. Run the dataset validator:

   ```bash
   node scripts/validate-dataset.mjs
   ```

3. If you are changing schema or validation behavior, check open pull requests first to avoid duplicating active work.

## Dataset rules

- Keep every exercise `id` unique and formatted as four digits, for example `0001`.
- Keep `image` and `gif_url` paths aligned with `id` and `media_id`:
  - `images/<id>-<media_id>.jpg`
  - `videos/<id>-<media_id>.gif`
- Keep all six instruction languages populated: `en`, `es`, `it`, `tr`, `ru`, and `zh`.
- Keep both `instructions` and `instruction_steps` in sync when editing exercise instructions.
- Keep `secondary_muscles` as an array of strings.
- Keep the exact media attribution in every record: `© Gym visual — https://gymvisual.com/`.

Duplicate exercise names are allowed only when the records represent distinct media or movement variants. The validator reports them as warnings so reviewers can inspect them.

## Media rules

The `images/` and `videos/` assets are not covered by the MIT license. They are included with separate permission from Gym visual at 180x180 resolution. Do not replace, upscale, redistribute, or add media unless you have confirmed the rights and attribution requirements.

## Browser checks

If you edit `index.html`, manually verify:

- Search filters the exercise grid.
- Category, equipment, and target filters work.
- Infinite scroll appends more exercises.
- Exercise modals show media, metadata, muscles, and language tabs.

If you edit `setup.html`, manually verify:

- Database tabs switch SQL dialects.
- SQL generation downloads a file.
- API language tabs update examples.
- The LLM prompt updates when framework or database options change.
