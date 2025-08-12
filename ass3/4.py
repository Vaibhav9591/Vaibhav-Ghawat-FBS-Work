# 4. Write a program to input all sides of a triangle and check whether triangle is valid or
# not.


num1 = int(input("enter a num 1 :"))
num2 = int(input("enter a num 2 :"))
num3 = int(input("enter a num 3 :"))
if (num1+num2+num3==180):
    print(f'the triangle is valid')
else:
    print(f'the triangle is invalid')