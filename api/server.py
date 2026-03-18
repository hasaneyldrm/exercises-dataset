import argparse
import json
from pathlib import Path

from flask import Flask, abort, jsonify, request, send_from_directory


ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = ROOT / "data" / "exercises.json"


def load_exercises() -> list[dict]:
    return json.loads(DATASET_PATH.read_text(encoding="utf-8"))


EXERCISES = load_exercises()
EXERCISES_BY_ID = {exercise["id"]: exercise for exercise in EXERCISES}

app = Flask(__name__)


@app.get("/")
def root() -> tuple[dict, int]:
    return {
        "name": "exercise-dataset-test-api",
        "endpoints": [
            "/health",
            "/stats",
            "/exercises?q=squat",
            "/exercises/<id>",
            "/images/<file>",
            "/videos/<file>",
        ],
    }, 200


@app.get("/health")
def health() -> tuple[dict, int]:
    return {"status": "ok", "exercise_count": len(EXERCISES)}, 200


@app.get("/stats")
def stats() -> tuple[dict, int]:
    return {
        "exercise_count": len(EXERCISES),
        "with_images": sum(1 for item in EXERCISES if item.get("image")),
        "with_gifs": sum(1 for item in EXERCISES if item.get("gif_url")),
    }, 200


@app.get("/exercises")
def list_exercises():
    q = request.args.get("q", "").strip().lower()
    body_part = request.args.get("body_part", "").strip().lower()
    equipment = request.args.get("equipment", "").strip().lower()
    target = request.args.get("target", "").strip().lower()
    limit = max(1, min(request.args.get("limit", default=20, type=int), 100))
    offset = max(0, request.args.get("offset", default=0, type=int))

    items = EXERCISES

    if q:
        items = [
            item
            for item in items
            if q in item["name"].lower()
            or q in item["target"].lower()
            or q in item["body_part"].lower()
            or q in item["equipment"].lower()
        ]
    if body_part:
        items = [item for item in items if item["body_part"].lower() == body_part]
    if equipment:
        items = [item for item in items if item["equipment"].lower() == equipment]
    if target:
        items = [item for item in items if item["target"].lower() == target]

    total = len(items)
    return jsonify(
        {
            "total": total,
            "offset": offset,
            "limit": limit,
            "items": items[offset : offset + limit],
        }
    )


@app.get("/exercises/<exercise_id>")
def get_exercise(exercise_id: str):
    exercise = EXERCISES_BY_ID.get(exercise_id)
    if not exercise:
        abort(404, description="Exercise not found")
    return jsonify(exercise)


@app.get("/images/<path:filename>")
def get_image(filename: str):
    return send_from_directory(ROOT / "images", filename)


@app.get("/videos/<path:filename>")
def get_video(filename: str):
    return send_from_directory(ROOT / "videos", filename)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Flask test API for the exercise dataset.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--debug", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
