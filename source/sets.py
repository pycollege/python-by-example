# Create a set (no duplicates)
colors = {"red", "green", "blue", "red"}
print(colors)

# Membership
print("red" in colors)
print("yellow" in colors)

# Add and remove
colors.add("yellow")
colors.discard("green")
print(colors)

# Set operations
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)   # union
print(a & b)   # intersection
print(a - b)   # difference
