lst_collection = [[item for item in items.split('->')] for items in input().split("|")]
money = float(input())
lst_prices = []
budget = money
for i in range(len(lst_collection)):
    new_price = 0
    price = float(lst_collection[i][1])
    product = lst_collection[i][0]
    if budget < price:
        continue
    if product == "Clothes" and price <= 50.00:
        budget -= price
        new_price = price * 1.40
        lst_prices.append(new_price)
    elif product == "Shoes" and price <= 35.00:
        budget -= price
        new_price = price * 1.40
        lst_prices.append(new_price)
    elif product == "Accessories" and price <= 20.50:
        budget -= price
        new_price = price * 1.40
        lst_prices.append(new_price)
total_money = budget + sum(lst_prices)
print(*[f"{num:.2f}" for num in lst_prices])
print(f"Profit: {(sum(lst_prices) - (sum(lst_prices) / 1.40)):.2f}")
if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

