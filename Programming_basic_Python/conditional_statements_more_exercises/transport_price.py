distance = int(input())
twenty_four_hours = input()
price_taxi = 0
price_bus = distance * 0.09
price_train = distance * 0.06
if distance < 20 and twenty_four_hours == "day":
    price_taxi = 0.79 * distance + 0.70
    print(f"{price_taxi:.2f}")
if distance < 20 and twenty_four_hours == "night":
    price_taxi = 0.90 * distance + 0.70
    print(f"{price_taxi:.2f}")
# if distance < 100 and distance >= 20:
if 100 > distance >= 20:
    if twenty_four_hours == "day":
        price_taxi = 0.79 * distance + 0.70
    elif twenty_four_hours == "night":
        price_taxi = 0.90 * distance + 0.70
    if price_taxi < price_bus:
        print(f"{price_taxi:.2f}")
    else:
        print(f"{price_bus:.2f}")
if distance >= 100:
    if twenty_four_hours == "day":
        price_taxi = 0.79 * distance + 0.70
    elif twenty_four_hours == "night":
        price_taxi = 0.90 * distance + 0.70
    if price_taxi < price_bus and price_taxi < price_train:
        print(f"{price_taxi:.2f}")
    elif price_train < price_bus :
        print(f"{price_train:.2f}")
    else:
        print(f"{price_bus:.2f}")


