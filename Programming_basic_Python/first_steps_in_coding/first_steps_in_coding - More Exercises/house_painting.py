height_house = float(input())
length_house = float(input())
height_side_triangle = float(input())
area_big_sides = 2 * (height_house * length_house - 1.5 * 1.5)
area_small_sides = (height_house ** 2) * 2 - 2 * 1.2
total_area_sides = area_small_sides + area_big_sides
area_triangle = (height_house * height_side_triangle) / 2
total_area_roof = 2 * area_triangle + 2 * (length_house * height_house)
green_paint = total_area_sides / 3.4
red_paint = total_area_roof / 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
# print("{:0.2f}".format(green_paint))
# print("{:0.2f}".format(red_paint))
