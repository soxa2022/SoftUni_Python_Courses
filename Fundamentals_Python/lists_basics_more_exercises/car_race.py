lst_number = [int(num) for num in input().split(" ")]
mid_index = len(lst_number) // 2
left_car = lst_number[:mid_index]
right_car = lst_number[mid_index + 1:]
right_car = right_car[::-1]
time_left = 0
time_right = 0
for i in left_car:
    if i == 0:
        time_left *= 0.8
    time_left += i
for j in right_car:
    if j == 0:
        time_right *= 0.8
    time_right += j
if time_left < time_right:
    print(f"The winner is left with total time: {time_left:.1f}")
elif time_left > time_right:
    print(f"The winner is right with total time: {time_right:.1f}")