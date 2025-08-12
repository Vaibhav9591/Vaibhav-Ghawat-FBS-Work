# 8. Write a program to convert days into years, weeks and days.

days = int(input('enter days :'))
years = days // 365
remaining_days = days % 365

weeks = remaining_days // 7

days = remaining_days % 7

print (f'years: {years}\nweeks: {weeks} \ndays: {days}')