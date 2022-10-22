import string


def find_paws(board):
    pos_white = ''
    pos_black = ''
    for rows in range(count_rows_cols):
        for cols in range(count_rows_cols):
            if board[rows][cols] == 'w':
                pos_white = rows, cols
            if board[rows][cols] == 'b':
                pos_black = rows, cols
    return pos_white, pos_black


def game(board):
    digit_side = [8, 7, 6, 5, 4, 3, 2, 1]
    white_pos, black_pos = find_paws(board)
    w_rows, w_cols = white_pos
    b_rows, b_cols = black_pos
    while True:
        if w_rows - 1 >= 0 and w_cols - 1 >= 0:
            if board[w_rows - 1][w_cols - 1] == 'b':
                return f"Game over! White win, capture on {string.ascii_lowercase[w_cols - 1]}{digit_side[w_rows - 1]}."
        if w_rows - 1 >= 0 and w_cols + 1 < 8:
            if board[w_rows - 1][w_cols + 1] == 'b':
                return f"Game over! White win, capture on {string.ascii_lowercase[w_cols + 1]}{digit_side[w_rows - 1]}."
        board[w_rows][w_cols] = '-'
        w_rows -= 1
        board[w_rows][w_cols] = 'w'
        if w_rows == 0:
            return f"Game over! White pawn is promoted to a queen at {string.ascii_lowercase[w_cols]}{digit_side[w_rows]}."
        if b_rows + 1 < 8 and b_cols - 1 >= 0:
            if board[b_rows + 1][b_cols - 1] == 'w':
                return f"Game over! Black win, capture on {string.ascii_lowercase[b_cols - 1]}{digit_side[b_rows + 1]}."
        if b_rows + 1 < 8 and b_cols + 1 < 8:
            if board[b_rows + 1][b_cols + 1] == 'w':
                return f"Game over! Black win, capture on {string.ascii_lowercase[b_cols + 1]}{digit_side[b_rows + 1]}."
        board[b_rows][b_cols] = '-'
        b_rows += 1
        board[b_rows][b_cols] = 'b'
        if b_rows == 7:
            return f"Game over! Black pawn is promoted to a queen at {string.ascii_lowercase[b_cols]}{digit_side[b_rows]}."


count_rows_cols = 8
board = [[x for x in input().split()] for _ in range(count_rows_cols)]
print(game(board))
