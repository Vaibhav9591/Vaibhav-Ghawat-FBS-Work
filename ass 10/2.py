# 2. Write a program to find maximum and minimum element in a list.

def max():
    li = [10,55,3,24,44,33]
    max = li[0]
    min = li[0]
    for i in range(0,len(li)):
       if(li[i]>max):
           max = li[i]
       elif(li[i]<min):
           min =li[i]
    print(f'maximum element is',max)
    print(f'minimum element is',min)     
max()