# Python by Example: Comprehensions

Comprehensions build lists, dicts, or sets in a compact, readable way. Instead of a loop with `append`, you write the transformation in one line. They're idiomatic Python—you'll see them everywhere. List comprehensions are most common; dict and set comprehensions follow the same pattern.

**What you'll learn:**
- List: `[expr for x in iterable]`
- With condition: `[expr for x in iterable if condition]`
- Dict: `{key: value for x in iterable}`
- Set: `{expr for x in iterable}`

```python
# List comprehension
squares = [x**2 for x in range(5)]
print(squares)

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Dict comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(word_lengths)

# Set comprehension
unique_lengths = {len(word) for word in ["apple", "banana", "apple"]}
print(unique_lengths)

# Nested
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)
```

The general form is `[expression for item in iterable if condition]`. Dict uses `{key: value}`; set uses `{expression}`. Nested comprehensions build nested structures.

To run this program:

```bash
$ python source/comprehensions.py
[0, 1, 4, 9, 16]
[0, 2, 4, 6, 8]
{'apple': 5, 'banana': 6, 'cherry': 6}
{5, 6}
[[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

**Tip:** Keep comprehensions readable. If they get long or complex, use a regular loop instead.

**Try it:** Use a list comprehension to get the uppercase version of each string in a list.

Source: [comprehensions.py](../source/comprehensions.py)

Next: [Classes](classes.md)
