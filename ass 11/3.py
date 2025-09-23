# 3. Python Program to Sort the List According to the Second Element in Sublist

li = [[10,23],[44,22],[32,56],[25,27]]
li.sort(key=lambda x: x[1])
print(li)
