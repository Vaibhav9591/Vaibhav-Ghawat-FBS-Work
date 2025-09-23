# 5. Python Program to Count the Number of Vowels in a String

str = 'Vaibhav Ghawat'
vowels = 0
for i in str:
    if(i == 'a'or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels+=1
print(vowels)