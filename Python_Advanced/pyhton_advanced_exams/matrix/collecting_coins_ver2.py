SIZE = int(input())
directions = {"left": (0, -1),
              "right": (0, 1),
              "up": (-1, 0),
              "down": (1, 0)
              }
field = []
player_position = []
collect_coins = 0
path_pos = []
for row in range(SIZE):
    line = [int(x) if not x.isalpha() else x for x in input().split()]

    if 'P' in line:
        col = line.index('P')
        player_position = [row, col]

    field.append(line)

row, col = player_position
path_pos.append([row, col])
field[row][col] = 0
while True:
    direction = input()

    if direction in directions:
        row += directions[direction][0]
        if row >= SIZE:
            row = 0
        if row < 0:
            row = SIZE - 1
        col += directions[direction][1]
        if col >= SIZE:
            col = 0
        if col < 0:
            col = SIZE - 1
        path_pos.append([row, col])
        if field[row][col] == "X":
            collect_coins /= 2
            print(f"Game over! You've collected {int(collect_coins)} coins.")
            break
        else:
            collect_coins += field[row][col]
            field[row][col] = 0
            if collect_coins >= 100:
                print(f"You won! You've collected {int(collect_coins)} coins.")
                break
print("Your path:")
[print(el) for el in path_pos]