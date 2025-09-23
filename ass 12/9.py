# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

str = 'vaibhav ghawat'
count = 1
for char in str:
    if(char == ' '):
        count+=1

print('number of words:',count)
print(f'the characters:',len(str))