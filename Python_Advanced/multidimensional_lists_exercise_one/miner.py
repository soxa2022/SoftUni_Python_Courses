import sys
from io import StringIO
from collections import deque

test_input1 = '''5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *
'''
test_input2 = '''4
up right right right down
* * * e
* * c *
* s * c
* * * *
'''
test_input3 = '''6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *
'''

# sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)


# sys.stdin = StringIO(test_input3)


def find_start_pos(rows, field):
    for row in range(rows):
        for col in range(rows):
            if field[row][col] == 's':
                return row, col


def find_count_coals(rows, field):
    count_coals = 0
    for row in range(rows):
        for col in range(rows):
            if field[row][col] == 'c':
                count_coals += 1
    return count_coals


rows = int(input())
commands = input().split()
field = [[s for s in input().split()] for _ in range(rows)]

r, c = find_start_pos(rows, field)
total_count_coals = find_count_coals(rows, field)
coals = 0
is_over = False
for command in commands:
    if command == 'left':
        if c - 1 >= 0:
            c -= 1
    elif command == 'right':
        if c + 1 < rows:
            c += 1
    elif command == 'up':
        if r - 1 >= 0:
            r -= 1
    elif command == 'down':
        if r + 1 < rows:
            r += 1
    if field[r][c] == 'c':
        field[r][c] = '*'
        coals += 1
    if field[r][c] == 'e':
        is_over = True
        print(f"Game over! ({r}, {c})")
        break
if not is_over:
    if coals == total_count_coals:
        print(f"You collected all coal! ({r}, {c})")
    else:
        print(f"{total_count_coals - coals} pieces of coal left. ({r}, {c})")
