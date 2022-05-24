budget = float(input())
season = input()
expenses = 0
destination = ""
vacation = ""
if budget <= 100 :
    destination = "Bulgaria"
    if season == "summer":
        expenses = budget * 0.30
        vacation = "Camp"
    else:
        expenses = budget * 0.70
        vacation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        expenses = budget * 0.40
        vacation = "Camp"
    else:
        expenses = budget * 0.80
        vacation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    vacation = "Hotel"
    expenses = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{vacation} - {expenses:.2f}")
