import sys
from io import StringIO

test_input1 = '''. . . . . .
. 6 . . . .
G . S . t S
. . 10 . . .
. 95 . . 8 .
. . P . . .
(1, 1)
Create, down, r
Update, right, e
Create, right, a
Read, right
Delete, right
Stop'''
test_input2 = '''. . . . . .
. 6 . . . .  
. T . D . O  
. . 10 A . .  
. 95 . 80 5 .  
. . P . t .   
(2, 3)
Create, down, o
Delete, right
Read, up
Create, left, 20
Update, up, P
Stop'''
test_input3 = '''. 6 . . . .
. T . D . O
. . 10 A . .
. 95 . 80 5 .
. . P . t .
(2, 3)
Create, down, o
Delete, right
Read, up
Create, left, 20
Update, up, P
Stop
'''

sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def move(direct, rows, cols):
    if direct == 'up':
        rows -= 1
    elif direct == 'down':
        rows += 1
    elif direct == 'left':
        cols -= 1
    elif direct == 'right':
        cols += 1
    return rows, cols


def create(direction, rows, cols, value):
    rows, cols = move(direction, rows, cols)
    if field[rows][cols] == '.':
        field[rows][cols] = value
    return rows, cols


def update(direction, rows, cols, value):
    rows, cols = move(direction, rows, cols)
    if not field[rows][cols] == '.':
        field[rows][cols] = value
    return rows, cols


def delete(direction, rows, cols):
    rows, cols = move(direction, rows, cols)
    if not field[rows][cols] == '.':
        field[rows][cols] = '.'
    return rows, cols


def read(direction, rows, cols):
    rows, cols = move(direction, rows, cols)
    if not field[rows][cols] == '.':
        print(field[rows][cols])
    return rows, cols


def crud(field, row, col):
    while True:
        command = input().split(', ')
        if command[0] == "Stop":
            break
        action = command[0]
        directions = command[1]
        if action == "Create":
            values = command[2]
            row, col = create(directions, row, col, values)
        elif action == 'Update':
            values = command[2]
            row, col = update(directions, row, col, values)
        elif action == 'Delete':
            row, col = delete(directions, row, col)
        elif action == 'Read':
            row, col = read(directions, row, col)
    return field


number_rows_cols = 6
field = [[s for s in input().split()] for _ in range(number_rows_cols)]
r, c = [int(s) for s in input() if s.isdigit()]
# [print(' '.join(el)) for el in crud(field, r, c)]
[print(*el) for el in crud(field, r, c)]

