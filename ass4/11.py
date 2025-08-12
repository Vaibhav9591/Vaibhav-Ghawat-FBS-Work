# 11. WAP to check if given number Strong Number.

num = int(input("enter a number: "))
num_str = str(num)
n = len(num_str)
sum = 0
for i in num_str:
     sum += int(i)**n
if sum == num:
    print(f'{num} is armstrong num')
else:
    print(f'{num} num is not armstrong num')  