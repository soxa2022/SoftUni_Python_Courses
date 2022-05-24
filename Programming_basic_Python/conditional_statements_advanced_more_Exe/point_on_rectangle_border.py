x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x = float(input())
y = float(input())
point_check = ""
if x == x_1 and y_1 <= y <= y_2:
    point_check = "Border"
elif x == x_2 and y_1 <= y <= y_2:
    point_check = "Border"
elif y == y_2 and x_1 <= x <= x_2:
    point_check = "Border"
elif y == y_1 and x_1 <= x <= x_2:
    point_check = "Border"
else:
    point_check = "Inside / Outside"
print(point_check)
