size = int(input())
count_bombs = int(input())
directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (1, 1),
    (-1, 1),
    (1, -1)
)
field = [[0 for s in range(size)] for _ in range(size)]

for _ in range(count_bombs):
    coordinates = input()
    row, col = map(int, coordinates.strip(')').strip("(").split(', '))
    field[row][col] = '*'

    for direction in directions:
        rows = direction[0] + row
        cols = direction[1] + col
        if 0 <= rows < size and 0 <= cols < size:
            if not field[rows][cols] == '*':
                field[rows][cols] += 1

[print(*el) for el in field]
