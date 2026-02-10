# Python by Example: Constants

Python does not have built-in constants like some languages. Instead, programmers use a naming convention: `UPPER_CASE` names mean "treat this as constant—don't change it." The interpreter won't enforce this; it's a convention teams agree on. Constants are useful for configuration values and magic numbers.

**What you'll learn:**
- The `UPPER_CASE` convention for constants
- Why Python doesn't enforce immutability

```python
# Convention: UPPER_CASE for "constants"
MAX_SIZE = 100
API_URL = "https://api.example.com"
PI = 3.14159

print(MAX_SIZE)
print(API_URL)
print(PI)

# You can still reassign—Python won't stop you
MAX_SIZE = 200
print(MAX_SIZE)
```

Nothing prevents reassigning `MAX_SIZE`—Python allows it. The convention tells other developers (and your future self) not to change it.

To run this program:

```bash
$ python source/constants.py
100
https://api.example.com
3.14159
200
```

**Tip:** Use constants for values that appear multiple times or that might change later (e.g., API URLs, limits). Centralizing them makes updates easier.

**Try it:** Add your own constant and use it in a calculation.

Source: [constants.py](../source/constants.py)

Next: [For Loops](for-loops.md)
