main_string = input()
size = int(input())
field = []
player_pos = ()
commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    line = list(input())
    if 'P' in line:
        player_pos = [row, line.index("P")]
    field.append(line)

m = int(input())
field[player_pos[0]][player_pos[1]] = "-"
for _ in range(m):
    command = input()
    rows, cols = player_pos
    if not (0 <= rows + commands[command][0] < size and 0 <= cols + commands[command][1] < size):
        main_string = main_string[:-1]
        continue
    else:
        rows += commands[command][0]
        cols += commands[command][1]
        if field[rows][cols].isalpha():
            main_string += field[rows][cols]
            field[rows][cols] = '-'
        player_pos = [rows, cols]
field[player_pos[0]][player_pos[1]] = "P"
print(main_string)
print(*[''.join(s) for s in field], sep='\n')
