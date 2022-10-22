main_string = input()
SIZE = int(input())

directions = {'left': (0, -1),
              'right': (0, 1),
              'down': (1, 0),
              'up': (-1, 0)
              }

field = []
player_pos = []

for rows in range(SIZE):
    line = list(input())

    if 'P' in line:
        cols = line.index('P')
        player_pos = [rows, cols]

    field.append(line)

commands_count = int(input())
for _ in range(commands_count):
    direction = input()

    if 0 <= player_pos[0] + directions[direction][0] < SIZE and 0 <= player_pos[1] + directions[direction][1] < SIZE:
        field[player_pos[0]][player_pos[1]] = '-'
        row = player_pos[0] + directions[direction][0]
        col = player_pos[1] + directions[direction][1]

        if not field[row][col] == '-':
            main_string = main_string + field[row][col]

        field[row][col] = 'P'
        player_pos = [row, col]
    else:
        main_string = main_string[:-1]

print(main_string)
[print(''.join(x)) for x in field]
