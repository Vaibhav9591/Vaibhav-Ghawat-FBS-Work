# 6. Write a program to calculate profit or loss.

sp = float(input("enter selling price: "))
cp = float(input("entet cost price: "))


if(sp>cp):
    profit = sp - cp
    print(f'profit is :{profit}')
else:
    loss = cp-sp
    print(f'loss is :{loss}')