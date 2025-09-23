# 7. Python Program to Remove the Given Key from a Dictionary

def remove(dict):
    keyy = int(input("enter a key for remove:"))
    if(keyy in dict):
      dict.pop(keyy)
      print(dict)
    else:
        print('key is not present in list')
dict = {1:'vaibhav',2:'ghawat',3:'ahilyanagar'}

remove(dict)
