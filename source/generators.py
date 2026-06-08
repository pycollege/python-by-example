def count_up(n):
    for i in range(n):
        yield i


gen = count_up(3)
print(next(gen))
print(next(gen))
print(next(gen))

for value in count_up(5):
    print(value)

# Generator expression—like a list comprehension but lazy
squares = (x**2 for x in range(5))
print(list(squares))


def integers():
    n = 0
    while True:
        yield n
        n += 1


gen = integers()
print([next(gen) for _ in range(5)])
