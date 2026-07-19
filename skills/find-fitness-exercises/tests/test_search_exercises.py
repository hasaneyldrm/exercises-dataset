import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace


SCRIPT = Path(__file__).parents[1] / "scripts" / "search_exercises.py"
SPEC = importlib.util.spec_from_file_location("search_exercises", SCRIPT)
search_exercises = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(search_exercises)


def exercise(**overrides):
    record = {
        "id": "1",
        "name": "dumbbell bench press",
        "body_part": "chest",
        "category": "chest",
        "equipment": "dumbbell",
        "target": "pectorals",
        "muscle_group": "triceps",
        "secondary_muscles": ["triceps", "delts"],
        "instructions": {"en": "Press the dumbbells.", "zh": "向上推起哑铃。"},
        "instruction_steps": {"en": ["Press the dumbbells."], "zh": ["向上推起哑铃。"]},
        "image": "images/1.jpg",
        "gif_url": "videos/1.gif",
        "attribution": "© Gym visual — https://gymvisual.com/",
    }
    record.update(overrides)
    return record


class ExerciseSearchTests(unittest.TestCase):
    def test_chinese_aliases_apply_hard_filters_and_select_chinese_steps(self):
        data = [
            exercise(),
            exercise(id="2", name="barbell bench press", equipment="barbell"),
            exercise(id="3", name="dumbbell curl", body_part="upper arms", category="upper arms", target="biceps"),
        ]
        args = SimpleNamespace(
            query="哑铃练胸",
            body_part="胸部",
            equipment="哑铃",
            target=None,
            lang="zh",
            limit=5,
        )

        results = search_exercises.search(data, args)

        self.assertEqual([result["id"] for result in results], ["1"])
        self.assertEqual(results[0]["steps"], ["向上推起哑铃。"])

    def test_common_chinese_exercise_name_ranks_matching_name_first(self):
        data = [
            exercise(id="1", name="push-up", equipment="body weight"),
            exercise(id="2", name="dumbbell bench press"),
            exercise(
                id="3",
                name="elbow lift - reverse push-up",
                equipment="body weight",
                body_part="back",
                target="upper back",
            ),
        ]
        args = SimpleNamespace(
            query="俯卧撑",
            body_part=None,
            equipment=None,
            target=None,
            lang="zh",
            limit=5,
        )

        results = search_exercises.search(data, args)

        self.assertEqual(results[0]["name"], "push-up")

    def test_malformed_custom_dataset_is_rejected_at_load_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "exercises.json"
            path.write_text(json.dumps(["not an exercise record"]), encoding="utf-8")

            with self.assertRaisesRegex(RuntimeError, "record 1"):
                search_exercises.load_dataset(str(path), refresh=False)

    def test_malformed_nested_steps_are_rejected_at_load_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "exercises.json"
            record = exercise(instruction_steps={"en": "not a list"})
            path.write_text(json.dumps([record]), encoding="utf-8")

            with self.assertRaisesRegex(RuntimeError, "instruction_steps.en"):
                search_exercises.load_dataset(str(path), refresh=False)

    def test_missing_explicit_dataset_does_not_silently_fall_back(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.json"

            with self.assertRaisesRegex(RuntimeError, "does not exist"):
                search_exercises.load_dataset(str(missing), refresh=False)

    def test_leg_alias_expands_to_upper_and_lower_leg_filters(self):
        self.assertEqual(
            search_exercises.resolve_filter("body_part", "腿"),
            {"upper legs", "lower legs"},
        )

    def test_bodyweight_alias_resolves_to_dataset_equipment_value(self):
        self.assertEqual(
            search_exercises.resolve_filter("equipment", "bodyweight"),
            {"body weight"},
        )

    def test_media_path_is_url_encoded(self):
        self.assertEqual(
            search_exercises.media_url("images/example image.jpg"),
            f"{search_exercises.RAW_ROOT}/images/example%20image.jpg",
        )


if __name__ == "__main__":
    unittest.main()
