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
for rows in range(SIZE):
    line = [int(x) if not x.isalpha() else x for x in input().split()]

    if 'P' in line:
        cols = line.index('P')
        player_position = [rows, cols]

    field.append(line)
path_pos.append([player_position[0], player_position[1]])

while True:

    field[player_position[0]][player_position[1]] = 0
    direction = input()

    if direction in directions:
        player_position[0] += directions[direction][0]
        player_position[1] += directions[direction][1]

        for i in range(len(player_position)):
            if player_position[i] == SIZE:
                player_position[i] = 0
            if player_position[i] < 0:
                player_position[i] = SIZE - 1

        path_pos.append([player_position[0], player_position[1]])
        if field[player_position[0]][player_position[1]] == "X":
            collect_coins /= 2
            print(f"Game over! You've collected {int(collect_coins)} coins.")
            break
        else:
            collect_coins += field[player_position[0]][player_position[1]]
            if collect_coins >= 100:
                print(f"You won! You've collected {int(collect_coins)} coins.")
                break
print("Your path:")
[print(el) for el in path_pos]
