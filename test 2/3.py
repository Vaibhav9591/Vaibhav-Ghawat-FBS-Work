# 3. A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

length = 50
breadth = 40

area_of_circle = 1.57 * 20*20
area = length * breadth + area_of_circle
print(f"total area of fencing is {area} mtr")

times = 35*5
total_cost = area*times

print(f'cost of fancing is {total_cost}')