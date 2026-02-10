def greet(name):
    return f"Hello, {name}!"


# Call the function
print(greet("Alice"))


def add(a, b):
    return a + b


print(add(2, 3))
print(add("hello", " world"))


# Default arguments
def power(base, exp=2):
    return base**exp


print(power(3))
print(power(3, 3))
