# 13. Python Program to count number of digits and letters in a string.

str = 'vaibhav9591ghawat'
digit = 0
letters = 0
for i in str:
    if(i.isdigit()):
        digit+=1
    else:
        i.isalpha()
        letters+=1
print('digit is :',digit)
print('letters are:',letters)