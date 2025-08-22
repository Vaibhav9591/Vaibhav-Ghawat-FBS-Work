#2.
# Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.

num = int(input("enter three digit num: "))


d1 = num // 100

d2 = (num//10) %10

d3 = num % 10

if (d1 == 2* d2 and d1 * 2 ==d3):
    print(f'you have done it')
else:
    print(f'try again')
