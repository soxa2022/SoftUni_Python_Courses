from math import pi
radius = float(input())
area_circle = radius ** 2 * pi
perimeter_circle = 2 * pi * radius
print(f"{area_circle:.2f}")
print(f"{perimeter_circle:.2f}")
# print("{:0.2f}".format(area_circle))
# print("{:0.2f}".format(perimeter_circle))