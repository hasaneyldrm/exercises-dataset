#!/usr/bin/env python3
"""Extract every unique English instruction step from data/exercises.json.

Output: scripts/en_strings.json — an array of {"id": int, "en": str} objects,
where each `en` value appears exactly once across all 1,324 exercises.

The translation script (2_translate.py) consumes this list, translates each
entry to pt-PT, and writes scripts/translations.json keyed by the same `id`.

Usage:
    python3 scripts/1_extract_unique.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "exercises.json"
OUT = ROOT / "scripts" / "en_strings.json"


def main() -> int:
    if not SRC.exists():
        sys.stderr.write(f"ERROR: {SRC} not found\n")
        return 1

    with SRC.open("r", encoding="utf-8") as f:
        exercises = json.load(f)

    seen: dict[str, int] = {}
    order: list[str] = []

    for ex in exercises:
        steps = ex.get("instruction_steps", {}).get("en", [])
        if not isinstance(steps, list):
            sys.stderr.write(
                f"ERROR: exercise {ex.get('id')} has non-list instruction_steps.en\n"
            )
            return 1
        for s in steps:
            if not isinstance(s, str) or not s.strip():
                sys.stderr.write(
                    f"ERROR: exercise {ex.get('id')} has empty/non-string step\n"
                )
                return 1
            if s not in seen:
                seen[s] = len(order)
                order.append(s)

    out = [{"id": i, "en": s} for i, s in enumerate(order)]

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    total_steps = sum(
        len(ex.get("instruction_steps", {}).get("en", [])) for ex in exercises
    )
    print(f"exercises:         {len(exercises)}")
    print(f"total en steps:    {total_steps}")
    print(f"unique en strings: {len(out)}")
    print(f"dedup ratio:       {total_steps / len(out):.2f}x")
    print(f"written to:        {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())