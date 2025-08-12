# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1=int(input("enter marks of subject 1: "))
sub2=int(input("enter marks of subject 2: "))
sub3=int(input("enter marks of subject 3: "))
sub4=int(input("enter marks of subject 4: "))
sub5=int(input("enter marks of subject 5: "))

total_marks= (sub1+sub2+sub3+sub4+sub5) / 5

if(total_marks>=90):
    print(f'pass with first class  ')

elif(total_marks>=80):
    print(f'pass with second class ')
    
elif(total_marks>=70):
    print(f'pass with third class  ')

elif(total_marks>=60):
    print(f'pass with four class  ')

elif(total_marks>=50):
    print(f'pass with five class ')
    
else:
    print(f'student is fail')