def get_symbol_pos(matrix, symbol):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if symbol == matrix[i][j]:
                return i, j
    return f"{symbol} does not occur in the matrix"


n = int(input())
char_matrix = [[ch for ch in input()] for _ in range(n)]
char = input()
print(get_symbol_pos(char_matrix, char))


# def get_symbol_pos(matrix, symbol):
#     pos = None
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if symbol == matrix[i][j]:
#                 pos = (i, j)
#                 break
#         if pos:
#             break
#     return pos
#
#
# n = int(input())
# char_matrix = [[ch for ch in input()] for _ in range(n)]
# char = input()
# position = get_symbol_pos(char_matrix, char)
# if position:
#     print(position)
# else:
#     print(f"{char} does not occur in the matrix")
