# 6. Write a program to print Fibonacci series using recursion.
    
def fibonacci(num):
    if num <= 0:
        return 
    elif num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
def print_fibonacci_series(n):
    if n <= 0:
       return
    else:
        for i in range(1, n + 1):
            print(fibonacci(i), end=" ")
num = int(input("enter a number: "))
res = print_fibonacci_series(num)
print,res