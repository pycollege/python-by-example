# Python by Example: Variables

Variables are named containers for values. They let you store data and reuse it. Python is dynamically typed—a variable can hold an integer, then a string, without declaring the type. This makes code flexible but requires care when mixing types.

**What you'll learn:**
- Assigning with `=`
- Reassigning to a different type
- Multiple assignment in one line

```python
# Assign a string
name = "Alice"
print(name)

# Assign an integer
age = 30
print(age)

# Reassign to a different type
age = "thirty"  # Now age is a string
print(age)

# Multiple assignment
x, y = 1, 2
print(x, y)
```

The `x, y = 1, 2` line assigns 1 to `x` and 2 to `y` in one step. This is handy for swapping: `a, b = b, a`.

To run this program:

```bash
$ python source/variables.py
Alice
30
thirty
1 2
```

**Tip:** Use descriptive names like `user_count` instead of `x` or `n` to make code easier to understand.

**Try it:** Create a new variable, assign different types to it, and print each.

Source: [variables.py](../source/variables.py)

Next: [Constants](constants.md)
