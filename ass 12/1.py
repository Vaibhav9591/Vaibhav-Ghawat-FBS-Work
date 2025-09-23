# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

str = 'vaibhav ghawat'
replace = 'a'
char = '&'

strr = ''.join([char if char != replace else char for char in str])
print(strr)

