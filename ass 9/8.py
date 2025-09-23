# 8. Write a program to check whether a number is prime or not using recursion.

def prime(num):
    if(num == 0):
        return 0
    else:
         for i in range(2,num):
          if(num % i == 0):
             print(f'number is not prime ')
             break
         else:
          print(f'number is prime')
        
num = int(input("enter a number: "))
res = prime(num)
print,res