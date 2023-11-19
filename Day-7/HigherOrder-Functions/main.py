# # Powerful Functions to reduce to code lines and optimise time

# # map function  -> maps the value of list
# # filter -> filters
# # reduce -> higher order function -> it returns a single value


# # Python is case-sensitive


# numbers = [23, 45, 233, 5, 4656, 634]

# sqr_numbers = map(lambda a: a * 2, numbers)


# # print(numbers)
# # print(list(sqr_numbers))


# # filter -> for+conditionals(if,ifelse)


# eg_numbers = [23, 23, 34, 454, 2, 46, 5, 43, 4, 35, 47]

# even_nums = filter(lambda a: a % 2 == 0, eg_numbers)
# odd_nums = filter(lambda a: a % 2 != 0, eg_numbers)

# # filter(boolean exp, iterable)    iterable -> list , tuples , dict

# print(list(even_nums))  # type casting
# print(list(odd_nums))

# even
# [34, 454, 2, 46, 4]

# odd
# [23, 23, 5, 43, 35, 47]
from functools import reduce

numbers2 = [1, 2, 3, 4, 5]

sum1 = reduce(lambda temp, val2: temp + val2, numbers2, 0)
product1 = reduce(lambda temp, val2: temp * val2, numbers2, 1)
print("Sum of list nums= ", sum1)
print("Product of list nums= ", product1)


# [1, 2, 3, 4, 5]
# Sum of list nums=  15
# Product of list nums=  120
