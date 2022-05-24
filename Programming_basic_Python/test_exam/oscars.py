name_actor = input()
points_actor = float(input())
count_rate_man = int(input())
is_winner = False
for i in range(1, count_rate_man + 1):
    rate_man = input()
    points_of_rate = float(input())
    points_actor += (len(rate_man) * points_of_rate) / 2
    if points_actor >= 1250.5:
        is_winner = True
        break
if is_winner:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points_actor:.1f}!")
else:
    diff = abs(1250.5 - points_actor)
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")