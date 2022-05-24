hall_capacity = int(input())
input_line = input()
total_money = 0
count_people = 0
is_full = False
while input_line != "Movie time!":
    people = int(input_line)
    count_people += people
    if count_people > hall_capacity:
        is_full = True
        print("The cinema is full.")
        break
    total_money += people * 5
    if people % 3 == 0:
        total_money -= 5
    input_line = input()
if is_full:
    print(f"Cinema income - {total_money} lv.")
else:
    print(f"There are {hall_capacity - count_people} seats left in the cinema.")
    print(f"Cinema income - {total_money} lv.")
