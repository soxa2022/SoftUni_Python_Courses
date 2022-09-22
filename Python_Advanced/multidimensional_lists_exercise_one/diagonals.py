def primary_diagonal(matrix):
    primary_nums = []
    for i in range(len(matrix)):
        primary_nums.append(matrix[i][i])
    return primary_nums


def secondary_diagonal(matrix):
    secondary_nums = []
    for i in range(len(matrix)):
        secondary_nums.append(matrix[i][len(matrix) - i - 1])
    return secondary_nums


rows = int(input())
matrix_nums = [[int(s) for s in input().split(", ")] for _ in range(rows)]
print(
    f'Primary diagonal: {(", ".join([str(s) for s in (primary_diagonal(matrix_nums))]))}. Sum: {sum(primary_diagonal(matrix_nums))}')
print(
    f'Secondary diagonal: {(", ".join([str(s) for s in (secondary_diagonal(matrix_nums))]))}. Sum: {sum(secondary_diagonal(matrix_nums))}')
