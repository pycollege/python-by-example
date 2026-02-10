# Python by Example: Strings

Strings are immutable sequences of Unicode characters. You can index and slice them like lists. Python provides many string methods for common tasks: `split`, `join`, `strip`, `upper`, `lower`, `replace`, and more. Strings are used everywhere—user input, file content, API responses.

**What you'll learn:**
- Indexing and slicing strings
- Common methods: `split`, `join`, `strip`, `upper`, `lower`, `replace`

```python
s = "Hello, World!"

# Indexing and slicing
print(s[0])
print(s[-1])
print(s[7:12])

# Common methods
print(s.lower())
print(s.upper())
print(s.replace("World", "Python"))

# split and join
words = "a b c".split()
print(words)
print("-".join(words))

# strip whitespace
print("  hello  ".strip())
```

`split()` with no argument splits on whitespace. `join()` is the inverse—it combines a list of strings with the separator. Strings are immutable; methods return new strings.

To run this program:

```bash
$ python source/strings.py
H
!
World
hello, world!
HELLO, WORLD!
Hello, Python!
['a', 'b', 'c']
a-b-c
hello
```

**Tip:** `"".join(list_of_strings)` is faster than concatenating with `+` in a loop when building a string.

**Try it:** Use `split()` and `join()` to reverse the words in a sentence.

Source: [strings.py](../source/strings.py)

Next: [String Formatting](string-formatting.md)
