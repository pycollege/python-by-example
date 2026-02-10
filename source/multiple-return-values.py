def divide_and_remainder(a, b):
    return a // b, a % b


# Unpack into variables
quotient, remainder = divide_and_remainder(17, 5)
print(quotient, remainder)


def min_max(nums):
    return min(nums), max(nums)


low, high = min_max([3, 1, 4, 1, 5])
print(f"min={low}, max={high}")

# Or capture as a single tuple
result = min_max([1, 2, 3])
print(result)
