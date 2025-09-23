# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

str = input("enter a string:")
list =[]
list = str.split()
freq =[list.count(p) for p in list]
print('frequency of word is ')
print(dict(zip(list,freq)))
