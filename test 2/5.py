# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST

product1= float(input("enter 1 product price: "))
product2= float(input("enter 2 product price: "))
product3= float(input("enter 3 product price: "))
product4= float(input("enter 4 product price: "))
product5= float(input("enter 5 product price: "))

product_price1 = product1 *18/100
product_price1 = product_price1 + product1

product_price2 = product2 *18/100
product_price2 = product_price2 + product2

product_price3 = product3 *18/100
product_price3 = product_price3 + product3

product_price4 = product4 *18/100
product_price4 = product_price4 + product4

product_price5 = product5 *18/100
product_price5 = product_price5 + product5

print (f'total bill is after adding gst\n{product_price1}\n{product_price2}\n{product_price3}\n{product_price4}\n{product_price5}')