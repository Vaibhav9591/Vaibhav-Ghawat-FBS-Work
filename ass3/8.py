# 8. Write a program to prompt user to enter user id and password. After verifying
# user id and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

username= (input("enter username: "))
password= (input("enter your password: "))

import random
captcha = random.randint(1111,9999)

print(captcha)

captchaa= int(input("enter captcha: "))
              
if(captcha==captchaa):
    print(f'you login succesfully')

else:
    print(f'you failed to login')
    