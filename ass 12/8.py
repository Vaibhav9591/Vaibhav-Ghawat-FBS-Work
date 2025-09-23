# 8. Python Program to Remove the Characters of Odd Index Values in a
# String

str = 'vaibhav ghawat'
strr=''
for i in range(len(str)):
    if(i%2!=0):
       strr+=str[i]
print(strr,end=' ')
   