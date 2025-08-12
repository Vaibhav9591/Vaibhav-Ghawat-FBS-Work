# 5. WAP to print Fibonacci series upto n.

num = int(input("enter a number: "))

a = 0
b = 1
c = b  
count = 1

while count <= num:
    print(c, end=" ")
    count += 1
    a, b = b, c
    c = a + b