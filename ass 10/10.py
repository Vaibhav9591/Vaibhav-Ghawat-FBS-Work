# 10. Write a program to remove all occurrences of a given element in the list.

li = [1,2,3,2,4,2,5,2,7,2,8,2,9]
print(li)
li2 =[]
for i in range(len(li)):
    if(li[i]!=2):
     li2.append(li[i])
print('after occurrence',li2)