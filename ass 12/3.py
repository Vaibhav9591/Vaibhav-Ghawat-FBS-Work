# 3. Python Program to Detect if Two Strings are Anagrams

str1 = input('enter a string:')
str2 = input('enter a string:')

if(len(str1)!=len(str2)):
    print('string is not anagram')
elif sorted(str1)==sorted(str2):
    print('string is anagram')
else:
    ('string is not anagram')