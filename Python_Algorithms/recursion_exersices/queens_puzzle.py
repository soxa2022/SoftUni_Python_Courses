def can_place_queen(row, col, board, rows, cols, left_diagonal, right_diagonal):
    if row in rows:
        return False
    if col in cols:
        return False
    if (col - row) in left_diagonal:
        return False
    if (col + row) in right_diagonal:
        return False
    return True


def set_queen(row, col, board, rows, cols, left_diagonal, right_diagonal):
    board[row][col] = "*"
    rows.add(row)
    cols.add(col)
    left_diagonal.add(col - row)
    right_diagonal.add(col + row)


def remove_queen(row, col, board, rows, cols, left_diagonal, right_diagonal):
    board[row][col] = "-"
    rows.discard(row)
    cols.discard(col)
    left_diagonal.discard(col - row)
    right_diagonal.discard(col + row)


def queens_solution(row, col, board, rows, cols, left_diagonal, right_diagonal):
    if row == 8:
        [print(*x) for x in board]
        print()
        return

    for col in range(n):
        if can_place_queen(row, col, board, rows, cols, left_diagonal, right_diagonal):
            set_queen(row, col, board, rows, cols, left_diagonal, right_diagonal)
            queens_solution(row + 1, col, board, rows, cols, left_diagonal, right_diagonal)
            remove_queen(row, col, board, rows, cols, left_diagonal, right_diagonal)


n = 8
boards = [["-" for _ in range(n)] for _ in range(n)]

queens_solution(0, 0, boards, set(), set(), set(), set())