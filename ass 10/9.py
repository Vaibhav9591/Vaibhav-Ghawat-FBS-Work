# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

def even_odd():
    li=[]
    n=int(input("Enter number of elements:"))
    for i in range(1,n+1):
        b=int(input("Enter element:"))
        li.append(b)
    even=[]
    odd=[]
    for j in li:
        if(j%2==0):
            even.append(j)
        else:
            odd.append(j)
    print("The even numbers list",even)
    print("The odd numbers list",odd)
even_odd()