type_of_flower = input()
count_flowers = int(input())
budget = int(input())
price = 0
if type_of_flower == "Roses":
    if count_flowers > 80:
        price = 5 * 0.9
    else:
        price = 5
elif type_of_flower == "Dahlias":
    if count_flowers > 90:
        price = 3.80 * 0.85
    else:
        price = 3.80
elif type_of_flower == "Tulips":
    if count_flowers > 80:
        price = 2.80 * 0.85
    else:
        price = 2.80
elif type_of_flower == "Narcissus":
    if count_flowers < 120:
        price = 3 * 1.15
    else:
        price = 3
elif type_of_flower == "Gladiolus":
    if count_flowers < 80:
        price = 2.50 * 1.20
    else:
        price = 2.50
total_price = price * count_flowers
diff = abs(total_price - budget)
if total_price <= budget:
    print(f"Hey, you have a great garden with {count_flowers} {type_of_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")



