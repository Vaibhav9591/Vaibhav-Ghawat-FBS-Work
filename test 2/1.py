# 1.Write a program to accept year from user and check if it is a leap year or not.

year = int(input("enter year: "))


if (year % 4==0):
    print(f'year is leap year')
    
else:
    print(f'it is not leap year')
    