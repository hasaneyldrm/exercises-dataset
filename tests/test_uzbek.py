"""Data integrity tests for the Uzbek localization overlay.

Run: python3 -m unittest discover -s tests
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class UzbekDatasetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = load("data/exercises.json")
        cls.overlay = load("data/exercises_uz.json")
        cls.dictionary = load("data/uzbek_dictionary.json")
        cls.sample = load("data/exercises_uz_sample.json")
        cls.schema = load("data/exercises.schema.json")

    def test_one_overlay_per_source_record(self):
        source_ids = [x["id"] for x in self.source]
        overlay_ids = [x["id"] for x in self.overlay]
        self.assertEqual(len(source_ids), 1324)
        self.assertEqual(len(source_ids), len(set(source_ids)))
        self.assertEqual(source_ids, overlay_ids)

    def test_metadata_is_fully_covered(self):
        for ex, uz in zip(self.source, self.overlay):
            for field, dictionary in (
                ("category", "categories"), ("body_part", "body_parts"),
                ("equipment", "equipment"), ("muscle_group", "secondary_muscles"),
                ("target", "targets")
            ):
                with self.subTest(id=ex["id"], field=field):
                    self.assertEqual(uz[field + "_uz"], self.dictionary[dictionary][ex[field]])
            self.assertEqual(uz["secondary_muscles_uz"], [
                self.dictionary["secondary_muscles"][x] for x in ex["secondary_muscles"]
            ])

    def test_uzbek_instructions_are_consistent(self):
        with_steps = 0
        for ex, uz in zip(self.source, self.overlay):
            if "instruction_steps_uz" not in uz:
                self.assertNotIn("instructions_uz", uz)
                continue
            with_steps += 1
            steps = uz["instruction_steps_uz"]
            self.assertEqual(len(steps), len(ex["instruction_steps"]["en"]))
            self.assertTrue(all(isinstance(step, str) and step.strip() for step in steps))
            self.assertEqual(uz["instructions_uz"], " ".join(steps))
            self.assertFalse(re.search(r"[\u0400-\u052f]", uz["instructions_uz"]))
            self.assertTrue(uz["name_uz"])
        self.assertEqual(with_steps, 2)

    def test_samples_preserve_source_fields(self):
        orig = {ex["id"]: ex for ex in self.source}
        for sample in self.sample:
            en = orig[sample["id"]]
            for field in en:
                if field not in ("instructions", "instruction_steps"):
                    self.assertEqual(sample[field], en[field])
            for lang, text in en["instructions"].items():
                self.assertEqual(sample["instructions"][lang], text)
            for lang, steps in en["instruction_steps"].items():
                self.assertEqual(sample["instruction_steps"][lang], steps)

    def test_schema_keeps_original_formats(self):
        props = self.schema["$defs"]["exercise"]["properties"]
        self.assertEqual(props["name"]["type"], "string")
        self.assertEqual(props["instructions"]["$ref"], "#/$defs/languageMap")
        self.assertEqual(props["instruction_steps"]["$ref"], "#/$defs/languageStepsMap")
        self.assertIn("uz", self.schema["$defs"]["languageMap"]["properties"])
        self.assertIn("uz", self.schema["$defs"]["languageStepsMap"]["properties"])
        self.assertNotIn("uz", self.schema["$defs"]["languageMap"]["required"])


if __name__ == "__main__":
    unittest.main()
