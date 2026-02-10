nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slice[start:stop] — stop is exclusive
print(nums[2:5])

# Omit start (from beginning) or stop (to end)
print(nums[:3])
print(nums[7:])

# Step: every 2nd element
print(nums[::2])

# Negative step reverses
print(nums[::-1])

# Strings work the same way
s = "hello"
print(s[1:4])
print(s[::-1])
