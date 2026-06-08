# Python by Example: Sorting

Python has two ways to sort: `list.sort()` modifies a list in place; `sorted()` returns a new sorted list and works on any iterable. Both accept a `key` function to control sort order and a `reverse` flag for descending order.

**What you'll learn:**
- `sort()` vs `sorted()`
- Sorting in reverse
- Sorting by a custom key

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)

# sorted() leaves the original unchanged
original = [3, 1, 4]
result = sorted(original)
print(result)
print(original)

print(sorted([3, 1, 4, 1, 5], reverse=True))

# key= extracts a comparison value from each element
words = ["banana", "apple", "cherry", "date"]
print(sorted(words, key=len))

people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
by_age = sorted(people, key=lambda p: p["age"])
print(by_age)
```

`key=len` sorts by string length. `key=lambda p: p["age"]` sorts dicts by a field. Python's sort is stable—equal elements keep their original relative order.

To run this program:

```bash
$ python source/sorting.py
[1, 1, 2, 3, 4, 5, 6, 9]
[1, 3, 4]
[3, 1, 4]
[5, 4, 3, 1, 1]
['date', 'apple', 'banana', 'cherry']
[{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
```

**Tip:** Use `key=` instead of writing a custom comparison function. For multiple fields, return a tuple: `key=lambda x: (x["dept"], x["age"])`.

**Try it:** Sort a list of strings alphabetically, ignoring case.

Source: [sorting.py](../source/sorting.py)

Next: [Collections](collections.md)
