# 1. Write a program to prompt user to enter user id and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

# username1 = input("enter username: ")
# password1 = input("enter password: ")

# print(f'enter again')

# username = input("enter username: ")
# password = input("enter password: ")

# credentials = username,password

# if (username1 == username):
#      if(password1 == password): 
#          while(credentials==credentials): 
#           print(f'You have login successfull.')     
#           break
#      else:
#          print(f're-enter again')
#          username = input("enter username: ")
#          password = input("enter password: ")
         
# else:
#     print(f're-enter again')


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
    