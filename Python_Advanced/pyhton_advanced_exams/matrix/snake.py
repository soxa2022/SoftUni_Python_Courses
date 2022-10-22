directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1)
              }
field = []
snake_pos = []
burrows_pos = []
eaten_food = 0
size = int(input())
for rows in range(size):
    line = list(input())
    if 'S' in line:
        snake_pos.extend([rows, line.index("S")])
    if 'B' in line:
        burrows_pos.append([rows, line.index("B")])
    field.append(line)

row, col = snake_pos
while eaten_food < 10:

    field[row][col] = '.'
    command = input()
    row += directions[command][0]
    col += directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        print("Game over!")
        break
    if field[row][col] == '*':
        eaten_food += 1
    if field[row][col] == 'B':
        field[row][col] = '.'
        burrows_pos.remove([row, col])
        row = burrows_pos[0][0]
        col = burrows_pos[0][1]
    field[row][col] = "S"
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {eaten_food}")
[print(''.join(x)) for x in field]
