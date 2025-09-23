# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.

def list(li):
    cube_list=[]
    for i in li:
        cube_list.append(i**3)
    return (cube_list)
    
li =[1,2,3,4,5]
print('list before cubing the element',li)
li = list(li)
print('list after getting cube of an element',li)