// Validates data/exercises.json: JSON Schema, media file existence,
// duplicate ids, and sync with the copy of the data embedded in index.html.
import Ajv2020 from "ajv/dist/2020.js";
import addFormats from "ajv-formats";
import { existsSync, readFileSync } from "node:fs";
import assert from "node:assert/strict";

const errors = [];
const section = (title, fn) => {
  console.log(`\n— ${title}`);
  const before = errors.length;
  fn();
  if (errors.length === before) console.log("  ok");
};

function readJson(path) {
  const text = readFileSync(path, "utf8");
  try {
    return JSON.parse(text);
  } catch (e) {
    errors.push(`Failed to parse ${path}: ${e.message}`);
    return null;
  }
}

const schema = readJson("data/exercises.schema.json");
const exercises = readJson("data/exercises.json");

section("JSON Schema validation", () => {
  if (!schema || !exercises) {
    errors.push("skipped: schema or dataset failed to parse (see above)");
    return;
  }
  let validate;
  try {
    const ajv = new Ajv2020({ allErrors: true, strict: true });
    addFormats(ajv);
    validate = ajv.compile(schema);
  } catch (e) {
    errors.push(`Failed to compile data/exercises.schema.json: ${e.message}`);
    return;
  }
  if (!validate(exercises)) {
    for (const err of validate.errors) {
      errors.push(`schema: ${err.instancePath || "/"} ${err.message}`);
    }
  }
});

section("Duplicate ids", () => {
  if (!exercises) return errors.push("skipped: data/exercises.json failed to parse (see above)");
  const seen = new Map();
  for (const ex of exercises) {
    seen.set(ex.id, (seen.get(ex.id) ?? 0) + 1);
  }
  for (const [id, count] of seen) {
    if (count > 1) errors.push(`duplicate id "${id}" appears ${count} times`);
  }
});

section("Image files exist", () => {
  if (!exercises) return errors.push("skipped: data/exercises.json failed to parse (see above)");
  for (const ex of exercises) {
    if (typeof ex.image !== "string") errors.push(`id ${ex.id}: "image" is missing or not a string`);
    else if (!existsSync(ex.image)) errors.push(`id ${ex.id}: missing image file "${ex.image}"`);
  }
});

section("GIF files exist", () => {
  if (!exercises) return errors.push("skipped: data/exercises.json failed to parse (see above)");
  for (const ex of exercises) {
    if (typeof ex.gif_url !== "string") errors.push(`id ${ex.id}: "gif_url" is missing or not a string`);
    else if (!existsSync(ex.gif_url)) errors.push(`id ${ex.id}: missing gif file "${ex.gif_url}"`);
  }
});

section("index.html data is in sync with data/exercises.json", () => {
  if (!exercises) return errors.push("skipped: data/exercises.json failed to parse (see above)");
  const html = readFileSync("index.html", "utf8");
  const arrayText = extractJsonArray(html, "const EXERCISES = ");
  if (!arrayText) {
    errors.push("could not find \"const EXERCISES = [...]\" in index.html");
    return;
  }
  let embedded;
  try {
    embedded = JSON.parse(arrayText);
  } catch (e) {
    errors.push(`embedded EXERCISES array in index.html is not valid JSON: ${e.message}`);
    return;
  }
  try {
    assert.deepStrictEqual(embedded, exercises);
  } catch {
    errors.push(
      "index.html's embedded EXERCISES array does not match data/exercises.json — " +
      "regenerate index.html from the current dataset."
    );
  }
});

if (errors.length) {
  console.log(`\n${errors.length} problem(s) found:\n`);
  for (const e of errors) console.log(`  ✗ ${e}`);
  process.exitCode = 1;
} else {
  console.log("\nAll checks passed.");
}

// Returns the substring of `text` holding the JSON array that starts right
// after `marker`, found by bracket-depth counting (so it doesn't care
// whether the array is minified onto one line or pretty-printed).
function extractJsonArray(text, marker) {
  const markerIdx = text.indexOf(marker);
  if (markerIdx === -1) return null;
  const start = text.indexOf("[", markerIdx);
  if (start === -1) return null;

  let depth = 0;
  let inString = false;
  let escaped = false;
  for (let i = start; i < text.length; i++) {
    const ch = text[i];
    if (inString) {
      if (escaped) escaped = false;
      else if (ch === "\\") escaped = true;
      else if (ch === '"') inString = false;
      continue;
    }
    if (ch === '"') inString = true;
    else if (ch === "[" || ch === "{") depth++;
    else if (ch === "]" || ch === "}") {
      depth--;
      if (depth === 0) return text.slice(start, i + 1);
    }
  }
  return null;
}
