# 13 . Write a program to print list after removing even numbers.


li = [10,20,30,45,67,88]
li1 =[]
for i in li:
    if(i%2==0):
        print()
    else:
     li1.append(i)

print('list before removing even numbers',li)
print('list after removing even numbers',li1)
