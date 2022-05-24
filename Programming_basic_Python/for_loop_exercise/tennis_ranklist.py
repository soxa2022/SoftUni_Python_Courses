from math import floor
count_tournaments = int(input())
start_points = int(input())
final_points = start_points
counter = 0
for i in range(1, count_tournaments + 1):
    result = input()
    if result == "W":
        final_points = final_points + 2000
        counter += 1
    elif result == "F":
        final_points = final_points + 1200
    elif result == "SF":
        final_points += 720
average_points = floor((final_points - start_points) / count_tournaments)
percent = counter / count_tournaments * 100
print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent:.2f}%")

