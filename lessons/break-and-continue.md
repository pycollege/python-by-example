# Python by Example: Break and Continue

Sometimes you need to change loop behavior mid-iteration. `break` exits the loop immediately. `continue` skips the rest of the current iteration and jumps to the next. Both work in `for` and `while` loops. Use them when the normal loop flow isn't enough.

**What you'll learn:**
- `break`: exit the loop now
- `continue`: skip to the next iteration

```python
# break: exit loop when condition is met
for i in range(5):
    if i == 3:
        break
    print(i)
print("done with break")

# continue: skip current iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
print("done with continue")
```

With `break`, we never print 3—we leave the loop as soon as `i` is 3. With `continue`, we skip printing 2 but keep looping. The loop body after `continue` is not executed for that iteration.

To run this program:

```bash
$ python source/break-and-continue.py
0
1
2
done with break
0
1
3
4
done with continue
```

**Tip:** Prefer clear loop conditions over `break` when possible. But `break` is fine for "found what we needed" or "error, stop" cases.

**Try it:** Change the `break` condition to `i == 1` and see how the output changes.

Source: [break-and-continue.py](../source/break-and-continue.py)

Next: [Lists](lists.md)
