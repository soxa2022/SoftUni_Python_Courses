from math import floor
number_balls = int(input())
total_points = 0
counter_red = 0
counter_orange = 0
counter_yellow = 0
counter_white = 0
counter_black = 0
counter_other = 0
for balls in range(1, number_balls + 1):
    colour_ball = input()
    if colour_ball == "red":
        total_points += 5
        counter_red += 1
    elif colour_ball == "orange":
        total_points += 10
        counter_orange += 1
    elif colour_ball == "yellow":
        total_points += 15
        counter_yellow += 1
    elif colour_ball == "white":
        total_points += 20
        counter_white += 1
    elif colour_ball == "black":
        total_points = floor(total_points / 2)
        counter_black += 1
    else:
        total_points = total_points
        counter_other += 1
print(f"Total points: {total_points}")
print(f"Red balls: {counter_red}")
print(f"Orange balls: {counter_orange}")
print(f"Yellow balls: {counter_yellow}")
print(f"White balls: {counter_white}")
print(f"Other colors picked: {counter_other}")
print(f"Divides from black balls: {counter_black}")
