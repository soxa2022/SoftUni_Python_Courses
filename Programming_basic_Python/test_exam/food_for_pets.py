days = int(input())
food_quantity = float(input())
total_cat_food = 0
total_dog_food = 0
total_food = 0
biscuits = 0
count_days = 0
all_biscuits = 0
for i in range(1, days + 1):
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())
    count_days += 1
    total_cat_food += cat_eaten_food
    total_dog_food += dog_eaten_food
    if count_days % 3 == 0:
        biscuits = (cat_eaten_food + dog_eaten_food) * 0.10
        all_biscuits += biscuits
total_food = total_dog_food + total_cat_food
percent_eaten_food = total_food / food_quantity * 100
percent_dog = total_dog_food / total_food * 100
percent_cat = total_cat_food / total_food * 100
print(f"Total eaten biscuits: {round(all_biscuits)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")
