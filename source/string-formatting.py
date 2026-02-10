name = "Alice"
age = 30

# f-strings (preferred)
print(f"{name} is {age} years old")
print(f"Next year: {age + 1}")

# Format specifiers
pi = 3.14159
print(f"Pi: {pi:.2f}")
print(f"Hex: {42:x}")

# str.format()
print("{} is {}".format(name, age))

# % (legacy)
print("%s is %d" % (name, age))
