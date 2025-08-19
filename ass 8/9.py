# 9. Write a program to check if entered number is a palindrome or
# not.

def palindrome(num):
    num > 100 == num < 999
    
    if(str(num) == str(num) [::-1]):
        return f'{num} is palindrome number'
    else:
        return f'{num} is not palindrome number'

num = int(input("enter a number: "))   
res = palindrome(num)
print(res)