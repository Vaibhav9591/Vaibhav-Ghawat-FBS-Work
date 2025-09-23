# 14. Python Program to count the occurrences of each word in a string.

str="vaibhav is not a is vaibhav"
a=str.split(' ')
dic={}
for i in a:
    if(i in dic):
        dic[i]+=1
    else:
        dic[i]=1

for i,j in dic.items():
    print(i,j)
