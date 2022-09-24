import sys
from io import StringIO

test_input1 = '''5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
'''
test_input2 = '''8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22
'''

# sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)


def bunny_pos(field):
    for row in range(rows):
        for col in range(rows):
            if field[row][col] == "B":
                return row, col


def best_path(field):
    egg_collection = {"up": {'eggs': 0, 'pos': []}, "down": {'eggs': 0, 'pos': []}, "left": {'eggs': 0, 'pos': []},
                      "right": {'eggs': 0, 'pos': []}}

    row, col = bunny_pos(field)
    # down
    for i in range(row + 1, rows):
        if field[i][col] == 'X':
            break
        egg_collection['down']['eggs'] += int(field[i][col])
        egg_collection['down']['pos'].append([i, col])
    # right
    for i in range(col + 1, rows):
        if field[row][i] == 'X':
            break
        egg_collection['right']['eggs'] += int(field[row][i])
        egg_collection['right']['pos'].append([row, i])
    # up
    for i in range(row - 1, -1, -1):
        if field[i][col] == 'X':
            break
        egg_collection['up']['eggs'] += int(field[i][col])
        egg_collection['up']['pos'].append([i, col])
    # left
    for i in range(col - 1, -1, -1):
        if field[row][i] == 'X':
            break
        egg_collection['left']['eggs'] += int(field[row][i])
        egg_collection['left']['pos'].append([row, i])

    return egg_collection


def printing_data():
    max_eggs_direction = ''
    max_eggs = -sys.maxsize
    best_path_coordinates = []
    egg_collection = best_path(field)
    for item in egg_collection:
        if egg_collection[item]['eggs'] > max_eggs and egg_collection[item]['pos']:
            max_eggs = egg_collection[item]['eggs']
            max_eggs_direction = item
            best_path_coordinates = egg_collection[item]['pos']
    print(max_eggs_direction)
    [print(x) for x in best_path_coordinates]
    print(max_eggs)


rows = int(input())
field = []
for _ in range(rows):
    nums = list(input().split())
    field.append(nums)

printing_data()
