# 9. WAP to print all numbers in a range divisible by a given number.

n = int(input("enter a range: "))
num = int(input("enter a num: "))

i=1

for i in range(i,n):
     if (i % num ==0):
        print(i)
        