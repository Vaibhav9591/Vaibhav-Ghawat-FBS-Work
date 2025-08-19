# 8. Write a program find reverse of a number

def reverse_num():
    num = int(input("enter a number: "))
    
    temp = num
    d1 = temp % 10
    temp = temp //10
    d2 = temp % 10
    temp = temp //10
    d3 = temp % 10
    temp = temp //10
    
    print('reverse of this number is',d1,d2,d3)
reverse_num()