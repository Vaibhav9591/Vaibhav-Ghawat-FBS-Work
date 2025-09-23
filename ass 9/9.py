# 9. Write a program to calculate the m to the power n using recursion.

def power(a, b):
    if b != 0:
        return a * power(a, b - 1)
    else:
        return 1

num = int(input("enter a number: "))
b = 3
print(num, "to the power of", b, "is", power(num, b))