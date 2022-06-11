from math import sqrt, pow, floor


def center_point(x1, y1):
    distance = sqrt(pow((x1 - 0), 2) + pow((y1 - 0), 2))
    return distance


first_x = floor(float(input()))
first_y = floor(float(input()))
second_x = floor(float(input()))
second_y = floor(float(input()))

min_distance = center_point(first_x, first_y)
if center_point(second_x, second_y) < min_distance:
    min_distance = center_point(second_x, second_y)
    print(f"({second_x}, {second_y})")
else:
    print(f"({first_x}, {first_y})")
