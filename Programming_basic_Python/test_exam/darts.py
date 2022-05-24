start_points = 301
name_player = input()
input_line = input()
counter_successful = 0
counter_unsuccessful = 0
score = 0
do_leg = False
while input_line != "Retire":
    points = int(input())
    if input_line == "Triple":
        points *= 3
    elif input_line == "Double":
        points *= 2
    score = start_points - points
    if score > 0:
        start_points = score
        counter_successful += 1

    elif score < 0:
        counter_unsuccessful += 1

    elif score == 0:
        counter_successful += 1
        do_leg = True
        break
    input_line = input()
if do_leg:
    print(f"{name_player} won the leg with {counter_successful} shots.")
else:
    print(f"{name_player} retired after {counter_unsuccessful} unsuccessful shots.")
