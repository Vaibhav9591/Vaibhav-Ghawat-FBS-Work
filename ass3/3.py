# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1= int(input("enter side 1 : "))
angle2= int(input("enter side 2 : "))
angle3= int(input("enter side 3 : "))

if(angle1+angle2>angle3):
    print(f'triangle is valid')
else:
    print(f'triangle is not valid')