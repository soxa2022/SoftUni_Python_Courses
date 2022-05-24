profit = float(input())
total_money = 0
cocktail = input()
is_complete = False
while cocktail != "Party!":
    count_cocktails = int(input())
    price_cocktail = len(cocktail)
    income_money = count_cocktails * price_cocktail
    if income_money % 2 != 0:
        income_money = income_money * 0.75
    total_money += income_money
    if total_money >= profit:
        is_complete = True
        print("Target acquired.")
        break
    cocktail = input()
if is_complete:
    print(f"Club income - {total_money:.2f} leva.")
else:
    diff = profit - total_money
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {total_money:.2f} leva.")
