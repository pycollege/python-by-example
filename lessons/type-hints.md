# Python by Example: Type Hints

Type hints annotate variables, parameters, and return values. They don't change runtime behavior—Python ignores them. But tools like mypy and IDEs use them to catch bugs and improve autocomplete. Hints are optional; add them gradually to existing code. Use `list[int]`, `dict[str, int]` (Python 3.9+); for older Python, use `List[int]` from `typing`.

**What you'll learn:**
- Annotating parameters and return values
- Generic types: `list[str]`, `dict[str, int]`
- `Optional` for values that can be `None`

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def process(items: list[str]) -> dict[str, int]:
    return {s: len(s) for s in items}


print(greet("Alice"))
print(add(2, 3))
print(process(["a", "bb", "ccc"]))


# Optional (can be None)
from typing import Optional


def find(items: list[str], target: str) -> Optional[int]:
    for i, x in enumerate(items):
        if x == target:
            return i
    return None
```

`Optional[int]` means `int | None`. In Python 3.10+, you can write `int | None` directly. Run `mypy script.py` to check types.

To run this program:

```bash
$ python source/type-hints.py
Hello, Alice!
5
{'a': 1, 'bb': 2, 'ccc': 3}
```

**Tip:** Start with function signatures—they give the biggest benefit. Add variable hints where they clarify tricky code.

**Try it:** Add type hints to a function you wrote earlier.

Source: [type-hints.py](../source/type-hints.py)

Next: [Exceptions](exceptions.md)
