#!/usr/bin/env python3
"""Apply scripts/translations.json to data/exercises.json, adding `pt`.

Insertion order: `pt` is appended AFTER `fr` in both `instructions` and
`instruction_steps` of every record. All pre-existing fields are kept
byte-identical (the script verifies this).

Invariants enforced (mirror the French PR, commit 6f3031b):
  1. Result validates against the updated JSON Schema.
  2. `pt` step count == `en` step count, in every record.
  3. `instructions.pt` == ' '.join(instruction_steps.pt), every record.
  4. Pre-existing fields byte-identical to original (only `pt` keys added).
  5. No empty strings in `pt`; none left in English.
  6. `pt` appears last in both objects' key order, after `fr`.

Modes:
    python3 scripts/3_apply.py            # apply: write new exercises.json
    python3 scripts/3_apply.py --check    # check only: report any invariant
                                           # violations on the current files

Usage requires: scripts/translations.json (from 2_translate.py) for apply mode.
Check mode runs against whatever is currently on disk.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "exercises.json"
SCHEMA = ROOT / "data" / "exercises.schema.json"
SCRIPTS = ROOT / "scripts"
TRANSLATIONS = SCRIPTS / "translations.json"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def serialize_exercises(exercises: list[dict[str, Any]]) -> str:
    """Serialize with indent=2 + trailing newline, matching the file's format."""
    return json.dumps(exercises, ensure_ascii=False, indent=2) + "\n"


def check_invariants(exercises: list[dict[str, Any]]) -> list[str]:
    """Return a list of invariant violation messages (empty == all pass)."""
    errors: list[str] = []

    # Load schema for invariant #1
    try:
        schema = load(SCHEMA)
    except Exception as e:
        errors.append(f"could not load schema: {e}")
        schema = None

    if schema is not None:
        try:
            import jsonschema

            jsonschema.validate(exercises, schema)
        except ImportError:
            errors.append(
                "jsonschema not installed — invariant #1 (schema validation) "
                "skipped. Install: pip install jsonschema"
            )
        except Exception as e:
            errors.append(f"schema validation failed: {e}")

    for i, ex in enumerate(exercises):
        eid = ex.get("id", f"<index {i}>")

        # invariant 2: pt step count == en step count
        instr = ex.get("instructions", {})
        steps = ex.get("instruction_steps", {})
        if "pt" not in instr:
            errors.append(f"{eid}: instructions.pt missing")
            continue
        if "pt" not in steps:
            errors.append(f"{eid}: instruction_steps.pt missing")
            continue
        if not isinstance(steps["pt"], list):
            errors.append(f"{eid}: instruction_steps.pt is not a list")
            continue
        if not isinstance(instr["pt"], str):
            errors.append(f"{eid}: instructions.pt is not a string")
            continue

        en_steps = steps.get("en", [])
        if len(steps["pt"]) != len(en_steps):
            errors.append(
                f"{eid}: pt step count {len(steps['pt'])} != en step count "
                f"{len(en_steps)}"
            )

        # invariant 3: instructions.pt == ' '.join(instruction_steps.pt)
        expected = " ".join(steps["pt"])
        if instr["pt"] != expected:
            errors.append(
                f"{eid}: instructions.pt does not equal ' '.join(steps.pt)"
            )
            errors.append(f"    got:      {instr['pt'][:120]!r}")
            errors.append(f"    expected: {expected[:120]!r}")

        # invariant 5: no empty strings in pt; none left in English
        if not instr["pt"].strip():
            errors.append(f"{eid}: instructions.pt is empty/whitespace")
        for j, s in enumerate(steps["pt"]):
            if not isinstance(s, str) or not s.strip():
                errors.append(f"{eid}: instruction_steps.pt[{j}] is empty/non-string")

        # invariant 6: pt is last, after fr
        instr_keys = list(instr.keys())
        if instr_keys and instr_keys[-1] != "pt":
            errors.append(
                f"{eid}: instructions.pt is not last (order: {instr_keys})"
            )
        steps_keys = list(steps.keys())
        if steps_keys and steps_keys[-1] != "pt":
            errors.append(
                f"{eid}: instruction_steps.pt is not last (order: {steps_keys})"
            )

    return errors


