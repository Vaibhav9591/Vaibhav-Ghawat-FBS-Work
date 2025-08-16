# 5. Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount. (Use looping to optimize
# the problem)

amt = int(input("enter a amount: "))

temp = amt
while(amt>=0):
    notes_of_two_thousand = temp // 2000
    temp = temp % 2000
    notes_of_five_hundred = temp // 500
    temp = temp % 500
    notes_of_two_hundred = temp // 200
    temp = temp % 200
    notes_of_one_hundred = temp // 100
    print(f'notes of two thousand {notes_of_two_thousand}\nnotes of five hundred {notes_of_five_hundred}\nnotes of two hundred {notes_of_two_hundred}\nnotes of one hundred {notes_of_one_hundred}')
    break
    