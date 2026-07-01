import json

DATA_DIR = "data"
HTML_FILE = "index.html"

with open(f"{DATA_DIR}/exercises.json") as f:
    exercises = json.load(f)

with open(HTML_FILE) as f:
    html = f.read()

exercises_json_str = json.dumps(exercises, ensure_ascii=False, indent=2)

marker_start = "const EXERCISES = ["
marker_end = "];"

idx_start = html.find(marker_start)
if idx_start == -1:
    print("ERROR: could not find EXERCISES array start")
    exit(1)

# find the closing ]; after the array
idx_end = html.find(marker_end, idx_start + len(marker_start))
if idx_end == -1:
    print("ERROR: could not find EXERCISES array end")
    exit(1)
idx_end += len(marker_end)  # include the ];

new_html = html[:idx_start] + f"const EXERCISES = {exercises_json_str};" + html[idx_end:]

with open(HTML_FILE, "w") as f:
    f.write(new_html)

# count to verify
start_line = html[:idx_start].count("\n") + 1
end_line = html[:idx_end].count("\n") + 1
print(f"Replaced inline EXERCISES array (lines {start_line}–{end_line}) with {len(exercises)} exercises from data/exercises.json")
