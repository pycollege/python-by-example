# Python by Example: Decorators

Decorators wrap a function to add behavior before or after it runs. Write `@decorator` above a function definition to apply it. Under the hood, `@log` is shorthand for `greet = log(greet)`. Decorators are used everywhere—logging, timing, authentication, caching.

**What you'll learn:**
- Defining and applying a decorator
- Preserving arguments with `*args, **kwargs`
- Decorators that accept their own arguments

```python
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done {func.__name__}")
        return result
    return wrapper


@log
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print("hi")


say_hi()
```

`log` takes a function and returns `wrapper`, which calls the original. `*args, **kwargs` passes any arguments through unchanged. `repeat(3)` returns a decorator—an extra layer of nesting handles the argument.

To run this program:

```bash
$ python source/decorators.py
Calling greet
Hello, Alice!
Done greet
hi
hi
hi
```

**Tip:** Use `functools.wraps(func)` inside `wrapper` to preserve the original function's name and docstring.

**Try it:** Write a decorator that measures and prints how long a function takes to run.

Source: [decorators.py](../source/decorators.py)

Next: [Range and Enumerate](range-and-enumerate.md)
