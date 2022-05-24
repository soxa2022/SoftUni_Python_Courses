drink = input()
sugar = input()
number_of_cups = int(input())
if drink == "Espresso" and sugar == "Without":
    total_price = (number_of_cups * 0.90) * 0.65
    if number_of_cups >= 5:
        total_price = total_price * 0.75
        if total_price > 15:
            total_price = total_price * 0.8
            print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
        else:
            print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
elif drink == "Espresso" and sugar == "Normal":
    total_price = number_of_cups * 1
    if number_of_cups >= 5:
        total_price = total_price * 0.75
        if total_price > 15:
            total_price = total_price * 0.8
            print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
        else:
            print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
elif drink == "Espresso" and sugar == "Extra":
    total_price = number_of_cups * 1.2
    if number_of_cups >= 5:
        total_price = total_price * 0.75
        if total_price > 15:
            total_price = total_price * 0.8
            print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
        else:
            print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
elif drink == "Cappuccino" and sugar == "Without":
    total_price = (number_of_cups * 1) * 0.65
    if total_price > 15:
        total_price = total_price * 0.8
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
    else:
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
elif drink == "Tea" and sugar == "Without":
    total_price = (number_of_cups * 0.50) * 0.65
    if total_price > 15:
        total_price = total_price * 0.8
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
    else:
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
elif drink == "Cappuccino" and sugar == "Normal":
    total_price = number_of_cups * 1.20
    if total_price > 15:
        total_price = total_price * 0.8
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
    else:
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
elif drink == "Cappuccino" and sugar == "Extra":
    total_price = number_of_cups * 1.60
    if total_price > 15:
        total_price = total_price * 0.8
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
    else:
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
elif drink == "Tea" and sugar == "Normal":
    total_price = number_of_cups * 0.60
    if total_price > 15:
        total_price = total_price * 0.8
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
    else:
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
elif drink == "Tea" and sugar == "Extra":
    total_price = number_of_cups * 0.70
    if total_price > 15:
        total_price = total_price * 0.8
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
    else:
        print(f"You bought {number_of_cups} cups of {drink} for {total_price:.2f} lv.")
