# Python by Example: Dataclasses

Dataclasses (Python 3.7+) reduce boilerplate for classes that mainly hold data. The `@dataclass` decorator auto-generates `__init__`, `__repr__`, and more from typed fields. Use them instead of plain classes when you're mostly storing attributes with minimal logic. Add `frozen=True` for immutability.

**What you'll learn:**
- Using `@dataclass` for data containers
- Typed fields and default values
- Less code, same behavior

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


p = Point(3.0, 4.0)
print(p)
print(p.x, p.y)


@dataclass
class Person:
    name: str
    age: int = 0  # default value


alice = Person("Alice", 30)
bob = Person("Bob")  # age defaults to 0
print(alice)
print(bob)
```

Without `@dataclass`, you'd write `__init__`, `__repr__`, and more by hand. The decorator generates them from the field declarations. Defaults go after required fields.

To run this program:

```bash
$ python source/dataclasses.py
Point(x=3.0, y=4.0)
3.0 4.0
Person(name='Alice', age=30)
Person(name='Bob', age=0)
```

**Tip:** Use dataclasses for config objects, records, and DTOs. Use regular classes when you have complex behavior.

**Try it:** Add a `@dataclass` for a `Rectangle` with `width` and `height`, and a method that returns the area.

Source: [dataclasses.py](../source/dataclasses.py)

Next: [Enums](enums.md)
