# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene
# triangle.

side1= int(input("enter side 1 : "))
side2= int(input("enter side 2 : "))
side3= int(input("enter side 3 : "))

if(side1==side2==side3):
    print('triangle is equilateral')
elif(side1==side2):
     print(f'triangle is isosceles')
elif(side1 != side2 != side3):
 print(f'triangle is scalene')
else:
  print('invalid triangle')