#!/usr/bin/env python3
"""Translate the unique English steps from scripts/en_strings.json to pt-PT.

Output: scripts/translations.json — {"<id>": {"en": ..., "pt": ...}, ...}
Resumable: re-running skips IDs already present in the output file.

Provider
--------
Uses any OpenAI-compatible Chat Completions endpoint. Configure via env vars:
    OPENAI_API_KEY   required
    OPENAI_BASE_URL  default: https://api.openai.com/v1
    OPENAI_MODEL     default: gpt-4o-mini
    BATCH_SIZE       default: 50  (strings per request)
    MAX_RETRIES      default: 4
    REQUEST_TIMEOUT  default: 120 (seconds)

Tested with: OpenAI gpt-4o-mini, Anthropic via openrouter.ai (set OPENAI_BASE_URL
to https://openrouter.ai/api/v1 and OPENAI_MODEL to anthropic/claude-sonnet-4),
and any local server exposing the OpenAI Chat Completions schema (llama.cpp,
ollama with /v1/chat/completions, vllm, LM Studio, etc.).

Glossary
--------
scripts/glossary_pt.json pins the recurring fitness terminology. The system
prompt instructs the model to use the glossary's exact PT form whenever the
source contains the English term — so terminology stays consistent across all
1,324 records rather than varying sentence by sentence (same approach the
French PR used for French).

Usage:
    OPENAI_API_KEY=sk-... python3 scripts/2_translate.py
    OPENAI_API_KEY=sk-... OPENAI_BASE_URL=https://openrouter.ai/api/v1 \
        OPENAI_MODEL=anthropic/claude-sonnet-4 python3 scripts/2_translate.py
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
SRC = SCRIPTS / "en_strings.json"
GLOSSARY = SCRIPTS / "glossary_pt.json"
OUT = SCRIPTS / "translations.json"

API_KEY = os.environ.get("OPENAI_API_KEY")
BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
BATCH_SIZE = int(os.environ.get("BATCH_SIZE", "50"))
MAX_RETRIES = int(os.environ.get("MAX_RETRIES", "4"))
REQUEST_TIMEOUT = int(os.environ.get("REQUEST_TIMEOUT", "120"))


SYSTEM_PROMPT = """\
You are a professional translator specializing in fitness and exercise \
instruction text. Translate the user-provided English exercise step \
sentences into European Portuguese (pt-PT, Portuguese from Portugal).

Hard rules:
1. Output ONLY a JSON object: {"results": [{"id": <int>, "pt": "<translation>"}]}.\
 No prose, no Markdown, no code fences.
2. Translate every entry in the same order as the input. The "id" in each \
result MUST match the input id exactly.
3. Register: impersonal, 3rd-person without subject pronoun — "Deite-se", \
"Mantenha", "Repita", "Contraia o abdomen". NEVER use "tu" (informal) and \
NEVER use "voce" (it reads as Brazilian). Use the imperative/infinitive form \
that addresses the reader impersonally.
4. PT-PT orthography, not PT-BR: "abdmen" (not "abdmen"), "fletido" \
(not "flexionado"), "fletir" (not "flexionar"), "peito", "chorar" stays \
"chorar". Use the European forms consistently.
5. Terminology: when the source contains an English term present in the \
glossary below, you MUST use the exact pt form given there. Do not substitute \
synonyms.
6. Preserve sentence punctuation and capitalization style of the source. \
Keep periods where the source has them.
7. Do not translate exercise names, muscle names that are not in the glossary, \
or proper nouns (e.g. "Smith", "EZ"). Keep them as in the source.
8. Do not add commentary, do not paraphrase, do not expand. Translate the \
step as-is.
9. If a step is a single word or very short fragment, still translate it \
and keep it short.
10. Numbers, angles (45-degree, 90-degree), and units stay as digits/words \
matching the source style.

