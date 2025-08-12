# 12. WAP to print Armstrong number within a given range

Range = int(input("Enter  range : "))  

for n in range(Range + 1):  
   sum = 0  
   temp = n  
   while temp > 0:  
       digit = temp % 10  
       sum = sum + digit **3 
       temp = temp // 10  
  
   if n == sum:  
       print(n)    