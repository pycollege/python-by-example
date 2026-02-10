x = 10

if x > 10:
    print("greater than 10")
elif x == 10:
    print("exactly 10")
else:
    print("less than 10")

# One-line conditional expression
result = "even" if x % 2 == 0 else "odd"
print(result)

# Truthiness: empty sequences and zero are falsy
items = []
if not items:
    print("list is empty")
