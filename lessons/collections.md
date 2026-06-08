# Python by Example: Collections

The `collections` module provides specialized data structures for common patterns. `Counter` counts occurrences; `defaultdict` supplies a default value for missing keys; `deque` is a fast double-ended queue. All three solve problems that plain lists and dicts handle awkwardly.

**What you'll learn:**
- `Counter` for tallying items
- `defaultdict` for grouping without KeyError
- `deque` for fast appends and pops from both ends

```python
from collections import Counter, defaultdict, deque


# Counter tallies occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
print(counts)
print(counts["apple"])
print(counts.most_common(2))


# defaultdict avoids KeyError for missing keys
groups = defaultdict(list)
for name, dept in [("Alice", "eng"), ("Bob", "hr"), ("Carol", "eng")]:
    groups[dept].append(name)
print(dict(groups))


# deque supports fast O(1) appends and pops from both ends
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(d)
d.popleft()
print(d)
```

`Counter` also supports arithmetic—add two counters to combine counts. `defaultdict(list)` is the idiomatic way to group items. `deque` is better than a list when you frequently add or remove from the front.

To run this program:

```bash
$ python source/collections-example.py
Counter({'apple': 3, 'banana': 2, 'cherry': 1})
3
[('apple', 3), ('banana', 2)]
{'eng': ['Alice', 'Carol'], 'hr': ['Bob']}
deque([0, 1, 2, 3, 4])
deque([1, 2, 3, 4])
```

**Tip:** `Counter("hello")` counts characters; `Counter(a) + Counter(b)` merges two tallies.

**Try it:** Use `Counter` to find the three most common words in a paragraph of text.

Source: [collections-example.py](../source/collections-example.py)

Next: [Functions](functions.md)
