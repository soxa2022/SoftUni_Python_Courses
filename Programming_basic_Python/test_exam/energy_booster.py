fruit = input()
type_of_set = input()
count_sets = int(input())
price = 0
numbers = 0
if type_of_set == "small":
    numbers = 2
    if fruit == "Watermelon":
        price = numbers * 56
    elif fruit == "Mango":
        price = numbers * 36.66
    elif fruit == "Pineapple":
        price = numbers * 42.10
    elif fruit == "Raspberry":
        price = numbers * 20
elif type_of_set == "big":
    numbers = 5
    if fruit == "Watermelon":
        price = numbers * 28.70
    elif fruit == "Mango":
        price = numbers * 19.60
    elif fruit == "Pineapple":
        price = numbers * 24.80
    elif fruit == "Raspberry":
        price = numbers * 15.20
total_price = price * count_sets
if 400 <= total_price <= 1000:
    total_price = total_price * 0.85
elif total_price> 1000:
    total_price *= 0.50
print(f"{total_price:.2f} lv.")

