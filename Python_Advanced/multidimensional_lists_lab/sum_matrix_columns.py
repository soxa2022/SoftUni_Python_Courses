rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

# for _ in range(rows):
#     nums = [int(el) for el in input().split()]
#     matrix.append(nums)

for j in range(cols):
    res = 0
    for i in range(rows):
        res += matrix[i][j]
    print(res)