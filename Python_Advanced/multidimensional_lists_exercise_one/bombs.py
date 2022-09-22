import sys
from io import StringIO
from collections import deque

test_input1 = '''4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0
'''
test_input2 = '''3
7 8 4
3 1 5
6 4 9
0,2 1,0 2,2
'''


# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def bombs(rows, matrix, coordinates):
    for i in range(len(coordinates)):
        r, c = coordinates[i]
        if matrix[r][c] > 0:
            if r - 1 >= 0:
                if matrix[r - 1][c] > 0:
                    matrix[r - 1][c] -= matrix[r][c]
                if c - 1 >= 0:
                    if matrix[r - 1][c - 1] > 0:
                        matrix[r - 1][c - 1] -= matrix[r][c]
                if c + 1 < rows:
                    if matrix[r - 1][c + 1] > 0:
                        matrix[r - 1][c + 1] -= matrix[r][c]
            if r + 1 < rows:
                if matrix[r + 1][c] > 0:
                    matrix[r + 1][c] -= matrix[r][c]
                if c - 1 >= 0:
                    if matrix[r + 1][c - 1] > 0:
                        matrix[r + 1][c - 1] -= matrix[r][c]
                if c + 1 < rows:
                    if matrix[r + 1][c + 1] > 0:
                        matrix[r + 1][c + 1] -= matrix[r][c]
            if c - 1 >= 0:
                if matrix[r][c - 1] > 0:
                    matrix[r][c - 1] -= matrix[r][c]
            if c + 1 < rows:
                if matrix[r][c + 1] > 0:
                    matrix[r][c + 1] -= matrix[r][c]
            matrix[r][c] = 0
    return matrix


rows = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(rows)]
# coordinates = [list(map(int, s.split(','))) for s in input().split()]
coordinates = [[int(x) for x in s.split(',')] for s in input().split()]
print(f"Alive cells: {len([x for row in bombs(rows, matrix, coordinates) for x in row if x > 0])}")
print(f"Sum: {sum([x for row in bombs(rows, matrix, coordinates) for x in row if x > 0])}")
[print(*el) for el in bombs(rows, matrix, coordinates)]
