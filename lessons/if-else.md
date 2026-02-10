# Python by Example: If/Else

Conditionals let your program choose different paths based on data. Python uses indentation (spaces) to define blocks—no braces needed. Use `if` for the first condition, `elif` for additional ones, and `else` for the fallback. Indentation matters: use 4 spaces consistently.

**What you'll learn:**
- `if`, `elif`, and `else`
- Indentation rules
- Truthiness: empty lists and zero are falsy
- One-line conditional expressions

```python
x = 10

if x > 10:
    print("greater than 10")
elif x == 10:
    print("exactly 10")
else:
    print("less than 10")

# One-line conditional expression
result = "even" if x % 2 == 0 else "odd"
print(result)

# Truthiness: empty sequences and zero are falsy
items = []
if not items:
    print("list is empty")
```

`elif` is short for "else if." The expression `"even" if x % 2 == 0 else "odd"` chooses one of two values. Empty lists (`[]`) and zero are "falsy"—`if not items:` is True when the list is empty.

To run this program:

```bash
$ python source/if-else.py
exactly 10
even
list is empty
```

**Tip:** Use 4 spaces for indentation. Never mix tabs and spaces—Python will complain. Most editors insert spaces when you press Tab.

**Try it:** Change `x` to 11 or 9 and see which branch runs.

Source: [if-else.py](../source/if-else.py)

Next: [Match](match.md)
