def move(row, col, end_row, end_col):
    if row == end_row and col == end_col:
        return 1
    if not (row <= end_row and col <= end_col):
        return 0
    counter = 0
    counter += move(row + 1, col, end_row, end_col)
    counter += move(row, col + 1, end_row, end_col)
    return counter


m = int(input())
n = int(input())
boards = [['-' for _ in range(m)] for _ in range(n)]
print(move(0, 0, m - 1, n - 1, ))