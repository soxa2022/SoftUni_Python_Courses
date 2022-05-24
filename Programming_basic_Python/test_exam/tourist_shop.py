budget = float(input())
count_products = 0
money = budget
product = input()
while product != "Stop":
    price = float(input())
    count_products += 1
    if count_products % 3 == 0:
        price *= 0.50
    if money >= price:
        money -= price
    else:
        print("You don't have enough money!")
        print(f"You need {abs(money - price):.2f} leva!")
        break
    product = input()
else:
    print(f"You bought {count_products} products for {abs(money - budget):.2f} leva.")
