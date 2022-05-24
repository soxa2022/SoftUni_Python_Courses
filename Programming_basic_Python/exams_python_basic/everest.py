command_line = input()
count_days = 1
is_failed = False
climb_meters_per_day = 5364
while command_line != "END":
    if command_line == "Yes":
        count_days += 1
    meters = int(input())
    if count_days > 5:
        print(f"Failed!")
        print(f"{climb_meters_per_day}")
        break
    climb_meters_per_day += meters
    if climb_meters_per_day >= 8848:
        print(f"Goal reached for {count_days} days!")
        break
    command_line = input()
else:
    print(f"Failed!")
    print(f"{climb_meters_per_day}")
