# Python by Example: Range and Enumerate

`range()` produces a sequence of integers without building a list in memory—it's lazy and efficient. Use it when you need to loop a fixed number of times or generate indices. `enumerate()` pairs each element with its index, so you get both when iterating. Both work in `for` loops.

**What you'll learn:**
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- `enumerate(iterable, start=0)` for index-value pairs

```python
# range(stop) — 0 to stop-1
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
for i in range(2, 6):
    print(i, end=" ")
print()

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# enumerate: index and value
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# Start counting from 1
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
```

`range(5)` yields 0, 1, 2, 3, 4—stop is exclusive. `enumerate(fruits)` yields (0, "apple"), (1, "banana"), (2, "cherry"). Use `start=1` when you want 1-based numbering for display.

To run this program:

```bash
$ python source/range-and-enumerate.py
0 1 2 3 4
2 3 4 5
0 2 4 6 8
0: apple
1: banana
2: cherry
1. apple
2. banana
3. cherry
```

**Tip:** Prefer `for i, item in enumerate(items):` over `for i in range(len(items)):` when you need the index—it's cleaner and less error-prone.

**Try it:** Use `enumerate` to print a numbered list of your favorite colors.

Source: [range-and-enumerate.py](../source/range-and-enumerate.py)

Next: [Comprehensions](comprehensions.md)
