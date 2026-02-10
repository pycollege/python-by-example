# Python by Example: Values

Before using variables, you need to know the basic value types Python understands. These are called literals—values you write directly in code. Understanding them is essential for everything that follows.

**What you'll learn:**
- Integers (whole numbers) and floats (decimals)
- Booleans: `True` and `False`
- Strings: text in quotes
- Scientific notation with `e`

```python
# Integers
print(42)
print(-17)

# Floats (decimal numbers)
print(3.14)
print(2.5e3)  # 2.5 * 10^3 = 2500.0

# Booleans
print(True)
print(False)

# Strings (single or double quotes)
print("hello")
print('world')
```

The `e` in `2.5e3` means "times 10 to the power of"—so `2.5e3` equals 2500.0. Python uses `True` and `False` (capital T and F) for booleans.

To run this program:

```bash
$ python source/values.py
42
-17
3.14
2500.0
True
False
hello
world
```

**Tip:** Strings can use either single (`'`) or double (`"`) quotes. Pick one style and stick with it in a project.

**Try it:** Change the numbers and strings, then run to see the output.

Source: [values.py](../source/values.py)

Next: [Variables](variables.md)
