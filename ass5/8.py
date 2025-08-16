# 8. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3 + N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

#a
num = int(input("enter a number: "))
fact = 1
total = 0
for i in range (1,num+1):
    fact = fact*i
    total+=fact
print(f'sum of factorial form 1 to {num} is {total}')


#b.
# num = int(input("enter a number: "))
# total = 0
# for i in range(1,num+1): 
#     total += i**i   
# print(total)

#c.
# num = int (input("enter a number: "))
# a =1
# r =2
# if(r==1):
#     print(a*num)
# else:
#     print(a*(r**num-1)//(r-1))


# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# num = int(input("enter a number: "))
# total =0
# for i in range(1,num+1):
#     temp = (num ** i)/i
#     total += temp
# print(f'the sum of this series from 1 to {num} is:',total)


#e.x - x2/3 + x3/5 - x4/7 + .... to n terms
# num = int(input("enter a number: "))
# sum = 0
# s = 1 
# for i in range(1, num + 1):
#     numerator = num ** i
#     denominator = 2 * i - 1
#     term = (numerator / denominator) * s
#     sum += term
        
#     s*= -1
# print(f'sum of series is {sum}')