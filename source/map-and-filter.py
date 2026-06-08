numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


def square(x):
    return x ** 2


print(list(map(square, numbers)))

# Equivalent list comprehensions
print([x * 2 for x in numbers])
print([x for x in numbers if x % 2 == 0])
