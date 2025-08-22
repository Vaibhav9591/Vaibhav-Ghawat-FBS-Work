# 1. Write a function to which we pass a parameter and
# print the factors of a given number

def factor (num):
    for i in range (2,num+1):
     if(num % i == 0):
        print(i,end = ' ')
num = int (input("enter a number: "))
factor(num)