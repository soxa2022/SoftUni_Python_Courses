budget = float(input())
count_serials = int(input())
total_price = 0
for serial in range(1, count_serials + 1):
    name = input()
    price_serial = float(input())
    if name == "Thrones":
        price_serial *= 0.50
    elif name == "Lucifer":
        price_serial *= 0.60
    elif name == "Protector":
        price_serial *= 0.70
    elif name == "TotalDrama":
        price_serial *= 0.80
    elif name == "Area":
        price_serial *= 0.90
    total_price += price_serial
diff = abs(budget - total_price)
if budget >= total_price:
    print(f"You bought all the series and left with {diff:.2f} lv.")
else:
    print(f"You need {diff:.2f} lv. more to buy the series!")
