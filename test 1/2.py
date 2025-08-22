# 2. Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100)
amt = int(input("enter amt:"))
rate = int(input("enter rate: "))
years = int(input("enter time: "))

amt= amt*rate*years/100

print(f'inrest for {years}years is: {amt}')