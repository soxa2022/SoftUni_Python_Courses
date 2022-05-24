import math
days_count = int(input())
food_kg = int(input())
dog_food = float(input())
cat_food = float(input())
turt_food = float(input())
turt_food = turt_food / 1000
total_food_dog = days_count * dog_food
total_food_cat = days_count * cat_food
total_food_turt = days_count * turt_food
all_food = total_food_turt + total_food_cat + total_food_dog
diff = abs(all_food - food_kg)
if food_kg >= all_food:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")
