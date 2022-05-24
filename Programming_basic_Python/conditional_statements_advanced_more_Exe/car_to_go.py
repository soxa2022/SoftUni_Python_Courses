budget = float(input())
season = input()
klass = ""
car = ""
price = 0
if budget <= 100:
    klass = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        car = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    klass = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        car = "Jeep"
        price = budget * 0.80
else:
    klass = "Luxury class"
    car = "Jeep"
    price = budget * 0.90
print(klass)
print(f"{car} - {price:.2f}")


