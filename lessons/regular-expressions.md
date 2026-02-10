# Python by Example: Regular Expressions

Regular expressions (regex) match text patterns. Use them for validation, search-and-replace, and parsing. The `re` module provides `search`, `findall`, `sub`, and more. Use raw strings `r"..."` so backslashes aren't interpreted as escape sequences. Regex has a learning curve—start simple.

**What you'll learn:**
- `re.search()` to find one match
- `re.findall()` for all matches
- `re.sub()` to replace
- `re.compile()` for reusable patterns

```python
import re

text = "Contact: alice@example.com or bob@test.org"

# Search for a pattern
match = re.search(r"\w+@\w+\.\w+", text)
if match:
    print(match.group())

# Find all matches
emails = re.findall(r"\w+@[\w.]+", text)
print(emails)

# Replace
masked = re.sub(r"\d+", "XXX", "Phone: 555-1234")
print(masked)

# Compile for reuse
pattern = re.compile(r"\b\w{4}\b")
print(pattern.findall("The quick brown fox"))
```

`\w` matches word characters; `\d` matches digits; `\b` is a word boundary. The `r` prefix makes it a raw string so `\w` isn't misinterpreted.

To run this program:

```bash
$ python source/regular-expressions.py
alice@example.com
['alice@example.com', 'bob@test.org']
Phone: XXX-XXXX
['quick', 'brown']
```

**Tip:** For simple string operations (e.g., `"x" in s`), prefer built-in methods. Use regex when you need pattern matching.

**Try it:** Use `re.sub` to replace all vowels in a string with `*`.

Source: [regular-expressions.py](../source/regular-expressions.py)

Next: [JSON](json.md)
