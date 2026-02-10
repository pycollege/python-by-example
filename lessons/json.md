# Python by Example: JSON

JSON is a common format for exchanging data. Python's `json` module converts between Python objects and JSON strings. Dicts become JSON objects; lists become arrays; types map naturally. Use `json.dumps()` to serialize (Python to string) and `json.loads()` to deserialize (string to Python).

**What you'll learn:**
- `json.dumps()` — Python to JSON string
- `json.loads()` — JSON string to Python
- Pretty printing with `indent`

```python
import json

# Python dict to JSON string
data = {"name": "Alice", "age": 30, "tags": ["python", "json"]}
json_str = json.dumps(data)
print(json_str)

# JSON string to Python dict
parsed = json.loads(json_str)
print(parsed["name"])
print(parsed["tags"])

# Pretty print
print(json.dumps(data, indent=2))
```

JSON supports objects (dicts), arrays (lists), strings, numbers, booleans, and null (None). Custom classes need a custom encoder or conversion to dict first.

To run this program:

```bash
$ python source/json-example.py
{"name": "Alice", "age": 30, "tags": ["python", "json"]}
Alice
['python', 'json']
{
  "name": "Alice",
  "age": 30,
  "tags": [
    "python",
    "json"
  ]
}
```

**Tip:** Use `indent=2` when writing config files or debugging—it makes JSON human-readable.

**Try it:** Create a nested dict (e.g., person with address) and serialize it to JSON.

Source: [json-example.py](../source/json-example.py)

Next: [JSON Files](json-files.md)
