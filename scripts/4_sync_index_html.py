#!/usr/bin/env python3
"""Sync the embedded EXERCISES JSON inside index.html with data/exercises.json.

index.html contains a 16 MB inline copy of the dataset on a single line:
    const EXERCISES = [...];
This script replaces that single line with a fresh serialization of
data/exercises.json, compact (no indent, no spaces after separators),
matching the existing format. Key order is preserved (insertion order).

Usage:
    python3 scripts/4_sync_index_html.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "exercises.json"
INDEX_HTML = ROOT / "index.html"

# Matches the single line: "  const EXERCISES = [...];"
# Uses a non-greedy match up to the first "];" at end of line.
PATTERN = re.compile(r"^(\s*const EXERCISES = )(\[.*\]);$", re.MULTILINE)


def main() -> int:
    if not DATA.exists():
        sys.stderr.write(f"ERROR: {DATA} not found\n")
        return 1
    if not INDEX_HTML.exists():
        sys.stderr.write(f"ERROR: {INDEX_HTML} not found\n")
        return 1

    exercises = json.loads(DATA.read_text(encoding="utf-8"))
    compact = json.dumps(exercises, ensure_ascii=False, separators=(",", ":"))

    html = INDEX_HTML.read_text(encoding="utf-8")
    match = PATTERN.search(html)
    if not match:
        sys.stderr.write(
            "ERROR: could not find `const EXERCISES = [...];` line in index.html\n"
        )
        return 1

    new_line = f"{match.group(1)}{compact};"
    new_html = html[: match.start()] + new_line + html[match.end() :]

    INDEX_HTML.write_text(new_html, encoding="utf-8")
    print(f"OK: synced index.html with {len(exercises)} exercises")
    print(f"   embedded JSON size: {len(compact):,} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())