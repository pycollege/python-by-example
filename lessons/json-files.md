# Python by Example: JSON Files

Reading and writing JSON files is common—config files, caches, API responses. Use `json.load()` to read from a file object and `json.dump()` to write. Both handle encoding. Use a context manager (`with`) so the file is closed properly.

**What you'll learn:**
- `json.dump()` — write Python object to file
- `json.load()` — read file into Python object

```python
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
```

`dump` and `load` work with file objects; `dumps` and `loads` work with strings. Use `indent` when writing for readability.

To run this program:

```bash
$ python source/json-files.py
{'name': 'Alice', 'scores': [85, 90, 78]}
```

**Tip:** For large files, consider `ijson` or streaming. For config, `json.load()` is usually sufficient.

**Try it:** Write a dict to a file, close it, then read it back and verify the data.

Source: [json-files.py](../source/json-files.py)

Next: [Time](time.md)
