# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

num = int(input("enter a num: "))

for i in range(5,num,5):
    if(i % 7 == 0):
     print(i)
     i =i+1
     break
else:
    print("invalid num")