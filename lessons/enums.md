# Python by Example: Enums

Enums define a fixed set of named constants. They're type-safe and self-documenting—better than magic numbers or strings. Use them for states, choices, categories, or any fixed set of options. The `enum` module provides `Enum`; use `IntEnum` if you need values that compare with plain integers.

**What you'll learn:**
- Defining an enum with `class Name(Enum):`
- Accessing members and values
- Iterating and comparing

```python
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.RED.value)
print(Color(2))


# Iterate
for c in Color:
    print(c.name, c.value)


# Compare by identity
if Color.RED == Color.RED:
    print("Same color")
```

`Color.RED` is the enum member; `Color.RED.value` is 1. `Color(2)` looks up the member with value 2. Compare enum members with `==`; they're singletons.

To run this program:

```bash
$ python source/enums.py
Color.RED
1
Color.GREEN
RED 1
GREEN 2
BLUE 3
Same color
```

**Tip:** Use enums instead of strings like `"red"` or numbers like `1` when the set of values is fixed—IDEs and type checkers can help catch errors.

**Try it:** Create an enum for days of the week and print each.

Source: [enums.py](../source/enums.py)

Next: [Type Hints](type-hints.md)
