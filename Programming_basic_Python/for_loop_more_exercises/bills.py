months = int(input())
water = 20
internet = 15
other_expenses = 0
total_electricity = 0
for i in range(1, months + 1):
    electric = float(input())
    total_electricity = total_electricity + electric
    other_expenses = other_expenses + (electric + water + internet) * 1.20
total_water = water * months
total_internet = internet * months
total_expenses = total_water + total_internet + total_electricity + other_expenses
average = total_expenses / months
print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {other_expenses:.2f} lv")
print(f"Average: {average:.2f} lv")