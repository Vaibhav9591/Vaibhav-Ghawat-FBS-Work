# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

num = int(input("enter number of students: "))
marks1 = float(input("enter marks of 1 subject: "))
marks2 = float(input("enter marks of 2 subject: "))
marks3 = float(input("enter marks of 3 subject: "))
marks4 = float(input("enter marks of 4 subject: "))
marks5 = float(input("enter marks of 5 subject: "))

Total_marks = marks1+marks2+marks3+marks4+marks5 % num 
percentage = Total_marks /500 *100

average_percentage = percentage % 10 + percentage
print(f'all percentage is {percentage}\naverage percentage of studernt: {average_percentage}')