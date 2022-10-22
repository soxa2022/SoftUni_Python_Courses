def find_buckets():
    coordinates = []
    for rows in range(size):
        for cols in range(size):
            if board[rows][cols] == "B":
                coordinates.append([rows, cols])
    return coordinates


def sum_col(cols):
    col_sum = 0
    for rows in range(size):
        if not board[rows][cols] == 'B':
            col_sum += board[rows][cols]
    return col_sum


size = 6
board = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]
buckets_coordinates = find_buckets()
total_points = 0

for _ in range(3):
    coordinate = [int(s) for s in list(input()) if s.isdigit()]
    if coordinate in buckets_coordinates:
        buckets_coordinates.remove(coordinate)
        total_points += sum_col(coordinate[1])
if total_points in range(100, 200):
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif total_points in range(200, 300):
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
elif total_points >= 300:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
