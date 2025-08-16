# 4. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

num = int(input("enter a num: "))
temp = num
d1= temp % 10   
temp = temp // 10
d2= temp % 10   
temp = temp // 10
d3= temp % 10   
temp = temp // 10
d4= temp % 10   
temp = temp // 10

if(d1*d1*d1 + d2*d2*d2 + d3*d3*d3 == num):
    print(f'{num} is armstrong num')
elif(d1*d1*d1*d1 + d2*d2*d2*d2 + d3*d3*d3*d3 + d4*d4*d4*d4 == num):
     print(f'{num} is armstrong num')
else:
    print(f'{num} is not armstrong num')
