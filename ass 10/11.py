# 11. Write a program to print all numbers which are divisible by m and n in the
# list.

def divisor(li):
    li1 = []
    for i in li:
        if (i % 2 ==0 and i % 5 ==0):
            li1.append(i)
            print('divisor of m and n is',i)
         
li = [10,20,30,33,45,43]
print('list',li)
divisor(li)
