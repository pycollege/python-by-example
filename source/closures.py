def make_counter(start=0):
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


c1 = make_counter()
c2 = make_counter(10)
print(c1())   # 1
print(c1())   # 2
print(c2())   # 11


def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))
print(triple(5))
