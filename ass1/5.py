# 5. Write a program to enter P, T, R and calculate Compound Interest.

amt = int(input("enter amout: "))
t = int (input("enter year: "))
r = float (input("enter rate of intrest: "))

p = amt * (1 + r/100) **t

compound_intrest = ( p - amt)

print(f'compound_intrest is: {compound_intrest}')