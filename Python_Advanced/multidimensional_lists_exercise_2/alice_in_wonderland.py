import sys
from io import StringIO

test_input1 = '''5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
'''
test_input2 = '''7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right
'''


# sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)


def alice_pos(field):
    for row in range(rows):
        for col in range(rows):
            if field[row][col] == "A":
                return row, col


def alice_path(field):
    tea_bags = 0
    alice_row, alice_col = alice_pos(field)
    field[alice_row][alice_col] = '*'
    while tea_bags < 10:
        command = input()
        if command == 'left':
            alice_col -= 1
            if alice_col < 0:
                break
            if field[alice_row][alice_col] == 'R':
                field[alice_row][alice_col] = '*'
                break
            if field[alice_row][alice_col].isdigit():
                tea_bags += int(field[alice_row][alice_col])
            field[alice_row][alice_col] = '*'
        elif command == 'right':
            alice_col += 1
            if alice_col == rows:
                break
            if field[alice_row][alice_col] == 'R':
                field[alice_row][alice_col] = '*'
                break
            if field[alice_row][alice_col].isdigit():
                tea_bags += int(field[alice_row][alice_col])
            field[alice_row][alice_col] = '*'
        elif command == 'up':
            alice_row -= 1
            if alice_row < 0:
                break
            if field[alice_row][alice_col] == 'R':
                field[alice_row][alice_col] = '*'
                break
            if field[alice_row][alice_col].isdigit():
                tea_bags += int(field[alice_row][alice_col])
            field[alice_row][alice_col] = '*'
        elif command == 'down':
            alice_row += 1
            if alice_row == rows:
                break
            if field[alice_row][alice_col] == 'R':
                field[alice_row][alice_col] = '*'
                break
            if field[alice_row][alice_col].isdigit():
                tea_bags += int(field[alice_row][alice_col])
            field[alice_row][alice_col] = '*'
    if tea_bags >= 10:
        return "She did it! She went to the party."
    return "Alice didn't make it to the tea party."


rows = int(input())
field = []
for _ in range(rows):
    nums = list(input().split())
    field.append(nums)
print(alice_path(field))
[print(*el) for el in field]
