#2. Write a program to find factorial of given number using recursion

def factor (num):
    if(num == 0):
        return 1
    else:
        return num * factor(num-1)
num = int (input("enter a number: "))
res = factor(num)
print (res)