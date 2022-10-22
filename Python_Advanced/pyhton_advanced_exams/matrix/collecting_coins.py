import sys
from io import StringIO

test_input1 = '''5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right
'''

test_input2 = '''8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
down
up
left
'''


# sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)

def find_player(matrix):
    for rows in range(size):
        for cols in range(size):
            if matrix[rows][cols] == 'P':
                return rows, cols


def move_player(rows, cols, command, matrix):
    if command == 'up':
        if rows - 1 >= 0:
            rows -= 1
        else:
            rows = size - 1

    elif command == 'down':
        if rows + 1 < size:
            rows += 1
        else:
            rows = 0
    elif command == 'left':
        if cols - 1 >= 0:
            cols -= 1
        else:
            cols = size - 1
    elif command == 'right':
        if cols + 1 < size:
            cols += 1
        else:
            cols = 0

    return rows, cols


size = int(input())
matrix = [input().split() for _ in range(size)]
coordinates = list()
total_coins = 0
is_lost = False
row, col = find_player(matrix)
coordinates.append([row, col])
matrix[row][col] = 'p'
while True:
    commands = input()
    row, col = move_player(row, col, commands, matrix)
    coordinates.append([row, col])
    if matrix[row][col] == 'X':
        is_lost = True
        break
    elif not matrix[row][col].isalpha():
        total_coins += int(matrix[row][col])
        if total_coins >= 100:
            break
    matrix[row][col] = 'p'
if is_lost:
    print(f"Game over! You've collected {total_coins // 2} coins.")
else:
    print(f"You won! You've collected {total_coins} coins.")
print("Your path:")
[print(s) for s in coordinates]
