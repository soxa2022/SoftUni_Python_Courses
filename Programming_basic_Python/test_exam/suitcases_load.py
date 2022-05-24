volume_capacity = float(input())
entering_cases = 0
count_succ_cases = 0
command_line = input()
is_full = False
while command_line != "End":
    case = float(command_line)
    entering_cases += 1
    if entering_cases % 3 == 0:
        case = case * 1.10
    if volume_capacity >= case:
        volume_capacity -= case
        count_succ_cases += 1
    else:
        print("No more space!")
        is_full = True
        break
    command_line = input()
if not is_full:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {count_succ_cases} suitcases loaded.")
