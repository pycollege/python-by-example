# Python by Example: Dictionaries

Dictionaries store key-value pairs—like a real dictionary maps words to definitions. Keys must be hashable (strings, numbers, tuples); values can be anything. Use them when you need fast lookup by name or ID. Lookup is typically O(1). Curly braces `{}` create dicts; colons separate keys from values.

**What you'll learn:**
- Creating and accessing dicts
- `.get()` for safe access with a default
- Adding and updating keys
- Iterating with `.items()`

```python
# Create a dict
person = {"name": "Alice", "age": 30, "city": "Paris"}
print(person)

# Access by key
print(person["name"])

# Safe access with .get()
print(person.get("country", "unknown"))

# Add or update
person["email"] = "alice@example.com"
person["age"] = 31
print(person)

# Keys, values, items
print(person.keys())
print(person.values())
for k, v in person.items():
    print(k, v)
```

`person["name"]` raises `KeyError` if the key is missing. `person.get("country", "unknown")` returns `"unknown"` instead. Use `.get()` when the key might not exist.

To run this program:

```bash
$ python source/dictionaries.py
{'name': 'Alice', 'age': 30, 'city': 'Paris'}
Alice
unknown
{'name': 'Alice', 'age': 31, 'city': 'Paris', 'email': 'alice@example.com'}
dict_keys(['name', 'age', 'city', 'email'])
dict_values(['Alice', 31, 'Paris', 'alice@example.com'])
name Alice
age 31
city Paris
email alice@example.com
```

**Tip:** Prefer `.get(key, default)` over `dict[key]` when the key might be missing—it avoids crashes.

**Try it:** Create a dict of your favorite things (e.g., color, food) and print one value.

Source: [dictionaries.py](../source/dictionaries.py)

Next: [Sets](sets.md)
