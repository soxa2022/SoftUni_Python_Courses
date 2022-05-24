from math import ceil

height = int(input())
width = int(input())
percents_windows = int(input())
area_walls = height * width * 4
area_for_paint = ceil(area_walls - area_walls * percents_windows / 100)
input_line = input()
while input_line != "Tired!":
    paint_lt = int(input_line)
    area_for_paint -= paint_lt
    if area_for_paint < 0:
        print(f"All walls are painted and you have {abs(area_for_paint)} l paint left!")
        break
    elif area_for_paint == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break
    input_line = input()
else:
    print(f"{area_for_paint} quadratic m left.")
