total_sum = 0
rows, cols = [int(s) for s in input().split(", ")]
# matrix = []
# for _ in range(rows):
#     matrix.append([int(s) for s in input().split(", ")])
matrix = [[int(s) for s in input().split(', ')] for _ in range(rows)]
for row in range(rows):
    # total_sum += sum(matrix[row])
    for col in range(cols):
        total_sum += matrix[row][col]
print(total_sum)
print(matrix)