import sys
from io import StringIO

test_input1 = '''3
11 2 4
4 5 6
10 8 -12
'''
test_input2 = '''4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14
'''

# sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)


def primary_diagonal(matrix):
    primary_nums = []
    for n in range(len(matrix)):
        primary_nums.append(matrix[n][n])
    return primary_nums


def secondary_diagonal(matrix):
    secondary_nums = []
    for n in range(len(matrix)):
        secondary_nums.append(matrix[n][len(matrix) - n - 1])
    return secondary_nums


def difference(matrix):
    sum_primary = sum(primary_diagonal(matrix))
    sum_secondary = sum(secondary_diagonal(matrix))
    return abs(sum_primary - sum_secondary)


rows = int(input())
matrix_nums = [[int(s) for s in input().split()] for _ in range(rows)]
print(difference(matrix_nums))
