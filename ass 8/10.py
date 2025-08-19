# 10. Write a program to check if entered year is a leap year or not.

def leap_year():
   
    year = int(input("enter a year: "))
    
    if(year%2==0):
     print('this is leap year ')
    else:
     print('this is not leap year')
leap_year()