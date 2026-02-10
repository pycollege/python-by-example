# List comprehension
squares = [x**2 for x in range(5)]
print(squares)

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Dict comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print(word_lengths)

# Set comprehension
unique_lengths = {len(word) for word in ["apple", "banana", "apple"]}
print(unique_lengths)

# Nested
matrix = [[i * j for j in range(3)] for i in range(3)]
print(matrix)
