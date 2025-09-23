# 2. Write a program to check if given number is Armstrong or not using recursive function

def armstrong(num):
    if(num == 0):
      return
    else:
        temp = num
        sum = 0
        while(temp>0):
            digit = temp%10
            sum = sum + digit**3
            temp = temp // 10
        if(num == sum):
          print(f'number is armstrong')
            
        else:
          print(f'number is not armstrong')
             
num = int(input("enter a number: "))
res = armstrong(num)
print,armstrong