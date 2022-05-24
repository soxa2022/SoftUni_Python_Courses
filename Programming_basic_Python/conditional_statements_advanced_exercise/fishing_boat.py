budget = int(input())
season = input()
fishersman = int(input())
ship_price = 0
if season == "Spring":
    ship_price = 3000
    if fishersman <= 6:
        ship_price = ship_price * 0.9
    elif 6 < fishersman <= 11:
        ship_price = ship_price * 0.85
    elif fishersman > 11:
        ship_price = ship_price * 0.75
elif season == "Summer" or season == "Autumn":
    ship_price = 4200
    if fishersman <= 6:
        ship_price = ship_price * 0.9
    elif 6 < fishersman <= 11:
        ship_price = ship_price * 0.85
    elif fishersman > 11:
        ship_price = ship_price * 0.75
elif season == "Winter":
    ship_price = 2600
    if fishersman <= 6:
        ship_price = ship_price * 0.9
    elif 6 < fishersman <= 11:
        ship_price = ship_price * 0.85
    elif fishersman > 11:
        ship_price = ship_price * 0.75
if season != "Autumn" and fishersman % 2 == 0:
    ship_price = ship_price * 0.95
diff = abs(budget - ship_price)
if budget >= ship_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")


