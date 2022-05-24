days_of_vacation = int(input())
type_of_room = input()
rating = input()
price = 0
days_of_vacation = days_of_vacation - 1
if type_of_room == "room for one person":
    price = 18
elif type_of_room == "apartment":
    price = 25
    if days_of_vacation < 10:
        price = price * 0.70
    elif 10 <= days_of_vacation <= 15:
        price *= 0.65
    elif days_of_vacation > 15:
        price *= 0.50
elif type_of_room == "president apartment":
    price = 35
    if days_of_vacation < 10:
        price = price * 0.90
    elif 10 <= days_of_vacation <= 15:
        price *= 0.85
    elif days_of_vacation > 15:
        price *= 0.80
if rating == "positive":
    price = price * 1.25
else:
    price *= 0.90
total_price = price * days_of_vacation
print(f"{total_price:.2f}")
