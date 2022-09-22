import sys
from io import StringIO

test_input2 = '''2 2
a b
c d
'''
test_input1 = '''3 4
A B B D
E B B B
I J B B
'''

test_input3 = '''5 4
A A B D
A A B B
I J B B
C C C G
C C K P
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def count_matrices(matrix):
    counter = 0
    for n in range(len(matrix) - 1):
        for m in range(len(matrix[n]) - 1):
            sub_matrix = [matrix[n][m], matrix[n][m + 1], matrix[n + 1][m], matrix[n + 1][m + 1]]
            if len(set(sub_matrix)) == 1:
                counter += 1
    return counter


count_rows, count_cols = [int(s) for s in input().split()]
# matrix_chars = []
# for _ in range(count_rows):
#     matrix_chars.append([s for s in input().split()])
matrix_chars = [[s for s in input().split()] for _ in range(count_rows)]
print(count_matrices(matrix_chars))
