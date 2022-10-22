import string

SIZE = 8
white_pos = []
black_pos = []
board = []
turn = ['w', 'b']
digit_side = ['8', '7', '6', '5', '4', '3', '2', '1']
winners = {'w': "White", "b": "Black"}
moves = [-1, 1]
positions = []

for rows in range(SIZE):
    line = input().split()

    if 'b' in line:
        black_pos = [rows, (line.index('b'))]
    if 'w' in line:
        white_pos = [rows, (line.index('w'))]

    board.append(line)

positions.append(white_pos)
positions.append(black_pos)

while True:

    row, col = positions[0]

    if col + 1 < SIZE and 0 <= row + moves[0] < SIZE:
        if board[row + moves[0]][col + 1] == turn[1]:
            board[row + moves[0]][col + 1] = turn[0]
            print(
                f"Game over! {winners[turn[0]]} win, capture on {string.ascii_lowercase[col + 1] + digit_side[row + moves[0]]}.")
            break

    if col - 1 >= 0 and 0 <= row + moves[0] < SIZE:
        if board[row + moves[0]][col - 1] == turn[1]:
            board[row + moves[0]][col - 1] = turn[0]
            print(
                f"Game over! {winners[turn[0]]} win, capture on {string.ascii_lowercase[col - 1] + digit_side[row + moves[0]]}.")
            break

    if row + moves[0] == 0 or row + moves[0] == SIZE - 1:
        print(
            f"Game over! {winners[turn[0]]} pawn is promoted to a queen at {string.ascii_lowercase[col] + digit_side[row + moves[0]]}.")
        break

    board[row][col] = '-'
    board[row + moves[0]][col] = turn[0]
    positions[0][0] += moves[0]
    turn.append(turn.pop(0))
    moves.append(moves.pop(0))
    positions.append(positions.pop(0))
