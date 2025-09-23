# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String

str = 'vaibhav ghawat'
strr =''
idx = int(input("enter an index: "))
for i in range(len(str)):
    if(i==idx):
        continue
    else:
     strr+=str[i]
print(strr)