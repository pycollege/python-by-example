# Python by Example: Recursion

Recursion means a function calls itself. It's useful when a problem breaks down into smaller, similar subproblems—like computing factorials, traversing trees, or processing nested data. Every recursive function needs a base case that stops the recursion; otherwise you get infinite recursion and a stack overflow.

**What you'll learn:**
- Writing recursive functions
- Base case vs recursive case
- Classic examples: factorial, Fibonacci, sum of list

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(i) for i in range(10)])


def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


print(sum_list([1, 2, 3, 4, 5]))
```

Factorial: `5! = 5 * 4!`, and `1! = 1` is the base case. Fibonacci: each number is the sum of the two before it. Sum: add first element to the sum of the rest; empty list returns 0.

To run this program:

```bash
$ python source/recursion.py
120
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
15
```

**Tip:** Python limits recursion depth (around 1000). For deep recursion, consider an iterative (loop) solution instead.

**Try it:** Write a recursive function to reverse a string.

Source: [recursion.py](../source/recursion.py)

Next: [Range and Enumerate](range-and-enumerate.md)
