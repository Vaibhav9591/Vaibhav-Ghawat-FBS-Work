# 6. WAP to check if a given number is prime number or not.

num = int(input("enter a num: "))
i = 1
for i in range (2,num):
    if(num % i==0):
        print(f'{num} is not a prime num')
        break
else:
    print(f'{num} is prime num')
    