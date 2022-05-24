name_actor = input()
points_of_academy = float(input())
count_rate_man = int(input())
points_actor = points_of_academy
for i in range(1, count_rate_man + 1):
    rate_man = input()
    points_of_rate = float(input())
    points_actor = points_actor + (len(rate_man) * points_of_rate) / 2
    if points_actor >= 1250.5:
        break
if points_actor >= 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points_actor:.1f}!")
else:
    diff = abs(1250.5 - points_actor)
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
