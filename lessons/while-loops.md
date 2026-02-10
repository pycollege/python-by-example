# Python by Example: While Loops

A `while` loop repeats as long as a condition is true. Use it when you don't know in advance how many iterations you need—for example, reading input until the user quits or retrying until success. Be careful: if the condition never becomes false, you get an infinite loop.

**What you'll learn:**
- The `while` loop syntax
- Updating the loop variable to avoid infinite loops
- Using `break` to exit early

```python
count = 0
while count < 3:
    print(count)
    count += 1

# Break out of a loop
n = 0
while True:
    print(n)
    n += 1
    if n >= 3:
        break
```

The first loop runs while `count < 3`; `count += 1` ensures we eventually stop. The second uses `while True` with `break`—a common pattern when the exit condition is complex.

To run this program:

```bash
$ python source/while-loops.py
0
1
2
0
1
2
```

**Tip:** Always ensure your condition can become false, or that `break` will run. Otherwise the loop runs forever. Press Ctrl+C to stop an infinite loop.

**Try it:** Change the condition to `count < 5` and see how the output changes.

Source: [while-loops.py](../source/while-loops.py)

Next: [If/Else](if-else.md)
