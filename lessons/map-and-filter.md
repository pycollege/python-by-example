# Python by Example: Map and Filter

`map()` applies a function to every element of an iterable; `filter()` keeps only elements for which a function returns `True`. Both return iterators—wrap them in `list()` to materialize the result. List comprehensions often read more clearly, but `map` and `filter` appear frequently in existing Python code.

**What you'll learn:**
- `map()` to transform elements
- `filter()` to select elements
- Equivalent list comprehensions

```python
numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


def square(x):
    return x ** 2


print(list(map(square, numbers)))

# Equivalent list comprehensions
print([x * 2 for x in numbers])
print([x for x in numbers if x % 2 == 0])
```

`map(f, iterable)` is equivalent to `(f(x) for x in iterable)`. `filter(f, iterable)` is equivalent to `(x for x in iterable if f(x))`. Named functions work just as well as lambdas.

To run this program:

```bash
$ python source/map-and-filter.py
[2, 4, 6, 8, 10]
[2, 4]
[1, 4, 9, 16, 25]
[2, 4, 6, 8, 10]
[2, 4]
```

**Tip:** Prefer list comprehensions when the logic is simple—they're more readable. Use `map`/`filter` when you already have a named function and don't want to repeat it in a comprehension.

**Try it:** Use `map()` to convert a list of strings to integers.

Source: [map-and-filter.py](../source/map-and-filter.py)

Next: [Closures](closures.md)
