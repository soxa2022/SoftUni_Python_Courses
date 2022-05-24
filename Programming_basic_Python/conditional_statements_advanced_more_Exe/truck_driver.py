season = input()
month_km = float(input())
salary = 0
# Spring", "Summer", "Autumn" или "Winter"
if month_km <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = month_km * 0.75
    elif season == "Summer":
        salary = month_km * 0.90
    elif season == "Winter":
        salary = month_km * 1.05
elif month_km <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = month_km * 0.95
    elif season == "Summer":
        salary = month_km * 1.10
    elif season == "Winter":
        salary = month_km * 1.25
elif month_km <= 20000:
    salary = month_km * 1.45
salary = (salary * 4) * 0.90
print(f"{salary:.2f}")