Glossary (English -> pt-PT, use these exact mappings when the term appears):
"""


def build_system_prompt() -> str:
    if not GLOSSARY.exists():
        sys.stderr.write(f"WARN: {GLOSSARY} not found — proceeding without glossary\n")
        return SYSTEM_PROMPT.rstrip() + "\n(none provided)\n"
    g = json.loads(GLOSSARY.read_text(encoding="utf-8"))
    lines = []
    for en, pt in g.get("terms", {}).items():
        lines.append(f'  "{en}" -> "{pt}"')
    return SYSTEM_PROMPT.rstrip() + "\n" + "\n".join(lines) + "\n"


def load_existing() -> dict[str, dict[str, str]]:
    if OUT.exists():
        return json.loads(OUT.read_text(encoding="utf-8"))
    return {}


def save(translations: dict[str, dict[str, str]]) -> None:
    OUT.write_text(
        json.dumps(translations, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def call_api(system: str, user: str) -> dict[str, Any]:
    url = f"{BASE_URL.rstrip('/')}/chat/completions"
    payload = json.dumps(
        {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "temperature": 0.2,
            "response_format": {"type": "json_object"},
        }
    ).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")

    last_err: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                body = resp.read().decode("utf-8")
                data = json.loads(body)
                content = data["choices"][0]["message"]["content"]
                return json.loads(content)
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code in (429, 500, 502, 503, 504):
                wait = min(2**attempt, 60)
                sys.stderr.write(
                    f"  HTTP {e.code} (attempt {attempt}/{MAX_RETRIES}), "
                    f"retrying in {wait}s\n"
                )
                time.sleep(wait)
                continue
            raise
        except (urllib.error.URLError, json.JSONDecodeError, KeyError, ValueError) as e:
            last_err = e
            wait = min(2**attempt, 60)
            sys.stderr.write(
                f"  error {type(e).__name__}: {e} (attempt {attempt}/{MAX_RETRIES}), "
                f"retrying in {wait}s\n"
            )
            time.sleep(wait)
    raise RuntimeError(f"all {MAX_RETRIES} attempts failed: {last_err}")


def translate_batch(
    system: str, batch: list[dict[str, Any]], translations: dict[str, dict[str, str]]
) -> None:
    user = json.dumps(
        {
            "instructions": "Translate each entry to pt-PT. Return "
            '{"results": [{"id": <int>, "pt": "<translation>"}]}.',
            "entries": batch,
        },
        ensure_ascii=False,
    )
    resp = call_api(system, user)
    results = resp.get("results", [])
    if not isinstance(results, list):
        raise RuntimeError(f"unexpected response shape: {resp!r}")

    by_id = {r["id"]: r["pt"] for r in results if "id" in r and "pt" in r}
    for entry in batch:
        eid = entry["id"]
        if eid not in by_id:
            raise RuntimeError(f"missing id {eid} in response")
        translations[str(eid)] = {"en": entry["en"], "pt": by_id[eid]}


def main() -> int:
    if not API_KEY:
        sys.stderr.write(
            "ERROR: OPENAI_API_KEY env var is required.\n"
            "Set it to any OpenAI-compatible API key (OpenAI, OpenRouter, "
            "local llama.cpp/ollama/vllm, etc.).\n"
        )
        return 2

    if not SRC.exists():
        sys.stderr.write(
            f"ERROR: {SRC} not found. Run scripts/1_extract_unique.py first.\n"
        )
        return 1

    entries = json.loads(SRC.read_text(encoding="utf-8"))
    translations = load_existing()
    system = build_system_prompt()

    pending = [e for e in entries if str(e["id"]) not in translations]
    print(f"total unique strings: {len(entries)}")
    print(f"already translated:  {len(entries) - len(pending)}")
    print(f"pending:             {len(pending)}")
    print(f"batch size:          {BATCH_SIZE}")
    print(f"model:               {MODEL}")
    print(f"endpoint:            {BASE_URL}")
    print()

    if not pending:
        print("nothing to do — translations.json is complete")
        return 0

    done = len(entries) - len(pending)
    total = len(entries)
    for i in range(0, len(pending), BATCH_SIZE):
        batch = pending[i : i + BATCH_SIZE]
        try:
            translate_batch(system, batch, translations)
        except Exception as e:
            sys.stderr.write(f"FATAL on batch starting id={batch[0]['id']}: {e}\n")
            save(translations)
            sys.stderr.write(
                f"partial state saved ({len(translations)}/{total}). "
                "Re-run to resume.\n"
            )
            return 1
        done += len(batch)
        save(translations)
        pct = 100.0 * done / total
        print(f"  [{done:>5}/{total}] {pct:5.1f}%  last id={batch[-1]['id']}")

    print(f"\ndone. {len(translations)} translations in {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())