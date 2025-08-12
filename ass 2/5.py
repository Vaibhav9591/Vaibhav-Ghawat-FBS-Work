# 5 WAP to calculate selling price of book based on cost price and discount.

cost_price= int(input("enter cost price: "))
discount_percent = float(input("enter discount in percent: "))

discount_percent= cost_price/100 *discount_percent
selling_price = (cost_price + discount_percent)

print(f'discount is: {discount_percent}\nselling price is {selling_price}')

