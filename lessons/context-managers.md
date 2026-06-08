# Python by Example: Context Managers

The `with` statement manages resources that need setup and cleanup—files, network connections, locks. It calls `__enter__` when entering the block and `__exit__` when leaving, even if an exception occurs. Use `contextlib.contextmanager` to build your own with a generator function.

**What you'll learn:**
- Using `with` for automatic resource cleanup
- Building a context manager with `@contextmanager`
- Combining multiple managers in one `with`

```python
from contextlib import contextmanager


# with guarantees cleanup even if an error occurs
with open("data.txt", "w") as f:
    f.write("hello")

with open("data.txt") as f:
    print(f.read())


@contextmanager
def managed(name):
    print(f"Opening {name}")
    try:
        yield name
    finally:
        print(f"Closing {name}")


with managed("connection") as conn:
    print(f"Using {conn}")


# Multiple managers in one with statement
with managed("db") as db, managed("cache") as cache:
    print(f"Using {db} and {cache}")
```

The code before `yield` is setup (`__enter__`); the `finally` block is cleanup (`__exit__`). Multiple managers on one line are cleaned up in reverse order.

To run this program:

```bash
$ python source/context-managers.py
hello
Opening connection
Using connection
Closing connection
Opening db
Opening cache
Using db and cache
Closing cache
Closing db
```

**Tip:** Any object with `__enter__` and `__exit__` works as a context manager—not just files. Examples: threading locks, database transactions, test fixtures.

**Try it:** Write a context manager that temporarily changes the current working directory and restores it on exit.

Source: [context-managers.py](../source/context-managers.py)

Next: [Modules](modules.md)
