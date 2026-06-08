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
