# Python by Example: Methods

Methods are functions defined on a class. Instance methods take `self` and operate on the instance. Class methods take `cls` and use `@classmethod`—useful for alternate constructors. Static methods use `@staticmethod` and take neither—they're utility functions that logically belong to the class but don't need instance or class data.

**What you'll learn:**
- Instance methods vs class methods vs static methods
- When to use each
- Class attributes shared by all instances

```python
class Counter:
    count = 0  # class attribute

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count

    def instance_method(self):
        return f"I am instance {self.id}"

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def info():
        return "Counter tracks instance creation"


c1 = Counter()
c2 = Counter()
print(c1.instance_method())
print(Counter.get_count())
print(Counter.info())
```

`Counter.count` is shared—both instances increment it. `get_count` uses `cls` to access the class; `info` needs neither `self` nor `cls`. Use `@staticmethod` when the function is related to the class but doesn't use instance or class state.

To run this program:

```bash
$ python source/methods.py
I am instance 1
2
Counter tracks instance creation
```

**Tip:** Most methods are instance methods. Use `@classmethod` for factory methods; use `@staticmethod` sparingly for utilities.

**Try it:** Add a class method that creates a Counter and returns it with a specific id.

Source: [methods.py](../source/methods.py)

Next: [Inheritance](inheritance.md)
