import sys
from io import StringIO

test_input1 = '''4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
'''
test_input2 = '''5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5
'''

# sys.stdin = StringIO(test_input1)


# sys.stdin = StringIO(test_input2)

rows, cols = [int(s) for s in input().split()]
# matrix_nums = []
# for _ in range(rows):
#     matrix_nums.append([int(el) for el in input().split()])
matrix = [[int(el) for el in input().split()] for _ in range(rows)]
max_sum = - sys.maxsize
max_sub = []
sub_matrix = []

for i in range(rows - 2):
    for j in range(cols - 2):
        sub_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i][j + 2], matrix[i + 1][j], matrix[i + 1][j + 1],
                      matrix[i + 1][j + 2], matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]
                      ]
        if sum(sub_matrix) > max_sum:
            max_sub = sub_matrix.copy()
            max_sum = sum(sub_matrix)
print(f'Sum = {max_sum}')
print(max_sub[0], max_sub[1], max_sub[2])
print(max_sub[3], max_sub[4], max_sub[5])
print(max_sub[6], max_sub[7], max_sub[8])