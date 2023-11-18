# Powerful Functions to reduce to code lines and optimise time

# map function

# Python is case-sensitive


numbers = [23, 45, 233, 5, 4656, 634]

sqr_numbers = map(lambda a: a * 2, numbers)


# print(numbers)
# print(list(sqr_numbers))


# filter -> for+conditionals(if,ifelse)


eg_numbers = [23, 23, 34, 454, 2, 46, 5, 43, 4, 35, 47]

even_nums = filter(lambda a: a % 2 == 0, eg_numbers)
odd_nums = filter(lambda a: a % 2 != 0, eg_numbers)

print(list(even_nums))
print(list(odd_nums))

# even
# [34, 454, 2, 46, 4]

# odd
# [23, 23, 5, 43, 35, 47]
