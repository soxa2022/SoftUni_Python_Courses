# n = int(input())
# matrix = [[int(s) for s in input().split()] for _ in range(n)]
# res = []
# for i in range(len(matrix)):
#     j = i
#     res.append(matrix[i][j])
# print(sum(res))


n = int(input())
matrix = [[int(s) for s in input().split()] for _ in range(n)]
res = 0
for i in range(len(matrix)):
    res += matrix[i][i]
print(res)