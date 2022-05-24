import math
days = int(input())
left_food = int(input())
food_first_dear = float(input())
food_second_dear = float(input())
food_third_dear = float(input())
first_dear_all_days = days * food_first_dear
second_dear_all_days = days * food_second_dear
third_dear_all_days = days * food_third_dear
needed_food_for_dears = first_dear_all_days + second_dear_all_days + third_dear_all_days
diff = left_food - needed_food_for_dears
if diff >= 0:
    print(f"{(math.floor(abs(diff)))} kilos of food left.")
else:
    print(f"{(math.ceil(abs(diff)))} more kilos of food are needed.")

