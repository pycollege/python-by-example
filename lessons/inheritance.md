# Python by Example: Inheritance

Inheritance lets a class reuse and extend another. The child class gets all attributes and methods from the parent; override them by redefining. Use `super()` to call the parent's methods—especially `__init__` so the base is initialized correctly. Inheritance models "is-a" relationships: a Dog *is* an Animal.

**What you'll learn:**
- Inheriting with `class Child(Parent):`
- Overriding methods
- Using `super()` for the parent

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"


animal = Animal("generic")
dog = Dog("Rex")
cat = Cat("Whiskers")
print(animal.speak())
print(dog.speak())
print(cat.speak())
```

`Dog` and `Cat` inherit `__init__` and `name` from `Animal`. They override `speak` to provide their own behavior. `Dog("Rex")` calls `Animal.__init__(self, "Rex")` implicitly (Python passes it through).

To run this program:

```bash
$ python source/inheritance.py
generic makes a sound
Rex says woof!
Whiskers says meow!
```

**Tip:** If the child adds new attributes, call `super().__init__(...)` first, then set the child's attributes.

**Try it:** Add a `Bird` class that inherits from `Animal` and overrides `speak` with "tweet!".

Source: [inheritance.py](../source/inheritance.py)

Next: [Dataclasses](dataclasses.md)
