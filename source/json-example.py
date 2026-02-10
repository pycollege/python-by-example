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
