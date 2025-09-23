# 3. Write a program to reverse a given number using recursive function.

def reverse(num):
    if(num == 0):
        return 0
    else:
        temp = num
        while(temp>0):
         digit = temp % 10
         temp = temp // 10
         print (f'',digit,end='')
         
num = int(input("enter a number: "))
res = reverse(num)
print,res