

# b. 1 
#    2 3
#    4 5 6
#    7 8 9 10

temp=0
for i in range(1,5):
    for j in range(1,i+1):
        temp=temp+1
        print(temp,end=' ')
    print()