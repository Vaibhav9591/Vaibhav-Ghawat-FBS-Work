# 11. WAP to check if a given number is Armstrong number or not. For

def armstrong(num):
    sum = 0
    temp = num
    while(temp>0):
        digit = temp % 10
        sum = sum + digit **3
        temp = temp // 10
    if sum == num:
        return f'{num} is armstrong number'
    else:
        return f'{num} is not armstrong number'
num = int(input("enter a number: "))
res = armstrong(num)
print(res)