def check_byte_identical_additive(
    original: list[dict[str, Any]], updated: list[dict[str, Any]]
) -> list[str]:
    """Invariant 4: every pre-existing field is byte-identical; only `pt` added."""
    errors: list[str] = []
    if len(original) != len(updated):
        errors.append(
            f"length mismatch: original {len(original)} vs updated {len(updated)}"
        )
        return errors

    for i, (o, u) in enumerate(zip(original, updated)):
        eid = o.get("id", f"<index {i}>")
        for key, o_val in o.items():
            if key not in u:
                errors.append(f"{eid}: field {key!r} missing from updated record")
                continue
            u_val = u[key]
            # For instructions/instruction_steps, compare only pre-existing sub-keys
            if key in ("instructions", "instruction_steps") and isinstance(o_val, dict):
                for sub_key, o_sub in o_val.items():
                    if sub_key not in u_val:
                        errors.append(f"{eid}: {key}.{sub_key!r} missing from updated")
                    elif u_val[sub_key] != o_sub:
                        errors.append(f"{eid}: {key}.{sub_key!r} changed value")
                        errors.append(f"    original: {str(o_sub)[:160]!r}")
                        errors.append(f"    updated:  {str(u_val[sub_key])[:160]!r}")
            elif u_val != o_val:
                errors.append(f"{eid}: field {key!r} changed value")
                errors.append(f"    original: {str(o_val)[:160]!r}")
                errors.append(f"    updated:  {str(u_val)[:160]!r}")

        # Only `pt` should be added, and only inside instructions/instruction_steps
        for key in u:
            if key not in o:
                errors.append(f"{eid}: unexpected new top-level field {key!r}")
        for sub_key in u.get("instructions", {}):
            if sub_key not in o.get("instructions", {}):
                if sub_key != "pt":
                    errors.append(
                        f"{eid}: unexpected new instructions key {sub_key!r}"
                    )
        for sub_key in u.get("instruction_steps", {}):
            if sub_key not in o.get("instruction_steps", {}):
                if sub_key != "pt":
                    errors.append(
                        f"{eid}: unexpected new instruction_steps key {sub_key!r}"
                    )

    return errors


def apply_translations() -> int:
    if not TRANSLATIONS.exists():
        sys.stderr.write(
            f"ERROR: {TRANSLATIONS} not found. Run scripts/2_translate.py first.\n"
        )
        return 1

    translations_raw = load(TRANSLATIONS)
    # translations.json: {"<id>": {"en": ..., "pt": ...}}
    by_id: dict[int, str] = {
        int(k): v["pt"] for k, v in translations_raw.items() if "pt" in v
    }

    original = load(DATA)
    updated: list[dict[str, Any]] = []

    # Build reverse map: en string -> pt translation
    en_to_pt: dict[str, str] = {
        translations_raw[str(k)]["en"]: translations_raw[str(k)]["pt"]
        for k in translations_raw
        if "pt" in translations_raw[k]
    }

    missing_translations: list[tuple[str, str]] = []
    for ex in original:
        eid = ex["id"]
        new_ex = dict(ex)

        # instruction_steps — translate each step individually
        steps = dict(ex["instruction_steps"])
        en_steps = ex["instruction_steps"]["en"]
        pt_steps: list[str] = []
        for s in en_steps:
            if s not in en_to_pt:
                missing_translations.append((eid, s[:80]))
                break
            pt_steps.append(en_to_pt[s])
        else:
            steps["pt"] = pt_steps
            new_ex["instruction_steps"] = steps

            # instructions.pt = ' '.join(instruction_steps.pt) — invariant #3
            instr = dict(ex["instructions"])
            instr["pt"] = " ".join(pt_steps)
            new_ex["instructions"] = instr

        updated.append(new_ex)

    if missing_translations:
        sys.stderr.write(
            f"ERROR: {len(missing_translations)} step(s) lack translations:\n"
        )
        for eid, sample in missing_translations[:20]:
            sys.stderr.write(f"  {eid}: {sample!r}\n")
        if len(missing_translations) > 20:
            sys.stderr.write(f"  ... and {len(missing_translations) - 20} more\n")
        sys.stderr.write(
            "Re-run scripts/2_translate.py to complete translations.json.\n"
        )
        return 1

    if len(updated) != len(original):
        sys.stderr.write(
            f"ERROR: only {len(updated)}/{len(original)} records updated\n"
        )
        return 1

    # Invariant 4: byte-identical pre-existing fields
    additive_errors = check_byte_identical_additive(original, updated)
    if additive_errors:
        sys.stderr.write("Invariant 4 (additive-only) FAILED:\n")
        for e in additive_errors:
            sys.stderr.write(f"  {e}\n")
        return 1

    # Invariants 1, 2, 3, 5, 6
    inv_errors = check_invariants(updated)
    if inv_errors:
        sys.stderr.write("Invariants FAILED:\n")
        for e in inv_errors:
            sys.stderr.write(f"  {e}\n")
        return 1

    # Write the updated file
    new_text = serialize_exercises(updated)
    DATA.write_text(new_text, encoding="utf-8")
    print(f"OK: wrote {len(updated)} records with `pt` to {DATA.relative_to(ROOT)}")
    print(f"   file size: {len(new_text):,} bytes")
    return 0


def check_only() -> int:
    if not DATA.exists():
        sys.stderr.write(f"ERROR: {DATA} not found\n")
        return 1
    exercises = load(DATA)
    errors = check_invariants(exercises)
    if errors:
        sys.stderr.write(f"FAIL: {len(errors)} invariant violation(s):\n")
        for e in errors:
            sys.stderr.write(f"  {e}\n")
        return 1
    print(f"OK: all 6 invariants pass for {len(exercises)} records")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check only — report invariant violations on the current files.",
    )
    args = parser.parse_args()

    if args.check:
        return check_only()
    return apply_translations()


if __name__ == "__main__":
    sys.exit(main())