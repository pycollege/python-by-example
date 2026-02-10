# Python by Example: Slicing

Slicing lets you extract a portion of a list, string, or tuple. The syntax is `[start:stop:step]`. Start is inclusive, stop is exclusive—the same rule as `range()`. Omitting values uses defaults: start=0, stop=end, step=1. Slicing never modifies the original; it returns a new sequence.

**What you'll learn:**
- `[start:stop]` and `[start:stop:step]`
- Omitted indices: `[:3]`, `[7:]`, `[::2]`
- Negative step to reverse: `[::-1]`

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slice[start:stop] — stop is exclusive
print(nums[2:5])

# Omit start (from beginning) or stop (to end)
print(nums[:3])
print(nums[7:])

# Step: every 2nd element
print(nums[::2])

# Negative step reverses
print(nums[::-1])

# Strings work the same way
s = "hello"
print(s[1:4])
print(s[::-1])
```

`nums[2:5]` gives indices 2, 3, 4—not 5. `nums[::-1]` reverses the list. Slicing works identically on strings.

To run this program:

```bash
$ python source/slicing.py
[2, 3, 4]
[0, 1, 2]
[7, 8, 9]
[0, 2, 4, 6, 8]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
ell
olleh
```

**Tip:** `s[::-1]` is a common way to reverse a string or list in one line.

**Try it:** Slice the string `"abcdef"` to get `"ace"` (every other character).

Source: [slicing.py](../source/slicing.py)

Next: [Tuples](tuples.md)
