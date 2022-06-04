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
    if product == "Clothes":
        if 0 < price <= 50.00:
            budget -= price
            new_price = price * 1.40
            lst_prices.append(new_price)
    elif product == "Shoes":
        if 0 < price <= 35.00:
            budget -= price
            new_price = price * 1.40
            lst_prices.append(new_price)
    elif product == "Accessories":
        if 0 < price <= 20.50:
            budget -= price
            new_price = price * 1.40
            lst_prices.append(new_price)
total_money = budget + sum(lst_prices)
for new_price in lst_prices:
    print(f'{new_price:.2f}', end=' ')
print('')
print(f"Profit: {(sum(lst_prices) - (sum(lst_prices) / 1.40)):.2f}")
if total_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
