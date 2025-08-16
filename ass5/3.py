# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

num = int(input("enter a num of passenger:  "))
cost = float(input("enter a cost of ticket: "))
age = int(input("enter age: "))

if(age<12):
    discount = cost*30/100
    cost_price = cost - discount 
    print(f'{cost_price*num}\neach person should pay {cost_price}')
    
elif(age>59):
     discount = cost*50/100
     cost_price = cost - discount 
     print(f'{cost_price*num}\neach person should pay {cost_price}')
        
else:
 print(f'You have to pay full amt {cost*num}\neach person should pay {cost}')
