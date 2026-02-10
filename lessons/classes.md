# Python by Example: Classes

Classes are blueprints for creating objects. They bundle data (attributes) and behavior (methods) together. Use them when you have data that belongs together and functions that operate on it. The `__init__` method runs when you create an instance; `self` refers to the instance.

**What you'll learn:**
- Defining a class with `class`
- The `__init__` constructor
- Instance attributes and the `self` parameter
- Creating instances by calling the class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


dog = Dog("Rex", 3)
print(dog.name)
print(dog.age)
print(dog.bark())
```

`Dog("Rex", 3)` creates a new Dog; Python calls `__init__(self, "Rex", 3)`. `self.name` and `self.age` store data on the instance. Every instance method takes `self` as the first parameter.

To run this program:

```bash
$ python source/classes.py
Rex
3
Rex says woof!
```

**Tip:** Class names use PascalCase (e.g., `Dog`, `UserAccount`). Method and attribute names use snake_case (e.g., `bark`, `user_name`).

**Try it:** Add a method that returns the dog's age in "dog years" (age * 7).

Source: [classes.py](../source/classes.py)

Next: [Methods](methods.md)
