budget = float(input())
category = input()
count_fans = int(input())
price_ticket = 0
transport_price = 0
if category == "VIP":
    price_ticket = 499.99
    if 1 <= count_fans <= 4:
        transport_price = budget * 0.75
    elif 4 < count_fans <= 9:
        transport_price = budget * 0.60
    elif 9 < count_fans <= 24:
        transport_price = budget * 0.50
    elif 25 < count_fans <= 49:
        transport_price = budget * 0.40
    else:
        transport_price = budget * 0.25
if category == "Normal":
    price_ticket = 249.99
    if 1 <= count_fans <= 4:
        transport_price = budget * 0.75
    elif 4 < count_fans <= 9:
        transport_price = budget * 0.60
    elif 9 < count_fans <= 24:
        transport_price = budget * 0.50
    elif 25 < count_fans <= 49:
        transport_price = budget * 0.40
    else:
        transport_price = budget * 0.25
total_cost = transport_price + count_fans * price_ticket
diff = abs(budget - total_cost)
if budget >= total_cost:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
