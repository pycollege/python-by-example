# Python by Example: For Loops

A `for` loop repeats code for each item in a sequence. Unlike C or Java, Python's `for` iterates over collections directly—you rarely need an index variable. Use `range()` when you need a sequence of numbers. For loops are one of the most common constructs in Python.

**What you'll learn:**
- Looping over lists and other sequences
- Using `range()` for numeric loops
- `range(start, stop, step)`—stop is exclusive

```python
# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with range(start, stop) — stop is exclusive
for i in range(3):
    print(i)

# range with start and end
for i in range(2, 5):
    print(i)

# range with step
for i in range(0, 10, 2):
    print(i)
```

`range(3)` produces 0, 1, 2—not 3. The end value is always exclusive. `range(0, 10, 2)` goes 0, 2, 4, 6, 8.

To run this program:

```bash
$ python source/for-loops.py
apple
banana
cherry
0
1
2
2
3
4
0
2
4
6
8
```

**Tip:** Prefer `for item in items:` over `for i in range(len(items)):` when you don't need the index. It's clearer and less error-prone.

**Try it:** Loop over a string—each character is an item.

Source: [for-loops.py](../source/for-loops.py)

Next: [While Loops](while-loops.md)
