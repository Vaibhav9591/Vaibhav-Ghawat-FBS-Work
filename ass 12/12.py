# 12. Python Program to count number of lowercase characters in a string.

str = 'vaiBHav GhawaT'
lower = 0
for i in str:
    if(i.islower()):
        lower+=1
print(lower)
