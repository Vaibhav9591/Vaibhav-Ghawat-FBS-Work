# 12. Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("enter 3 digit number: "))

num>100==num<999

if(str(num) ==str(num)[::-1]):
    print(f'number is palindrome')
    
else:
    print(f'number is not palindrome')