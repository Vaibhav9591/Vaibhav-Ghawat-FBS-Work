# 5. Accept a number from user and check if this element is present in the list or 
# # not. Also tell how many times it is present in the list.

def num():
    for i in range(0,len(li)):
        if(numm == li[i]):
         print(f'number is in list')
         print('numbers in list for',li.count(numm),'times')
         break
    else:
     print(f'number is not in list')
     
li = [10,20,30,30,40,50,60]   
numm = int(input("enter a number: "))
num()