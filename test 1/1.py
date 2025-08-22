# 1. Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:

length= int(input('enter a length: '))
breadth= int(input('enter a bradth: '))
radius= int(input('enter a radius: '))

area = length*breadth

perimeter = 3.14*radius**2

print(f'area is: {area}\nperimeter is: {perimeter}')