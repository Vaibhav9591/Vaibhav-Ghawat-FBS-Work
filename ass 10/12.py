# 12. Write a program to create three lists of numbers, their squares
# and cubes

def cube_square(li):
    cube =[]
    square =[]
    for i in li:
        cube.append(i**3)
       
    for i in li:
         square.append(i**2)
    print(f'list of cube',cube,'list of square',square)
li = [1,2,3,4,5]
print('list before',li)
cube_square(li)
