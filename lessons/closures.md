# Python by Example: Closures

A closure is a function that "remembers" variables from its enclosing scope. When you define a function inside another, the inner function can access the outer function's variables even after the outer function returns. Use `nonlocal` when the inner function needs to *modify* an outer variable.

**What you'll learn:**
- Nested functions and scope
- How closures "close over" outer variables
- The `nonlocal` keyword for reassignment

```python
def make_counter(start=0):
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


c1 = make_counter()
c2 = make_counter(10)
print(c1())   # 1
print(c1())   # 2
print(c2())   # 11


def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(5))
```

`make_counter` returns the inner `counter` function. Each call to `counter` increments `count` and returns it. Without `nonlocal`, `count += 1` would create a local variable instead of modifying the outer one.

To run this program:

```bash
$ python source/closures.py
1
2
11
10
15
```

**Tip:** Closures are useful for factory functions (like `make_counter`) and callbacks that need to remember state.

**Try it:** Write `make_adder(n)` that returns a function adding `n` to its argument.

Source: [closures.py](../source/closures.py)

Next: [Recursion](recursion.md)
