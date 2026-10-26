#!/usr/bin/env python3
"""Merge Uzbek exercise translations, optionally translating missing content online.

Uses the original data/exercises.json format:
- name: string; name_uz: string (when available)
- instructions.<lang>: string
- instruction_steps.<lang>: list[str]

The online provider is an unofficial, rate-limited Google Translate endpoint.
Machine-generated translations MUST be reviewed before release.
"""
import argparse
import json
import os
import re
import tempfile
import time
import urllib.parse
import urllib.request
from pathlib import Path


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def atomic_write(path, value):
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".uz-", suffix=".json", dir=target.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as out:
            json.dump(value, out, ensure_ascii=False, indent=2)
            out.write("\n")
        os.replace(tmp, target)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def machine_translate(text):
    params = urllib.parse.urlencode({"client": "gtx", "sl": "en", "tl": "uz",
                                      "dt": "t", "q": text})
    url = "https://translate.googleapis.com/translate_a/single?" + params
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for retry in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                chunks = json.load(response)[0]
            translated = "".join(chunk[0] for chunk in chunks if chunk and chunk[0]).strip()
            if not translated or (translated.casefold() == text.strip().casefold()
                                  and len(text.split()) > 3):
                raise ValueError("Missing or untranslated response")
            if re.search(r"[\u0400-\u052f]", translated):
                raise ValueError("Non-Latin Uzbek response")
            return translated
        except (OSError, ValueError, IndexError, TypeError, KeyError) as error:
            if retry == 2:
                raise RuntimeError(f"Translation failed: {text[:70]!r}") from error
            time.sleep(2 ** retry)


def run(input_path, output_path, overlay_path, mode, cache_path, require_complete):
    exercises = read_json(input_path)
    overlay_rows = read_json(overlay_path)
    if not isinstance(exercises, list) or not isinstance(overlay_rows, list):
        raise ValueError("Expected two JSON arrays")
    overlays = {row["id"]: row for row in overlay_rows}
    if len(overlays) != len(overlay_rows):
        raise ValueError("Duplicate IDs in Uzbek overlay")
    source_ids = {row["id"] for row in exercises}
    if len(source_ids) != len(exercises) or set(overlays) != source_ids:
        raise ValueError("Dataset and translation overlay IDs do not match")

    cache = read_json(cache_path) if Path(cache_path).exists() else {}
    translated_count = 0

    def get_translation(text):
        nonlocal translated_count
        if text in cache:
            return cache[text]
        result = machine_translate(text)
        cache[text] = result
        translated_count += 1
        if translated_count % 25 == 0:
            atomic_write(cache_path, cache)
            print(f"Translated {translated_count} unique texts", flush=True)
        time.sleep(0.12)
        return result

    try:
        for ex in exercises:
            o = overlays[ex["id"]]
            for field in ("category", "body_part", "equipment",
                          "muscle_group", "target", "secondary_muscles"):
                localized = field + "_uz"
                if localized not in o:
                    raise ValueError(f"{ex['id']}: missing {localized}")
                ex[localized] = o[localized]

            if "name_uz" in o:
                ex["name_uz"] = o["name_uz"]
            if "instruction_steps_uz" in o:
                ex.setdefault("instruction_steps", {})["uz"] = o["instruction_steps_uz"]
            if "instructions_uz" in o:
                ex.setdefault("instructions", {})["uz"] = o["instructions_uz"]

            if mode == "auto":
                if not ex.get("name_uz"):
                    ex["name_uz"] = get_translation(ex["name"])
                en_steps = ex["instruction_steps"]["en"]
                if not ex.get("instruction_steps", {}).get("uz"):
                    ex["instruction_steps"]["uz"] = [get_translation(s) for s in en_steps]
                ex["instructions"]["uz"] = " ".join(ex["instruction_steps"]["uz"])

            en_steps = ex["instruction_steps"]["en"]
            uz_steps = ex.get("instruction_steps", {}).get("uz")
            if uz_steps is not None:
                if (len(uz_steps) != len(en_steps)
                        or not all(isinstance(t, str) and t.strip() for t in uz_steps)):
                    raise ValueError(f"{ex['id']}: invalid Uzbek steps")
                if not ex.get("instructions", {}).get("uz"):
                    ex["instructions"]["uz"] = " ".join(uz_steps)

        complete = sum(bool(ex.get("name_uz") and ex.get("instructions", {}).get("uz")
                            and ex.get("instruction_steps", {}).get("uz"))
                       for ex in exercises)
        if require_complete and complete != len(exercises):
            raise ValueError(f"Only {complete}/{len(exercises)} exercises fully translated")
        atomic_write(output_path, exercises)
        print(f"Saved {len(exercises)} exercises; Uzbek instructions: "
              f"{complete}/{len(exercises)}. New machine translations: {translated_count}")
    finally:
        if translated_count:
            atomic_write(cache_path, cache)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Apply Uzbek exercise localization")
    p.add_argument("--input", default="data/exercises.json")
    p.add_argument("--output", default="data/exercises.json")
    p.add_argument("--overlay", default="data/exercises_uz.json")
    p.add_argument("--cache", default="data/uz_translation_cache.json")
    p.add_argument("--mode", choices=["offline", "auto"], default="offline")
    p.add_argument("--require-complete", action="store_true")
    args = p.parse_args()
    run(args.input, args.output, args.overlay, args.mode, args.cache, args.require_complete)
