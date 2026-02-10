# Python by Example: Lists

Lists are ordered, mutable sequences—one of the most used data structures in Python. Use them whenever you need an ordered collection of items. They can hold any type and can mix types. Indexing starts at 0; negative indices count from the end.

**What you'll learn:**
- Creating lists with square brackets
- Indexing: `[0]` for first, `[-1]` for last
- `append`, `extend`, `insert` to add items
- `len()` for the number of elements

```python
# Create a list
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Indexing
print(fruits[0])
print(fruits[-1])  # last element

# Append and extend
fruits.append("date")
print(fruits)

fruits.extend(["elderberry", "fig"])
print(fruits)

# Insert at position
fruits.insert(1, "apricot")
print(fruits)

# Length
print(len(fruits))
```

`append` adds one item; `extend` adds all items from another list. `insert(1, "apricot")` puts "apricot" at index 1 and shifts the rest.

To run this program:

```bash
$ python source/lists.py
['apple', 'banana', 'cherry']
apple
cherry
['apple', 'banana', 'cherry', 'date']
['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
['apple', 'apricot', 'banana', 'cherry', 'date', 'elderberry', 'fig']
7
```

**Tip:** `fruits[-1]` is the last element, `fruits[-2]` is second-to-last. Handy when you don't know the length.

**Try it:** Create a list of numbers, append some, and print the first and last.

Source: [lists.py](../source/lists.py)

Next: [Slicing](slicing.md)
