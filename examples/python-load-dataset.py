import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "exercises.json"


with DATA_PATH.open(encoding="utf-8") as file:
    exercises = json.load(file)

by_body_part = Counter(exercise["body_part"] for exercise in exercises)
bodyweight = [
    exercise for exercise in exercises
    if exercise["equipment"] == "body weight"
]

print(f"Total exercises: {len(exercises)}")
print(f"Bodyweight exercises: {len(bodyweight)}")
print("Exercises by body part:")

for body_part, count in by_body_part.most_common():
    print(f"- {body_part}: {count}")

print("\nFirst exercise media attribution:")
print(exercises[0]["attribution"])
