# 7. Write a program to find sum of digits using recursion.

def sum_of_digit(num):
    if(num==0):
        return 0
    temp = num   
    return temp % 10 + sum_of_digit(temp // 10)  
   
num = int(input("enter a two digit number: "))
res = sum_of_digit(num)
print(res)