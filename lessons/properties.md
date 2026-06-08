# Python by Example: Properties

The `@property` decorator lets you access a method like an attribute. Use it to add validation or computed values without changing the public interface of a class. Pair it with `@name.setter` to intercept assignments.

**What you'll learn:**
- `@property` for computed read access
- `@name.setter` for validated assignment
- Keeping implementation details private with `_name`

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


t = Temperature(100)
print(t.celsius)
print(t.fahrenheit)

t.celsius = 0
print(t.celsius)
print(t.fahrenheit)
```

`fahrenheit` is a computed property with no setter, so it's read-only. The leading underscore on `_celsius` signals it's an internal detail; callers use the `celsius` property instead. The call site `t.celsius` looks like plain attribute access—no parentheses needed.

To run this program:

```bash
$ python source/properties.py
100
212.0
0
32.0
```

**Tip:** Add `@property` gradually—start with plain attributes and add a property only when you need validation or computation. The call site stays the same either way.

**Try it:** Add a `kelvin` property that converts Celsius to Kelvin (add 273.15).

Source: [properties.py](../source/properties.py)

Next: [Dataclasses](dataclasses.md)
