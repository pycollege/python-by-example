# Python by Example: Scope

Python looks up names in four scopes in order: **local** (inside the function), **enclosing** (outer functions), **global** (module level), **built-in**. Use `global` to assign to a module-level variable from inside a function; use `nonlocal` to assign to a variable in an enclosing function.

**What you'll learn:**
- LEGB scope lookup order
- `global` to modify a module-level variable
- `nonlocal` to modify a variable in an enclosing scope

```python
x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()
    print(x)


outer()
print(x)


count = 0


def increment():
    global count
    count += 1


increment()
increment()
print(count)


def make_counter():
    n = 0

    def inc():
        nonlocal n
        n += 1
        return n

    return inc


counter = make_counter()
print(counter())
print(counter())
```

Each scope gets its own `x`—assigning inside a function never touches the outer `x` unless you use `global` or `nonlocal`. `nonlocal` is how closures maintain mutable state across calls.

To run this program:

```bash
$ python source/scope.py
local
enclosing
global
2
1
2
```

**Tip:** Prefer returning values over using `global`—it makes data flow explicit and functions easier to test.

**Try it:** Rewrite `increment()` to take and return `count` instead of using `global`.

Source: [scope.py](../source/scope.py)

Next: [Recursion](recursion.md)
