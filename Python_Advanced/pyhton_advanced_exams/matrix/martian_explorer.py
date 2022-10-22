import sys
from io import StringIO

test_input1 = '''- R - - - -
- - - - - R
- E - R - -
- W - - - -
- - - C - -
M - - - - -
down, right, down, right, down, left, left, left
'''
test_input2 = '''R - - - - -
- - C - - -
- - - - M -
- - W - - -
- E - W - R
- - - - - -
up, right, down, right, right, right
'''
test_input3 = '''R - - - - -
- - C - - -
- - - - M -
C - M - R M
- E - W - -
- - - - - -
right, right, up, left, left, left, left, left
'''

# sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)


def move(direct, rows, cols):
    if direct == 'up':
        if rows - 1 == -1:
            rows = 5
        else:
            rows -= 1
    elif direct == 'down':
        if rows + 1 == 6:
            rows = 0
        else:
            rows += 1
    elif direct == 'left':
        if cols - 1 == -1:
            cols = 5
        else:
            cols -= 1
    elif direct == 'right':
        if cols + 1 == 6:
            cols = 0
        else:
            cols += 1
    return rows, cols


def find_rover(field):
    for r in range(count_rows):
        for c in range(count_rows):
            if field[r][c] == 'E':
                return r, c


count_rows = 6
field = []
for _ in range(count_rows):
    field.append(input().split())

water, metal, concrete = 0, 0, 0
directions = list(input().split(', '))
row, col = find_rover(field)

for direction in directions:
    row, col = move(direction, row, col)
    if field[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break
    elif field[row][col] == "W":
        water += 1
        print(f"Water deposit found at ({row}, {col})")
    elif field[row][col] == "M":
        metal += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif field[row][col] == "C":
        concrete += 1
        print(f"Concrete deposit found at ({row}, {col})")

if all([metal, water, concrete]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
