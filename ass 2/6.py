# 6 WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

salary = float(input("enter salary: "))
da = salary*10/100
ta = salary*12/100
hrs = salary*15/100

basic_salary = (salary - da - ta - hrs ) 
print(f'da is: {da}\nta is:{ta}\nhrs is: {hrs}\nyour basic salary is {basic_salary}')


