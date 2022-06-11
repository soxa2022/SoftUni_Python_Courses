from math import sqrt, pow, floor


def longer_line(x1, y1, x2, y2) -> object:
    distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    return distance


first_x = floor(float(input()))
first_y = floor(float(input()))
second_x = floor(float(input()))
second_y = floor(float(input()))
third_x = floor(float(input()))
third_y = floor(float(input()))
forth_x = floor(float(input()))
forth_y = floor(float(input()))

first_line = longer_line(first_x, first_y, second_x, second_y)
second_line = longer_line(third_x, third_y, forth_x, forth_y)
if first_line >= second_line:
    if longer_line(0, 0, first_x, first_y) <= longer_line(0, 0, second_x, second_y):
        print(f"({first_x}, {first_y})({second_x}, {second_y})")
    else:
        print(f"({second_x}, {second_y})({first_x}, {first_y})")
else:
    if longer_line(0, 0, third_x, third_y) <= longer_line(0, 0, forth_x, forth_y):
        print(f"({third_x}, {third_y})({forth_x}, {forth_y})")
    else:
        print(f"({forth_x}, {forth_y})({third_x}, {third_y})")
