heritage = float(input())
year_to_live = int(input())
money_to_live = 0
age = 17
for i in range (1800, year_to_live + 1):
    if i % 2 == 0:
        age = age + 1
        money_to_live = money_to_live + 12000
    else:
        age = age + 1
        money_to_live = money_to_live + 12000 + 50 * age
diff = abs(heritage - money_to_live)
if heritage >= money_to_live:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")


