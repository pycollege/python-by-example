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
