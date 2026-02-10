# Python by Example: Functions

Functions let you reuse code and organize logic. Define them with `def`; parameters go in parentheses; use `return` to send a value back. Python doesn't require type declarations—you can add type hints for clarity. Default arguments let callers omit optional parameters.

**What you'll learn:**
- Defining functions with `def`
- Parameters and `return`
- Default argument values
- Functions can take different types (dynamic typing)

```python
def greet(name):
    return f"Hello, {name}!"


# Call the function
print(greet("Alice"))


def add(a, b):
    return a + b


print(add(2, 3))
print(add("hello", " world"))


# Default arguments
def power(base, exp=2):
    return base ** exp


print(power(3))
print(power(3, 3))
```

`power(3)` uses the default `exp=2`, so it returns 9. `power(3, 3)` overrides it and returns 27. The same `add` function works for numbers and strings because Python is dynamically typed.

To run this program:

```bash
$ python source/functions.py
Hello, Alice!
5
hello world
9
27
```

**Tip:** Keep functions focused—one clear purpose per function. Shorter functions are easier to test and reuse.

**Try it:** Write a function that takes a name and age, and returns a greeting that includes both.

Source: [functions.py](../source/functions.py)

Next: [Multiple Return Values](multiple-return-values.md)
