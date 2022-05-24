customers = int(input())
total_spend_money = 0
for i in range(1, customers + 1):
    sum_customer = 0
    count_products = 0
    product = input()
    while product != "Finish":
        if product == "basket":
            sum_customer += 1.50
            count_products += 1
        elif product == "wreath":
            sum_customer += 3.80
            count_products += 1
        elif product == "chocolate bunny":
            sum_customer += 7
            count_products += 1
        product = input()
    if count_products % 2 == 0:
        sum_customer = sum_customer * 0.80
    print(f"You purchased {count_products} items for {sum_customer:.2f} leva.")
    total_spend_money += sum_customer
average_spend_money = total_spend_money / customers
print(f"Average bill per client is: {average_spend_money:.2f} leva.")
