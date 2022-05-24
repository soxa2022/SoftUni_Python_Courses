walk_minutes = int(input())
count_walks = int(input())
calories = int(input())
burn_calories = walk_minutes * count_walks * 5
if burn_calories >= calories * 0.50:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burn_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burn_calories}.")

