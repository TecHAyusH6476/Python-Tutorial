# list comprehension

# syntax :
# list_of_num = [expression for item in iterable if condition]
nums = [12, 34, 623, 45, 6723, 78, 23]
# o/p = [1,4,9,16,25]

res = [i**2 for i in nums]
# print(res)

# list comprehension with conditions

# numbers -> odd and even ?
# even -> num % 2 == 0  // to check if num is even
# odd -> num % 2 != 0

# From the list we need to get all even numbers
nums = [12, 34, 623, 45, 6723, 78, 23, 0, -12, -13]
# o/p = [12,34,78,0,-12]

# res = []
# for val in nums:
#     if val % 2 == 0:
#         res.append(val)  # putting values in res list [12,34,...,-12]

res = [val for val in nums if val % 2 == 0]

print(res)
