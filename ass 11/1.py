# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists

li=[10,15,20,25,30,35,40,45,50]
even=[]
odd =[]
for i in li:
    if(i%2==0):
        even.append(i)   
    else:
        odd.append(i)
print('even numbers',even)
print('odd numbers',odd)
        
   
