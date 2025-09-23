# 9. Write a program to create three lists of numbers, their squares and cubes

li = []
num = int(input("enter a numbers: "))
for i in range(0,num):
    numm = int(input("enter an elements: "))
    li.append(numm)
print('you entered list:  ',li)
cube = []
square = []
for i in li:
    cube.append(i**3)
    square.append(i**2)
print('cube of elements in list:  ',cube)
print('square of elements in list:',square)