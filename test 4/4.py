#4.wap to check if number is palindrome or not using recursion
def palindrome ():
    if (num == 0):
        return 0
    else:
        temp = num
        rev = 0
        while(temp>0):
            digit = temp % 10
            rev = rev * 10 + digit
            temp= temp // 10
        if (num == rev):
            print(f'num is palindrome')
        else:
            print(f'num is not palindrome')

num = int(input("enter number: "))
res = palindrome()  
print,res


