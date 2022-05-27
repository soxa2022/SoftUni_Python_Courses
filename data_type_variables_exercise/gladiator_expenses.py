count_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0
count_shield_broke = 0
for number in range(1, count_lost_fights + 1):
    if number % 2 == 0:
        total_expenses += helmet_price
    if number % 3 == 0:
        total_expenses += sword_price
    if number % 3 == 0 and number % 2 == 0:
        total_expenses += shield_price
        count_shield_broke += 1
        if count_shield_broke % 2 == 0:
            total_expenses += armor_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")

number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmets_broken = number_of_lost_fights // 2
total_sword_broken = number_of_lost_fights // 3
total_shield_broken = number_of_lost_fights // 6
total_armor_broken = total_shield_broken // 2
expenses = total_helmets_broken * helmet_price + \
    total_sword_broken * sword_price + \
    total_shield_broken * shield_price + \
    total_armor_broken * armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")
