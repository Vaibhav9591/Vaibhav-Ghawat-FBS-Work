# 5. Sum of all prime numbers between 1 to n

def prime (num):
    total = 0
    for i in range(2,num+1):
        flag = 1
        for j in range(2, i // 2 + 1):
            if i % j == 0:
               flag = 0
               break
        if flag:
         total +=i  
    return total
num = int(input("enter a number: "))
res =prime(num)
print(f'sum of prime of number 1 to {num} is {res}')
