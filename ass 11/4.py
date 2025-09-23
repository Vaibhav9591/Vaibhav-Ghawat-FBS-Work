# 4. Python Program to Find the Second Largest Number in a List Using Bubble
# Sort

li = [10,20,30,40,50]
max = li[0]
smax = 0
for i in range(1,len(li)):
    for j in range(0,len(li)-1):
     if(li[j]<li[j+1]):
         smax = max
         max = li[j+1]
     elif(li[j]<smax):
         smax = li[j]
         li[j],li[j+1]=li[j+1],li[j]
print(smax)
