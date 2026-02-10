try:
    result = 10 / 2
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division succeeded")
finally:
    print("Done")


# Raising exceptions
def get_item(lst, index):
    if index < 0 or index >= len(lst):
        raise IndexError(f"Index {index} out of range")
    return lst[index]


try:
    get_item([1, 2, 3], 10)
except IndexError as e:
    print(f"Caught: {e}")
