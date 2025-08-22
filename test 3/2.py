# 2. Write a program to calculate the sum of following series
# where n is input by user.
# 1/1! + 2/2! + 3/3! + 4/4! + ... N/N!

def sumOfSeries(num):
    res = 0
    fact = 1
    for i in range(1, num+1):
        fact *= i
        res = res + (i/ fact)
        
    return res

num = int(input("enter a number: "))
print("Sum: ", sumOfSeries(num))