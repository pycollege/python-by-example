# Python by Example: Lambdas

Lambdas are small anonymous functions—they have no name and can only contain a single expression. Use them when you need a simple function inline, e.g., as the `key` for `sorted` or as an argument to `map` or `filter`. For anything more complex, use a regular `def` function.

**What you'll learn:**
- Lambda syntax: `lambda x: x * 2`
- Using lambdas with `sorted`, `map`, `filter`
- When to prefer a named function

```python
# Lambda: one expression, no statements
double = lambda x: x * 2
print(double(5))

# Common use: sorting
pairs = [(1, "one"), (3, "three"), (2, "two")]
sorted_by_num = sorted(pairs, key=lambda p: p[0])
sorted_by_word = sorted(pairs, key=lambda p: p[1])
print(sorted_by_num)
print(sorted_by_word)

# map and filter
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(squared)
print(evens)
```

The `key` in `sorted` is a function applied to each item; sorting uses the result. `map` applies a function to each element; `filter` keeps only elements where the function returns True.

To run this program:

```bash
$ python source/lambdas.py
10
[(1, 'one'), (2, 'two'), (3, 'three')]
[(1, 'one'), (2, 'two'), (3, 'three')]
[1, 4, 9, 16, 25]
[2, 4]
```

**Tip:** List comprehensions often replace `map` and `filter`: `[x**2 for x in nums]` instead of `map(lambda x: x**2, nums)`. Use whichever is clearer.

**Try it:** Use `sorted` with a lambda to sort a list of strings by length.

Source: [lambdas.py](../source/lambdas.py)

Next: [Closures](closures.md)
