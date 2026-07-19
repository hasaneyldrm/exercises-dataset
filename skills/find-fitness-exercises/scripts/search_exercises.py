#!/usr/bin/env python3
"""Search hasaneyldrm/exercises-dataset without third-party dependencies."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import unicodedata
import urllib.error
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote


REPOSITORY_URL = "https://github.com/hasaneyldrm/exercises-dataset"
RAW_ROOT = "https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main"
DATASET_URL = f"{RAW_ROOT}/data/exercises.json"
LANGUAGES = ("en", "es", "it", "tr", "ru", "zh", "hi", "pl", "ko", "fr")
MAX_DATASET_BYTES = 50 * 1024 * 1024

ALIASES = {
    # Body parts
    "胸部": "chest",
    "胸": "chest",
    "背部": "back",
    "背": "back",
    "肩部": "shoulders",
    "肩膀": "shoulders",
    "肩": "shoulders",
    "腰腹": "waist abs",
    "腰部": "waist",
    "核心": "waist core abs",
    "上臂": "upper arms",
    "大臂": "upper arms",
    "前臂": "lower arms forearms",
    "小臂": "lower arms forearms",
    "手臂": "upper arms lower arms",
    "大腿": "upper legs",
    "小腿": "lower legs calves",
    "腿部": "upper legs lower legs",
    "有氧": "cardio cardiovascular system",
    "颈部": "neck",
    # Equipment
    "徒手": "body weight",
    "自重": "body weight",
    "无器械": "body weight",
    "哑铃": "dumbbell",
    "杠铃": "barbell",
    "壶铃": "kettlebell",
    "绳索器械": "cable",
    "龙门架": "cable",
    "弹力带": "resistance band band",
    "史密斯机": "smith machine",
    "史密斯": "smith machine",
    "健身球": "stability ball",
    "药球": "medicine ball",
    "泡沫轴": "roller",
    "bodyweight": "body weight",
    # Target muscles
    "腹肌": "abs",
    "胸肌": "pectorals",
    "二头肌": "biceps",
    "肱二头": "biceps",
    "三头肌": "triceps",
    "肱三头": "triceps",
    "臀肌": "glutes",
    "臀部": "glutes",
    "三角肌": "delts",
    "背阔肌": "lats",
    "股四头": "quads quadriceps",
    "腘绳肌": "hamstrings",
    "斜方肌": "traps trapezius",
    # Common exercise names
    "俯卧撑": "push-up",
    "深蹲": "squat",
    "硬拉": "deadlift",
    "卧推": "bench press",
    "引体向上": "pull-up",
    "平板支撑": "plank",
    "弯举": "curl",
    "侧平举": "lateral raise",
    "划船": "row",
    "卷腹": "crunch",
    "仰卧起坐": "sit-up",
    "箭步蹲": "lunge",
    "臀桥": "glute bridge",
    "波比跳": "burpee",
}

FILTER_ALIASES = {
    "body_part": {
        "胸": ("chest",), "胸部": ("chest",), "背": ("back",), "背部": ("back",),
        "肩": ("shoulders",), "肩部": ("shoulders",), "腰": ("waist",), "腰腹": ("waist",),
        "手臂": ("upper arms", "lower arms"), "上臂": ("upper arms",), "前臂": ("lower arms",),
        "小臂": ("lower arms",), "腿": ("upper legs", "lower legs"), "腿部": ("upper legs", "lower legs"),
        "大腿": ("upper legs",), "小腿": ("lower legs",), "有氧": ("cardio",), "颈部": ("neck",),
    },
    "equipment": {
        "徒手": ("body weight",), "自重": ("body weight",), "无器械": ("body weight",),
        "哑铃": ("dumbbell",), "杠铃": ("barbell",), "壶铃": ("kettlebell",),
        "绳索": ("cable",), "龙门架": ("cable",), "弹力带": ("band", "resistance band"),
        "史密斯": ("smith machine",), "健身球": ("stability ball",), "药球": ("medicine ball",),
        "bodyweight": ("body weight",),
    },
    "target": {
        "腹肌": ("abs",), "胸肌": ("pectorals",), "二头肌": ("biceps",),
        "三头肌": ("triceps",), "臀肌": ("glutes",), "臀部": ("glutes",),
        "三角肌": ("delts",), "背阔肌": ("lats",), "股四头": ("quads",),
        "腘绳肌": ("hamstrings",), "小腿": ("calves",), "前臂": ("forearms",),
        "斜方肌": ("traps",),
    },
}


def normalize(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).lower()
    text = re.sub(r"[^\w\u4e00-\u9fff]+", " ", text, flags=re.UNICODE)
    return " ".join(text.split())


def expand_query(query: str) -> str:
    expanded = normalize(query)
    for alias in sorted(ALIASES, key=len, reverse=True):
        expanded = expanded.replace(alias, f" {ALIASES[alias]} ")
    return normalize(expanded)


def query_terms(query: str) -> list[str]:
    terms = re.findall(r"[a-z0-9]+|[\u4e00-\u9fff]+", expand_query(query))
    ignored = {"find", "show", "exercise", "exercises", "workout", "please", "推荐", "动作", "几个", "适合", "帮我", "想练"}
    return [
        term
        for term in terms
        if term not in ignored and (not term.isascii() or len(term) > 2)
    ]


def find_local_dataset(explicit_path: str | None) -> Path | None:
    candidates: list[Path] = []
    if explicit_path:
        candidates.append(Path(explicit_path).expanduser())
    env_path = os.environ.get("EXERCISES_DATASET_PATH")
    if env_path:
        candidates.append(Path(env_path).expanduser())
    for parent in Path(__file__).resolve().parents:
        candidates.append(parent / "data" / "exercises.json")
    candidates.append(Path.cwd() / "data" / "exercises.json")
    return next((path.resolve() for path in candidates if path.is_file()), None)


def download_dataset(refresh: bool) -> Path:
    cache_dir = Path(tempfile.gettempdir()) / "find-fitness-exercises"
    cache_path = cache_dir / "exercises.json"
    if cache_path.is_file() and not refresh:
        return cache_path
    cache_dir.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(DATASET_URL, headers={"User-Agent": "find-fitness-exercises/1.0"})
    temporary = cache_path.with_suffix(".tmp")
    try:
        with urllib.request.urlopen(request, timeout=60) as response, temporary.open("wb") as output:
            content_length = response.headers.get("Content-Length")
            if content_length and int(content_length) > MAX_DATASET_BYTES:
                raise RuntimeError("Upstream dataset exceeds the 50 MiB safety limit")
            downloaded = 0
            while chunk := response.read(1024 * 1024):
                downloaded += len(chunk)
                if downloaded > MAX_DATASET_BYTES:
                    raise RuntimeError("Upstream dataset exceeds the 50 MiB safety limit")
                output.write(chunk)
        temporary.replace(cache_path)
    except (OSError, RuntimeError, ValueError, urllib.error.URLError) as error:
        temporary.unlink(missing_ok=True)
        raise RuntimeError(f"Could not download dataset from {DATASET_URL}: {error}") from error
    return cache_path


def validate_dataset(data: Any, path: Path) -> list[dict[str, Any]]:
    if not isinstance(data, list):
        raise RuntimeError(f"Expected a JSON array in {path}")
    for index, record in enumerate(data, start=1):
        if not isinstance(record, dict):
            raise RuntimeError(f"Invalid record {index} in {path}: expected an object")
        for field in ("id", "name", "body_part", "equipment", "target", "image", "gif_url"):
            if not isinstance(record.get(field), str):
                raise RuntimeError(f"Invalid record {index} in {path}: {field} must be a string")
        instructions = record.get("instructions", {})
        if not isinstance(instructions, dict):
            raise RuntimeError(f"Invalid record {index} in {path}: instructions must be an object")
        for language, instruction in instructions.items():
            if not isinstance(language, str) or not isinstance(instruction, str):
                raise RuntimeError(f"Invalid record {index} in {path}: instructions values must be strings")
        instruction_steps = record.get("instruction_steps", {})
        if not isinstance(instruction_steps, dict):
            raise RuntimeError(f"Invalid record {index} in {path}: instruction_steps must be an object")
        for language, steps in instruction_steps.items():
            if not isinstance(language, str) or not isinstance(steps, list) or not all(isinstance(step, str) for step in steps):
                raise RuntimeError(f"Invalid record {index} in {path}: instruction_steps.{language} must be an array of strings")
        secondary_muscles = record.get("secondary_muscles", [])
        if not isinstance(secondary_muscles, list) or not all(isinstance(muscle, str) for muscle in secondary_muscles):
            raise RuntimeError(f"Invalid record {index} in {path}: secondary_muscles must be an array of strings")
    return data


def load_dataset(explicit_path: str | None, refresh: bool) -> tuple[list[dict[str, Any]], Path]:
    if explicit_path and not Path(explicit_path).expanduser().is_file():
        raise RuntimeError(f"Explicit dataset path does not exist: {explicit_path}")
    path = find_local_dataset(explicit_path) or download_dataset(refresh)
    try:
        if path.stat().st_size > MAX_DATASET_BYTES:
            raise RuntimeError(f"Dataset exceeds the 50 MiB safety limit: {path}")
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Could not read valid JSON from {path}: {error}") from error
    return validate_dataset(data, path), path


def resolve_filter(kind: str, value: str | None) -> set[str] | None:
    if not value:
        return None
    normalized = normalize(value)
    aliases = FILTER_ALIASES[kind]
    if normalized in aliases:
        return set(aliases[normalized])
    return {normalize(item) for item in value.split(",") if normalize(item)}


def matches_filters(exercise: dict[str, Any], filters: dict[str, set[str] | None]) -> bool:
    return all(not accepted or normalize(exercise.get(field)) in accepted for field, accepted in filters.items())


def score_exercise(exercise: dict[str, Any], query: str, terms: Iterable[str], language: str) -> float:
    if not query.strip():
        return 1.0
    name = normalize(exercise.get("name"))
    fields = {
        "name": name,
        "target": normalize(exercise.get("target")),
        "body_part": normalize(exercise.get("body_part")),
        "equipment": normalize(exercise.get("equipment")),
        "muscle_group": normalize(exercise.get("muscle_group")),
        "secondary": normalize(" ".join(exercise.get("secondary_muscles") or [])),
        "instructions": normalize((exercise.get("instructions") or {}).get(language, "")),
    }
    weights = {"name": 8.0, "target": 6.0, "body_part": 5.0, "equipment": 5.0, "muscle_group": 3.0, "secondary": 2.0, "instructions": 0.5}
    score = 0.0
    for term in terms:
        for field, value in fields.items():
            if term == value:
                score += weights[field] * 1.5
            elif (term in value.split()) if term.isascii() else (term in value):
                score += weights[field]
    expanded = expand_query(query)
    if expanded == name:
        score += 40.0
    elif expanded and expanded in name:
        score += 12.0
    score += SequenceMatcher(None, expanded, name).ratio() * 3.0
    return score


def media_url(path: str | None) -> str | None:
    if not path:
        return None
    return f"{RAW_ROOT}/{quote(path, safe='/')}"


def markdown_text(value: Any) -> str:
    return re.sub(r"([\\`*_[\]<>])", r"\\\1", str(value or ""))


def compact_result(exercise: dict[str, Any], score: float, language: str) -> dict[str, Any]:
    steps_by_language = exercise.get("instruction_steps") or {}
    steps = steps_by_language.get(language) or []
    if not steps:
        instruction = (exercise.get("instructions") or {}).get(language, "")
        steps = [part.strip() for part in re.split(r"(?<=[.!?。！？])\s*", instruction) if part.strip()]
    return {
        "id": exercise.get("id"),
        "name": exercise.get("name"),
        "body_part": exercise.get("body_part"),
        "target": exercise.get("target"),
        "equipment": exercise.get("equipment"),
        "muscle_group": exercise.get("muscle_group"),
        "secondary_muscles": exercise.get("secondary_muscles") or [],
        "steps": steps,
        "image_url": media_url(exercise.get("image")),
        "gif_url": media_url(exercise.get("gif_url")),
        "attribution": exercise.get("attribution") or "© Gym visual — https://gymvisual.com/",
        "source": REPOSITORY_URL,
        "relevance_score": round(score, 2),
    }


def search(data: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    filters = {
        "body_part": resolve_filter("body_part", args.body_part),
        "equipment": resolve_filter("equipment", args.equipment),
        "target": resolve_filter("target", args.target),
    }
    terms = query_terms(args.query)
    ranked = []
    for exercise in data:
        if not matches_filters(exercise, filters):
            continue
        score = score_exercise(exercise, args.query, terms, args.lang)
        if args.query.strip() and score <= 1.0:
            continue
        ranked.append((score, normalize(exercise.get("name")), exercise))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [compact_result(exercise, score, args.lang) for score, _, exercise in ranked[: args.limit]]


def print_markdown(results: list[dict[str, Any]], args: argparse.Namespace, dataset_path: Path) -> None:
    print("# Exercise matches\n")
    print(f"- Query: `{markdown_text(args.query or '(filters only)')}`")
    print(f"- Language: `{args.lang}`")
    print(f"- Dataset: `{markdown_text(dataset_path)}`\n")
    for index, result in enumerate(results, start=1):
        print(f"## {index}. {markdown_text(result['name'])}\n")
        print(f"- Body part: {markdown_text(result['body_part'])}")
        print(f"- Target: {markdown_text(result['target'])}")
        print(f"- Equipment: {markdown_text(result['equipment'])}")
        if result["secondary_muscles"]:
            print(f"- Secondary muscles: {markdown_text(', '.join(result['secondary_muscles']))}")
        print(f"- [Animation GIF]({result['gif_url']}) · [Thumbnail]({result['image_url']})")
        print(f"- Attribution: {markdown_text(result['attribution'])}\n")
        for step_number, step in enumerate(result["steps"], start=1):
            print(f"{step_number}. {markdown_text(step)}")
        print()
    print(f"Source: {REPOSITORY_URL}\n")
    print("> Reference only. Stop if an exercise causes pain; seek qualified guidance for injuries or medical conditions.")


def print_values(data: list[dict[str, Any]]) -> None:
    values = {
        field: sorted({str(item.get(field, "")) for item in data if item.get(field)})
        for field in ("body_part", "equipment", "target")
    }
    print(json.dumps(values, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="", help="Natural-language search query")
    parser.add_argument("--body-part", help="Exact body-part filter; Chinese aliases are accepted")
    parser.add_argument("--equipment", help="Exact equipment filter; Chinese aliases are accepted")
    parser.add_argument("--target", help="Exact target-muscle filter; Chinese aliases are accepted")
    parser.add_argument("--lang", choices=LANGUAGES, default="en", help="Instruction language")
    parser.add_argument("--limit", type=int, default=5, help="Maximum results, from 1 to 20")
    parser.add_argument("--format", choices=("json", "markdown"), default="json", help="Output format")
    parser.add_argument("--dataset", help="Path to a local exercises.json file")
    parser.add_argument("--refresh", action="store_true", help="Refresh the temporary downloaded dataset")
    parser.add_argument("--list-values", action="store_true", help="Print canonical filter values and exit")
    args = parser.parse_args()
    if not 1 <= args.limit <= 20:
        parser.error("--limit must be between 1 and 20")
    return args


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = parse_args()
    try:
        data, dataset_path = load_dataset(args.dataset, args.refresh)
        if args.list_values:
            print_values(data)
            return 0
        results = search(data, args)
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    if not results:
        print("No matching exercises found. Relax one filter or use --list-values.", file=sys.stderr)
        return 1
    if args.format == "markdown":
        print_markdown(results, args, dataset_path)
    else:
        payload = {
            "query": args.query,
            "language": args.lang,
            "filters": {"body_part": args.body_part, "equipment": args.equipment, "target": args.target},
            "count": len(results),
            "dataset_source": REPOSITORY_URL,
            "results": results,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
