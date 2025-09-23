# Write a program to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!
# Note : For fact and sum two recursive functions

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum(num):
    if num == 0:
        return 0
    else:
        return factorial(num) + sum(num - 1)
num = int(input("enter a number: "))
ress  = factorial(num)
res = sum(num)
print(f"The sum of series of factorials up to {num} is: {res}")
