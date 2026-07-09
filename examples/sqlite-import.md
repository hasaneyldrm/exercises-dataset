# SQLite import example

The dataset can be imported into SQLite by storing multilingual instructions and secondary muscles as JSON text columns.

## Minimal table

```sql
CREATE TABLE exercises (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  category TEXT,
  body_part TEXT,
  equipment TEXT,
  instructions TEXT,
  instruction_steps TEXT,
  muscle_group TEXT,
  secondary_muscles TEXT,
  target TEXT,
  image TEXT,
  gif_url TEXT,
  media_id TEXT,
  created_at TEXT,
  attribution TEXT
);
```

## Generate INSERT statements

Open `setup.html`, choose the SQLite tab, and click "Generate INSERT SQL". The generated file contains all 1,324 records and can be imported with:

```bash
sqlite3 exercises.db < exercises_insert_sqlite.sql
```

## Query examples

```sql
SELECT COUNT(*) FROM exercises;

SELECT name, target, equipment
FROM exercises
WHERE equipment = 'body weight'
ORDER BY name
LIMIT 20;

SELECT name, json_extract(instructions, '$.en') AS english_instructions
FROM exercises
WHERE id = '0001';
```

The media paths in `image` and `gif_url` point to files in this repository. Keep the `attribution` value with any exported records that include media references.
