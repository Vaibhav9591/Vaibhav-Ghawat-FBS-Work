# 4. Write a program to find sum of n numbers using recursion.

def sum_of_num(num):
    if(num == 0):
        return 0
    else:
     return sum_of_num(num-1)+num
    
num = int(input("enter a number: "))
res = sum_of_num(num)
print(f'sum of given number is:',res)