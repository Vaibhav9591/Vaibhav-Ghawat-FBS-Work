# 3. Write a program to find the second largest element in the list.

def second_largest():
    li = [13,120,99,35,115,33]
    max = li[0]
    second_max = 0
    for i in range(1,len(li)):
        if(li[i]>max):
            second_max = max
            max = li[i]   
        elif(li[i]>second_max):
            second_max =li[i]       
    print(f'second largest element is ',second_max)
second_largest()