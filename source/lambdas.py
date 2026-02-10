# Lambda: one expression, no statements
double = lambda x: x * 2
print(double(5))

# Common use: sorting
pairs = [(1, "one"), (3, "three"), (2, "two")]
sorted_by_num = sorted(pairs, key=lambda p: p[0])
sorted_by_word = sorted(pairs, key=lambda p: p[1])
print(sorted_by_num)
print(sorted_by_word)

# map and filter
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(squared)
print(evens)
