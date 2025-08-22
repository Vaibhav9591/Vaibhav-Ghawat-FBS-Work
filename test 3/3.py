# 3. Write a program to accept basic salary of n emp. (n should be
# accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and
# hra=20%. Based on this calculate the total salary of each emp
# and also total salary of all emp.

basic_salary= float(input("enter your basic salary: "))

if(basic_salary<=20000):
    da = 10*100
    ta = 12*100
    hrs =15*100
    total_salary = da+ta+hrs+basic_salary
    print(f'da is{da},ta is {ta},hrs is {hrs}\nyour total salary is {total_salary}')
else:
    da = 15*100
    ta = 18*100
    hrs =20*100
    total_salary = da+ta+hrs+basic_salary
    print(f'da is{da},ta is {ta},hrs is {hrs}\nyour total salary is {total_salary}')
    