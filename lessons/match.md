# Python by Example: Match

Structural pattern matching (Python 3.10+) lets you match values against patterns—not just equality. It replaces long `if/elif` chains with clearer, more expressive code. You can match literals, sequences, dictionaries, and more. The `_` pattern matches anything (like a default case).

**What you'll learn:**
- `match` and `case` syntax
- Matching literals, sequences, and dicts
- The wildcard `_` for "anything else"

```python
def describe(value):
    match value:
        case 0:
            return "zero"
        case 1 | 2:
            return "one or two"
        case [x, y]:
            return f"a pair: {x}, {y}"
        case {"name": n}:
            return f"dict with name: {n}"
        case _:
            return "something else"

print(describe(0))
print(describe(1))
print(describe([10, 20]))
print(describe({"name": "Alice"}))
print(describe(99))
```

`case 1 | 2` matches either 1 or 2. `case [x, y]` matches a two-element list and binds the elements. `case {"name": n}` matches a dict with a `"name"` key. `case _` catches everything else.

To run this program:

```bash
$ python source/match.py
zero
one or two
a pair: 10, 20
dict with name: Alice
something else
```

**Tip:** Match requires Python 3.10 or later. Check with `python --version`.

**Try it:** Add a new case for a three-element list `[a, b, c]`.

Source: [match.py](../source/match.py)

Next: [Break and Continue](break-and-continue.md)
