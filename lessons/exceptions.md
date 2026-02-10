# Python by Example: Exceptions

Exceptions handle errors gracefully. Use `try`/`except` to catch them; use `raise` to signal them. `else` runs only when no exception occurred; `finally` always runs (e.g., for cleanup). Catch specific exception types when you can—avoid bare `except:` which catches everything including `KeyboardInterrupt`.

**What you'll learn:**
- `try`, `except`, `else`, `finally`
- Catching specific exceptions
- Raising exceptions with `raise`

```python
try:
    result = 10 / 2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division succeeded")
finally:
    print("Done")

# Raising exceptions
def get_item(lst, index):
    if index < 0 or index >= len(lst):
        raise IndexError(f"Index {index} out of range")
    return lst[index]

try:
    get_item([1, 2, 3], 10)
except IndexError as e:
    print(f"Caught: {e}")
```

`except IndexError as e` captures the exception object so you can inspect it. The `else` block runs only if no exception was raised in `try`. `finally` runs whether or not an exception occurred.

To run this program:

```bash
$ python source/exceptions.py
5.0
Division succeeded
Done
Caught: Index 10 out of range
```

**Tip:** Prefer specific exceptions (`except ValueError`) over broad ones (`except Exception`). It prevents masking bugs.

**Try it:** Wrap a division in try/except and handle both `ZeroDivisionError` and `TypeError`.

Source: [exceptions.py](../source/exceptions.py)

Next: [Custom Exceptions](custom-exceptions.md)
