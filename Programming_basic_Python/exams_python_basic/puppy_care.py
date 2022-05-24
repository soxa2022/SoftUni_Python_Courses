bought_food_kg = int(input())
total_eaten_food = 0
command_line = input()
while command_line != "Adopted":
    eaten_food_gr = int(command_line)
    total_eaten_food += eaten_food_gr
    command_line = input()
bought_food_gr = bought_food_kg * 1000
diff = abs(bought_food_gr - total_eaten_food)
if bought_food_gr >= total_eaten_food:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
