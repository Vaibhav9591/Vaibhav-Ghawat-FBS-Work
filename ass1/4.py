# 4. Write a program to enter P, T, R and calculate simple Interest.


p = float(input(" enter principal amt: "))
t = float(input(" enter time: "))
r = float(input(" enter rate of intrest: "))

calculate = p * r * t / 100
 
print(f'simple intrest is {calculate}')