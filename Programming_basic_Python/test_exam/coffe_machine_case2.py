drink = input()
sugar = input()
number_of_cups = int(input())
price = 0
if drink == "Espresso":
    if sugar == "Without":
        price = price + 0.90 * number_of_cups
        price = price * 0.65
    else:
        if sugar == "Normal":
            price = price + 1.00 * number_of_cups
        else:
            if sugar == "Extra":
                price = price + 1.20 * number_of_cups
    if number_of_cups >= 5:
        price = price * 0.75
if drink == "Cappuccino":
    if sugar == "Without":
        price = price + 1.00 * number_of_cups
        price = price * 0.65
    else:
        if sugar == "Normal":
            price = price + 1.20 * number_of_cups
        else:
            if sugar == "Extra":
                price = price + 1.60 * number_of_cups
if drink == "Tea":
    if sugar == "Without":
        price = price + 0.50 * number_of_cups
        price = price * 0.65
    else:
        if sugar == "Normal":
            price = price + 0.60 * number_of_cups
        else:
            if sugar == "Extra":
                price = price + 0.70 * number_of_cups
if price > 15:
    price = price * 0.8
print(f"You bought {number_of_cups} cups of {drink} for {price:.2f} lv.")
