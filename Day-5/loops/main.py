# for - loop

# 2
# 3
# syntax
# for var_name in range(start,stop,step):
#     # block of code

# i=0
# i<5


# step -> i=i+2
# i=0
# i=0+2=2
# i=2+2=4
# step : we add the step value
# step<0 -> it is substraction

i = 5
# i=i+step = 5+(-1)=5-1=4
# try to code at same time
# start > stop || start < stop ( ? condition)

# Quick Qna -> Find what this loop print on the console
# for i in range(0, 5, -1):
#     print(i)

# the number of iteration is fixed
# for i in range(5, 0, -1):
#     print("Hello world", i)


# what is while loop ?
# the number of iteration is not fixed
# run the block until a condition is true

# Reverse a number
# Get the sum of digits of number

# while (condition is true):
#     # block of code

# Print the number from 1 to n ( by the user given as n)

# n = int(input("Enter n: "))
# i = 1  # initialization
# while i <= n:  # condition
#     print(i)
#     i = i + 1  # updation


# WAP to Print the number from n to 1

n = int(input("Enter n: "))
while n >= 1:  # condition
    print(n)
    n = n - 1  # updation
