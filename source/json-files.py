import json
import tempfile
import os

# Write to a file
data = {"name": "Alice", "scores": [85, 90, 78]}
with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
    json.dump(data, f, indent=2)
    path = f.name

# Read from file
with open(path) as f:
    loaded = json.load(f)
print(loaded)
os.unlink(path)
