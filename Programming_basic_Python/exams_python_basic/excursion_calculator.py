count_people = int(input())
season = input()
price_vacation = 0

if count_people <= 5:
    if season == "spring":
        price_vacation += count_people * 50
    elif season == "summer":
        price_vacation += count_people * 48.50
        price_vacation = price_vacation * 0.85
    elif season == "autumn":
        price_vacation += count_people * 60
    elif season == "winter":
        price_vacation += count_people * 86
        price_vacation *= 1.08
elif count_people > 5:
    if season == "spring":
        price_vacation += count_people * 48
    elif season == "summer":
        price_vacation += count_people * 45
        price_vacation = price_vacation * 0.85
    elif season == "autumn":
        price_vacation += count_people * 49.50
    elif season == "winter":
        price_vacation += count_people * 85
        price_vacation *= 1.08
print(f"{price_vacation:.2f} leva.")
