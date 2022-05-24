fuel_type = input()
quantity_fuel = float(input())
discount_card = input()
total_price = 0
if discount_card == "Yes":
    price_gas = 0.93 - 0.08
    price_gasoline = 2.22 - 0.18
    price_diesel = 2.33 - 0.12
    if fuel_type == "Gas":
        total_price = quantity_fuel * price_gas
        if quantity_fuel < 20:
            print(f"{total_price:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            print(f"{(total_price * 0.92):.2f} lv.")
        else: print(f"{(total_price * 0.90):.2f} lv.")
    if fuel_type == "Gasoline":
        total_price = quantity_fuel * price_gasoline
        if quantity_fuel < 20:
            print(f"{total_price:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            print(f"{(total_price * 0.92):.2f} lv.")
        else: print(f"{(total_price * 0.90):.2f} lv.")
    if fuel_type == "Diesel":
        total_price = quantity_fuel * price_diesel
        if quantity_fuel < 20:
            print(f"{total_price:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            print(f"{(total_price * 0.92):.2f} lv.")
        else: print(f"{(total_price * 0.90):.2f} lv.")
if discount_card == "No":
    price_gas = 0.93
    price_gasoline = 2.22
    price_diesel = 2.33
    if fuel_type == "Gas":
        total_price = quantity_fuel * price_gas
        if quantity_fuel < 20:
            print(f"{total_price:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            print(f"{(total_price * 0.92):.2f} lv.")
        else: print(f"{(total_price * 0.90):.2f} lv.")
    if fuel_type == "Gasoline":
        total_price = quantity_fuel * price_gasoline
        if quantity_fuel < 20:
            print(f"{total_price:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            print(f"{(total_price * 0.92):.2f} lv.")
        else: print(f"{(total_price * 0.90):.2f} lv.")
    if fuel_type == "Diesel":
        total_price = quantity_fuel * price_diesel
        if quantity_fuel < 20:
            print(f"{total_price:.2f} lv.")
        elif 20 <= quantity_fuel <= 25:
            print(f"{(total_price * 0.92):.2f} lv.")
        else: print(f"{(total_price * 0.90):.2f} lv.")



