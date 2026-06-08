# Python by Example: Generators

Generators produce values one at a time using `yield`. Unlike a list, a generator doesn't compute all values upfront—it yields each one on demand, making them memory-efficient for large or infinite sequences. A generator function looks like a normal function but uses `yield` instead of `return`.

**What you'll learn:**
- Defining generator functions with `yield`
- Advancing with `next()`
- Generator expressions (like list comprehensions, but lazy)
- Infinite generators

```python
def count_up(n):
    for i in range(n):
        yield i


gen = count_up(3)
print(next(gen))
print(next(gen))
print(next(gen))

for value in count_up(5):
    print(value)

# Generator expression—like a list comprehension but lazy
squares = (x**2 for x in range(5))
print(list(squares))


def integers():
    n = 0
    while True:
        yield n
        n += 1


gen = integers()
print([next(gen) for _ in range(5)])
```

Each call to `next()` resumes the function from where it last yielded. When the function returns, the generator raises `StopIteration`—a `for` loop handles this automatically. The `integers()` generator is infinite but safe because we only pull five values.

To run this program:

```bash
$ python source/generators.py
0
1
2
0
1
2
3
4
[0, 1, 4, 9, 16]
[0, 1, 2, 3, 4]
```

**Tip:** Prefer a generator expression `(x for x in ...)` over `list(...)` when you only iterate once—you skip building the entire list in memory.

**Try it:** Write a generator that yields Fibonacci numbers indefinitely.

Source: [generators.py](../source/generators.py)

Next: [Classes](classes.md)
