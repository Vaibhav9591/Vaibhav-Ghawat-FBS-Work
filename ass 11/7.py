# 7. Python Program to Find the Intersection of Two Lists

li1 = [10,11,20,22,30,45,43,47]
li2 = [11,23,34,45,20,13,56,76]


res = list(filter(lambda x:x in li2,li1))

print(res)