# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n

def additionofnumber():    
    num = int(input("enter a number: "))
    total = 0
    for i in range(1,num+1):
     total +=i
    print(f'sum of 1 to {num} is:',total)
additionofnumber()

# b. 1!+ 2! + 3! + 4!+..... + n!

# num = int(input("enter a number: "))
# def fact(x):  
#     fact = 1
#     for i in range (1,x+1):
#      fact = fact*i
#     return fact
# total = 0
# for i in range(1,num+1):
#     total+=fact(i)
# print(f'sum of factorial form 1 to {num} is {total}')
        
# c. 1^1 + 2^2 + 3^3+ ...... n^n

# def exponensial():
#     num = int(input("enter a number: "))
#     total =0
#     for i in range (1,num+1):
#         total += i**i
#     print(f'sum of series from 1 to {num} is ',total)
# exponensial()