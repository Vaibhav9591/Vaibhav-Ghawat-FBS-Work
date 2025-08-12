# 11Write a program to accept an integer amount from user and tell minimum
# number of notes needed for representing that amount.

amt = int(input("enter amt: "))
temp = amt 
notes_of_two_thousand= temp // 2000
temp = temp % 2000

notes_of_five_hundred = temp //500
temp = temp % 500

notes_of_two_hundred = temp //200
temp = temp % 200

notes_of_one_hundred = temp //100
temp = temp % 100


print(f'notesof two thousand:{notes_of_two_thousand}\nnotes of five hundred:{notes_of_five_hundred}\nnotes of two hundred: {notes_of_two_hundred}\nnotes of one hundred: {notes_of_one_hundred}')