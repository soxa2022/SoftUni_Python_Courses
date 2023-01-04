def dfs(key, row, col, matrix, visited):
    if not (0 <= row < len(matrix) and 0 <= col < len(matrix[row])):
        return 0
    if visited[row][col]:
        return 0
    if matrix[row][col] != key:
        return 0

    visited[row][col] = True

    dfs(key, row + 1, col, matrix, visited, )
    dfs(key, row - 1, col, matrix, visited, )
    dfs(key, row, col + 1, matrix, visited, )
    dfs(key, row, col - 1, matrix, visited, )
    return 1


rows = int(input())
cols = int(input())
matrix = []
visited = []
areas = {}
total_areas = 0
for row in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)
for row in range(rows):
    for col in range(cols):
        key = matrix[row][col]
        result = dfs(key, row, col, matrix, visited)
        if key not in areas:
            areas[key] = 0
        areas[key] += result
        total_areas += result

# print(f"Areas: {sum(areas.values())}")
print(f"Areas: {total_areas}")
for letter, count in sorted(areas.items()):
    print(f"Letter '{letter}' -> {count}")
