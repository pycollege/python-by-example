# Python by Example: Multiple Return Values

Python functions can return multiple values. Behind the scenes, they return a single tuple; Python unpacks it into separate variables. This is convenient for functions that naturally produce several results—like divide-and-remainder or min-and-max.

**What you'll learn:**
- Returning multiple values as a tuple
- Unpacking into variables: `a, b = func()`
- When to use multiple returns

```python
def divide_and_remainder(a, b):
    return a // b, a % b


# Unpack into variables
quotient, remainder = divide_and_remainder(17, 5)
print(quotient, remainder)


def min_max(nums):
    return min(nums), max(nums)


low, high = min_max([3, 1, 4, 1, 5])
print(f"min={low}, max={high}")

# Or capture as a single tuple
result = min_max([1, 2, 3])
print(result)
```

`a // b` is integer division; `a % b` is the remainder. Returning `a, b` is shorthand for `return (a, b)`. You can capture the whole tuple or unpack it.

To run this program:

```bash
$ python source/multiple-return-values.py
3 2
min=1, max=5
(1, 3)
```

**Tip:** Use multiple returns when the values are related (e.g., quotient and remainder). For unrelated data, consider returning a dict or a small object.

**Try it:** Write a function that returns both the sum and product of two numbers.

Source: [multiple-return-values.py](../source/multiple-return-values.py)

Next: [Variadic Functions](variadic-functions.md)
