sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

day_add = int(input("how much was sold on finaly day of week 2"))
print(day_add)
sales_w2.append(day_add)
print(sales_w2)
sales.extend(sales_w1)
sales.extend(sales_w2)
print("max",max(sales))
print("min",min(sales))
print("sum",sum(sales))