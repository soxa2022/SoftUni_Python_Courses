steps_to_reach = 10000
steps_now = input()
total_steps_for_day = 0
diff = 0
is_reached = False
while steps_now != "Going home":
    steps_now = int(steps_now)
    total_steps_for_day += steps_now
    if total_steps_for_day >= steps_to_reach:
        break
    steps_now = input()
if steps_now == "Going home":
    steps_to_home = int(input())
    total_steps_for_day += steps_to_home
diff = abs(steps_to_reach - total_steps_for_day)
if total_steps_for_day >= steps_to_reach:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")