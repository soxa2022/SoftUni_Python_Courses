import sys

rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]
sub_matrix = []
max_sum = - sys.maxsize
max_sub = []
for i in range(rows - 1):
    for j in range(cols - 1):
        sub_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
        if sum(sub_matrix) > max_sum:
            max_sub = sub_matrix.copy()
            max_sum = sum(sub_matrix)

print(max_sub[0], max_sub[1])
print(max_sub[2], max_sub[3])
print(max_sum)