from functools import reduce


def add(a, b):
    return a + b


nums = [1, 2, 3, 4, 5]

sum1 = reduce(add, nums, 0)


print("the sum is = ", sum1)
