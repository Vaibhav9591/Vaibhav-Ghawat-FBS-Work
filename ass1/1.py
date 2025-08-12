# 1. Write a program to calculate the percentage of student based on marks of any 5
# subjects.

m1= int(input('enter marks of sub 1:'))
m2= int(input("enter marks of sub 2:"))
m3= int(input("enter marks of sub 3:"))
m4= int(input("enter marks of sub 4:"))
m5= int(input("enter marks of sub 5:"))

 
gain_marks = m1+ m2+ m3+ m4+ m5
 
percentage =(gain_marks/500)*100
print (F'total marks is: {m1+ m2+ m3+ m4+ m5}\npercentage is {percentage} %')
