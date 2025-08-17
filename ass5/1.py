# 1. Write a program to prompt user to enter user id and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.


user_id=(input("enter user id = "))
password=input("enter password = ")

print("re-enter user id and password")

for i in range(1,4):
    user_id1=input("enter user id = ")
    password2=input("enter password = ")
    if(user_id1==user_id and password2==password):
     print("You login successfull")
     break
    else:
     print("Your user id and password is incorrect")
    
else:
    print("Your account is blocked.")
    