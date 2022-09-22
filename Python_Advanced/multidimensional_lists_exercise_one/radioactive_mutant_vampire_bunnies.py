import sys
from io import StringIO

test_input1 = '''5 6
.....P
......
...B..
......
......
ULDDDR
'''
test_input2 = '''4 5
.....
.....
.B...
...P.
LLLLLLLL
'''
test_input3 = '''5 8
.......B
...B....
....B..B
........
..P.....
ULLL
'''

# sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)


# sys.stdin = StringIO(test_input3)

def find_player_pos():
    for row in range(rows):
        for col in range(cols):
            if lair[row][col] == 'P':
                return row, col
    return


def spread_bunnies():
    coordinates = []
    for row in range(rows):
        for col in range(cols):
            if lair[row][col] == 'B':
                coordinates.append([row, col])
    for r, c in coordinates:
        if r + 1 < rows:
            lair[r + 1][c] = 'B'
        if r - 1 >= 0:
            lair[r - 1][c] = 'B'
        if c - 1 >= 0:
            lair[r][c - 1] = 'B'
        if c + 1 < cols:
            lair[r][c + 1] = 'B'


rows, cols = [int(el) for el in input().split()]
lair = [[s for s in input()] for _ in range(rows)]
commands = list(input())
row_player, col_player = find_player_pos()
is_won = False
is_died = False
for command in commands:
    n = row_player
    m = col_player
    lair[row_player][col_player] = '.'
    if command == "L":
        col_player -= 1
    elif command == "U":
        row_player -= 1
    elif command == "D":
        row_player += 1
    elif command == "R":
        col_player += 1
    if col_player >= cols or col_player < 0 or row_player < 0 or row_player >= rows:
        row_player = n
        col_player = m
        is_won = True
        spread_bunnies()
        break
    if lair[row_player][col_player] == 'B':
        is_died = True
        spread_bunnies()
        break

    lair[row_player][col_player] = 'P'
    spread_bunnies()
    if not find_player_pos():
        is_died = True
        break

if is_won:
    [print(''.join(el)) for el in lair]
    print(f"won: {row_player} {col_player}")
if is_died:
    [print(''.join(el)) for el in lair]
    print(f"dead: {row_player} {col_player}")
