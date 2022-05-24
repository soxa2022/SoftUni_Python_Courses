bottles = int(input())
quantity_ml = bottles * 750
sum_dishes = 0
sum_pots = 0
count_washes = 1
spend_washer = 0
input_line = input()
while input_line != "End":
    things = int(input_line)
    if count_washes % 3 == 0:
        spend_washer = things * 15
        quantity_ml = quantity_ml - spend_washer
        sum_pots = things + sum_pots
    else:
        spend_washer = things * 5
        quantity_ml = quantity_ml - spend_washer
        sum_dishes += things
    if quantity_ml < 0:
        print(f"Not enough detergent, {abs(quantity_ml)} ml. more necessary!")
        break
    input_line = input()
    count_washes += 1
else:
    print("Detergent was enough!")
    print(f"{sum_dishes} dishes and {sum_pots} pots were washed.")
    print(f"Leftover detergent {quantity_ml} ml.")


