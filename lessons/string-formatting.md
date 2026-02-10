# Python by Example: String Formatting

String formatting inserts values into a template. F-strings (Python 3.6+) are the preferred way—they're readable and support expressions. Use format specifiers like `:.2f` for decimals or `:x` for hex. Older options are `str.format()` and `%`; you may see them in legacy code.

**What you'll learn:**
- F-strings: `f"{var}"`
- Format specifiers: `:.2f`, `:x`
- Alternative methods: `format()` and `%`

```python
name = "Alice"
age = 30

# f-strings (preferred)
print(f"{name} is {age} years old")
print(f"Next year: {age + 1}")

# Format specifiers
pi = 3.14159
print(f"Pi: {pi:.2f}")
print(f"Hex: {42:x}")

# str.format()
print("{} is {}".format(name, age))

# % (legacy)
print("%s is %d" % (name, age))
```

Anything inside `{}` in an f-string is evaluated: `{age + 1}` computes the value. `:.2f` means 2 decimal places; `:x` means hexadecimal.

To run this program:

```bash
$ python source/string-formatting.py
Alice is 30 years old
Next year: 31
Pi: 3.14
Hex: 2a
Alice is 30
Alice is 30
```

**Tip:** Prefer f-strings for new code. They're faster and clearer than `format()` or `%`.

**Try it:** Format a float with 3 decimal places and a percentage (e.g., 0.75 as "75%").

Source: [string-formatting.py](../source/string-formatting.py)

Next: [Regular Expressions](regular-expressions.md)
