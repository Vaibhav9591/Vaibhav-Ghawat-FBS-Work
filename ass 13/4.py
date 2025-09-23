# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).
    
def number(n):
  square= {}
  for i in range(1, n + 1):
    square[i] =  i*i
  return square

num = int(input("Enter a number : "))
res = number(num)
print(f"The generated dictionary is:{res}")
