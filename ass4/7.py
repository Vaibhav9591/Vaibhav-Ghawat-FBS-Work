# 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.

num = int(input("enter a num: "))
i=1
for i in range(1,num):
    if(i % 3 == 1):
       if(i % 2 == 1): 
        print(i)  
    else:
     print()
i=i+1
    