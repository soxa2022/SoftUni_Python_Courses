def santa_pos(matrix):
    count = 0
    new_row = 0
    new_col = 0
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "S":
                new_row = row
                new_col = col
            elif matrix[row][col] == 'V':
                count += 1
    return new_row, new_col, count


def move_func(command):
    new_row, new_col, _ = santa_pos(matrix)
    if command == 'up':
        matrix[new_row][new_col] = '-'
        new_row -= 1
    elif command == 'left':
        matrix[new_row][new_col] = '-'
        new_col -= 1
    elif command == 'down':
        matrix[new_row][new_col] = '-'
        new_row += 1
    elif command == 'right':
        matrix[new_row][new_col] = '-'
        new_col += 1

    return new_row, new_col


def delivery(matrix, command, presents):
    row, col = move_func(command)
    if matrix[row][col] == 'V':
        presents -= 1
        matrix[row][col] = 'S'
    elif matrix[row][col] == 'C':
        if not matrix[row + 1][col] == '-' and presents:
            presents -= 1
            matrix[row + 1][col] = '-'
        if not matrix[row - 1][col] == '-' and presents:
            presents -= 1
            matrix[row - 1][col] = '-'
        if not matrix[row][col + 1] == '-' and presents:
            presents -= 1
            matrix[row][col + 1] = '-'
        if not matrix[row][col - 1] == '-' and presents:
            presents -= 1
            matrix[row][col - 1] = '-'
        matrix[row][col] = "S"
    else:
        matrix[row][col] = "S"
    return presents


number_presents = int(input())
size = int(input())
matrix = [[el for el in input().split()] for _ in range(size)]
*_, count_nice_kids = santa_pos(matrix)
while number_presents > 0:
    commands = input()
    if commands == "Christmas morning":
        break
    number_presents = delivery(matrix, commands, number_presents)
    *_, count_kids = santa_pos(matrix)
    if not count_kids:
        break
*_, kids_without_presents = santa_pos(matrix)
if not number_presents and kids_without_presents:
    print("Santa ran out of presents!")
[print(*el) for el in matrix]
if not kids_without_presents:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {kids_without_presents} nice kid/s.")


def eat_cookie(present_left, nice_kids):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighborhood[r][c].isalpha():
            if neighborhood[r][c] == 'V':
                nice_kids += 1

            neighborhood[r][c] = '-'
            present_left -= 1

        if not present_left:
            break

    return present_left, nice_kids


# present = int(input())
# size = int(input())
# neighborhood = []
# santa_pos = []
# total_nice_kids = 0
# nice_kids_visited = 0
#
# directions = {
#     'up': (-1, 0),
#     'down': (1, 0),
#     'left': (0, -1),
#     'right': (0, 1)
# }
#
# for row in range(size):
#     line = input().split()
#
#     neighborhood.append(line)
#
#     if 'S' in line:
#         santa_pos = [row, line.index('S')]
#         neighborhood[row][santa_pos[1]] = '-'
#
#     total_nice_kids += line.count('V')
#
# command = input()
#
# while True:
#     if command == 'Christmas morning':
#         break
#
#     santa_pos = [
#         santa_pos[0] + directions[command][0],
#         santa_pos[1] + directions[command][1],
#     ]
#
#     house = neighborhood[santa_pos[0]][santa_pos[1]]
#
#     if house == 'V':
#         nice_kids_visited += 1
#         present -= 1
#
#     elif house == 'C':
#         present, nice_kids_visited = eat_cookie(present,nice_kids_visited)
#
#     neighborhood[santa_pos[0]][santa_pos[1]] = '-'
#
#     if not present or nice_kids_visited == total_nice_kids:
#         break
#
#     command = input()
#
# neighborhood[santa_pos[0]][santa_pos[1]] = 'S'
#
# if not present and nice_kids_visited < total_nice_kids:
#     print('Santa ran out presents!')
#
# print(*[' '.join(row) for row in neighborhood], sep="\n")
#
# if nice_kids_visited == total_nice_kids:
#     print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')
# else:
#     print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')