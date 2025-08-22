# write a program to print n prime numbers

       
def isPrime(n):
    if(n==1 or n==0): 
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
num = int(input("enter a number:"))
for i in range(1,num+1):
    if(isPrime(i)):
        print(i,end=" ")