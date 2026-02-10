# Python by Example: Sets

Sets are unordered collections of unique elements—no duplicates. Use them when you need to remove duplicates, check membership quickly, or perform set operations (union, intersection, difference). Sets use curly braces like dicts but have no colons; they're defined by their unique values.

**What you'll learn:**
- Creating sets (duplicates are removed)
- `in` for membership testing
- `add` and `discard` to modify
- Union (`|`), intersection (`&`), difference (`-`)

```python
# Create a set (no duplicates)
colors = {"red", "green", "blue", "red"}
print(colors)

# Membership
print("red" in colors)
print("yellow" in colors)

# Add and remove
colors.add("yellow")
colors.discard("green")
print(colors)

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)   # union
print(a & b)   # intersection
print(a - b)   # difference
```

`discard` removes an item if present; it doesn't error if missing. `remove` would raise `KeyError`. Use sets when order doesn't matter and uniqueness does.

To run this program:

```bash
$ python source/sets.py
{'red', 'green', 'blue'}
True
False
{'red', 'blue', 'yellow'}
{1, 2, 3, 4}
{2, 3}
{1}
```

**Tip:** To remove duplicates from a list: `list(set(my_list))`. Note: order is not preserved.

**Try it:** Create two sets of numbers and print their union and intersection.

Source: [sets.py](../source/sets.py)

Next: [Functions](functions.md)
