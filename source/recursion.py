def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(i) for i in range(10)])


def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


print(sum_list([1, 2, 3, 4, 5]))
