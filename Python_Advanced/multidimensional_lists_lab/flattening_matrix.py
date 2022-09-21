# rows = int(input())
# matrix = []
# for _ in range(rows):
#     numbers = [int(s) for s in input().split(', ')]
#     matrix.extend(numbers)
#
# print(matrix)

rows = int(input())


numbers = [[int(s) for s in input().split(', ')] for _ in range(rows)]
matrix = [num for row in numbers for num in row]


print(matrix)

