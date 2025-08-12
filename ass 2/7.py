# 7 Find the sum of three-digit number.

num = int(input( "enter three digit num: "))

temp = num
d1= temp % 10
temp= temp // 10

d2 = temp % 10
temp= temp // 10

d3 = temp % 10
temp= temp //10

add_of_num = d1+d2+d3

print(f'd1:{d1}\nd2:{d2}\nd3:{d3}\naddition of three digit num is: {add_of_num}')


