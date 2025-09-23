# 6. Write a program to remove duplicates from the list.

def duplicate():
  
    list=[]
    for i in li:
        if i not in list:
            list.append(i)      
    return list
li = [1,2,2,3,3,4,5,5,6]
print('before removing list: ',li)
list =duplicate()
print('after removing duplicate: ',list)