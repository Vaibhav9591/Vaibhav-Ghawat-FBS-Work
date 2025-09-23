# 10. Write a program to print list after removing even numbers.

li = [10,15,20,25,30,35,40,45,50]  
li1=[]
for i in li:
        if(i%2!=0):
         li1.append(i)
print('list after romoving even number:',li1,end=' ')
