# Python by Example: Tuples

Tuples are immutable sequences—once created, you can't change them. Use them for fixed data (e.g., coordinates), multiple return values, and as dictionary keys (lists can't be keys). They're faster and use less memory than lists for fixed-size data. Tuple unpacking lets you assign multiple variables in one line.

**What you'll learn:**
- Creating tuples with parentheses
- Tuple unpacking: `x, y = point`
- Single-element tuples need a trailing comma
- Returning multiple values from a function

```python
# Create tuples
point = (3, 4)
rgb = (255, 128, 0)

# Access by index
print(point[0], point[1])

# Tuple unpacking
x, y = point
print(x, y)

# Single-element tuple needs a trailing comma
single = (1,)
print(single)

# Tuples are immutable — this would error:
# point[0] = 5

# Return multiple values (as a tuple)
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([3, 1, 4, 1, 5])
print(low, high)
```

`(1,)` needs the comma—otherwise `(1)` is just the integer 1 in parentheses. When a function returns `a, b`, Python returns a tuple; you can unpack it directly.

To run this program:

```bash
$ python source/tuples.py
3 4
3 4
(1,)
1 5
```

**Tip:** Use tuples when the data shouldn't change. Use lists when you need to add, remove, or modify items.

**Try it:** Write a function that returns the first and last element of a list as a tuple.

Source: [tuples.py](../source/tuples.py)

Next: [Dictionaries](dictionaries.md)
