import sys
from io import StringIO

test_input1 = '''5 
0K0K0
K000K
00K00
K000K
0K0K0
'''
test_input2 = '''2
KK
KK
'''
test_input3 = '''8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK
'''


# sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)


# sys.stdin = StringIO(test_input3)


def find_knights_pos(board):
    max_knight_pos = []
    max_count = 0
    for row in range(rows):
        for col in range(rows):
            count_k = 0
            if board[row][col] == 'K':
                if row + 2 < rows and col + 1 < rows:
                    if board[row + 2][col + 1] == "K":
                        count_k += 1
                if row + 2 < rows and col - 1 >= 0:
                    if board[row + 2][col - 1] == "K":
                        count_k += 1
                if row - 2 >= 0 and col - 1 >= 0:
                    if board[row - 2][col - 1] == "K":
                        count_k += 1
                if row - 2 >= 0 and col + 1 < rows:
                    if board[row - 2][col + 1] == "K":
                        count_k += 1
                if row + 1 < rows and col + 2 < rows:
                    if board[row + 1][col + 2] == "K":
                        count_k += 1
                if row + 1 < rows and col - 2 >= 0:
                    if board[row + 1][col - 2] == "K":
                        count_k += 1
                if row - 1 >= 0 and col - 2 >= 0:
                    if board[row - 1][col - 2] == "K":
                        count_k += 1
                if row - 1 >= 0 and col + 2 < rows:
                    if board[row - 1][col + 2] == "K":
                        count_k += 1
                if count_k > max_count:
                    max_count = count_k
                    if not max_count == 0:
                        max_knight_pos = [row, col]

    return max_knight_pos


def remove_knight(board):
    removed_knight = 0
    while True:
        knight_count = find_knights_pos(board)
        if not knight_count:
            break
        max_row, max_col = knight_count
        board[max_row][max_col] = '0'
        removed_knight += 1
    return removed_knight


rows = int(input())
board = [[s for s in input()] for _ in range(rows)]
print(remove_knight(board))

# size = int(input())
# matrix = [list(input()) for _ in range(size)]
# positions = (
#     (-2, 1),
#     (-2, -1),
#     (-1,-2),
#     (-1, 2),
#     (2, 1),
#     (2, -1),
#     (1, 2),
#     (1, -2)
# )
#
# removed_knights = 0
#
# while True:
#     max_attacks = 0
#     knight_with_most_attacks_pos = []
#
#     for row in range(size):
#         for col in range(size):
#             if matrix[row][col] == 'K':
#                 attacks = 0
#
#                 for pos in positions:
#                     pos_row = row + pos[0]
#                     pos_col = col + pos[1]
#
#                     if 0 <= pos_row < size and 0 <= pos_col < size:
#                      if matrix[pos_row][pos_col] == 'K':
#                         attacks += 1
#
#                 if attacks > max_attacks:
#                     knight_with_most_attacks_pos = [row, col]
#                     max_attacks = attacks
#     if knight_with_most_attacks_pos:
#         matrix[knight_with_most_attacks_pos[0]][knight_with_most_attacks_pos[1]] = '0'
#         removed_knights += 1
#     else:
#         break
#
# print(removed_knights)