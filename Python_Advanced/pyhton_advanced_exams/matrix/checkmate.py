size = 8
board = []
king_pos = tuple()
queens_pos = []
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
for rows in range(size):
    line = input().split()
    if 'K' in line:
        king_pos = (rows, line.index('K'))
    board.append(line)
for direction in directions:
    row, col = king_pos
    for _ in range(size):
        row += direction[0]
        col += direction[1]
        if 0 <= row < size and 0 <= col < size:
            if board[row][col] == "Q":
                queens_pos.append([row, col])
                break
        else:
            break
if queens_pos:
    print(*queens_pos, sep='\n')
else:
    print("The king is safe!")
