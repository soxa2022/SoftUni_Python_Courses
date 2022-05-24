budget = float(input())
price_flour_kg = float(input())
price_milk = (price_flour_kg * 1.25) / 4
price_eggs = price_flour_kg * 0.75
price_bread = price_eggs + price_milk + price_flour_kg
count_coloured_eggs = 0
count_bread = 0
while budget >= price_bread:
    count_bread += 1
    count_coloured_eggs += 3
    if count_bread % 3 == 0:
        count_coloured_eggs -= (count_bread - 2)
    budget -= price_bread
print(f"You made {count_bread} loaves of Easter bread! Now you have {count_coloured_eggs} eggs and {budget:.2f}BGN left.")
