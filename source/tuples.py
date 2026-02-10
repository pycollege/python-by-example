# Create tuples
point = (3, 4)
rgb = (255, 128, 0)

# Access by index
print(point[0], point[1])

# Tuple unpacking
x, y = point
print(x, y)

# Single-element tuple needs a trailing comma
single = (1,)
print(single)

# Return multiple values (as a tuple)
def min_max(nums):
    return min(nums), max(nums)


low, high = min_max([3, 1, 4, 1, 5])
print(low, high)
