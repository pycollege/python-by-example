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
