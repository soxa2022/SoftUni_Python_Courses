class Store:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def find_area(row, col, matrix):
    if not (0 <= row < len(matrix) and 0 <= col < len(matrix[row])):
        return 0
    if not matrix[row][col] == "-":
        return 0

    matrix[row][col] = "v"
    result = 1
    result += find_area(row + 1, col, matrix, )
    result += find_area(row - 1, col, matrix, )
    result += find_area(row, col + 1, matrix, )
    result += find_area(row, col - 1, matrix, )
    return result


def find_size(matrix, area):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            size = find_area(row, col, matrix)
            if size > 0:
                area.append(Store(row, col, size))
    return area


n = int(input())
m = int(input())
mat = [[x for x in input()] for _ in range(n)]
areas = (find_size(mat, []))
# sorted_areas = dict(sorted(areas.items(), key=lambda x: (-x[1], x[0][0], x[0][1])))
# print(f"Total areas found: {len(sorted_areas)}")
# n = 1
# for key, value in sorted_areas.items():
#     print(f"Area #{n} at {key}, size: {value}")
#     n += 1
print(f"Total areas found: {len(areas)}")
sorted_areas = sorted(areas, key=lambda x: (-x.size, x.row, x.col))
# sorted_areas = sorted(areas, key=lambda x: (-x.size,))
# for idx, area in enumerate(sorted_areas):
#     print(f"Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}")

for i in range(len(sorted_areas)):
    print(f"Area #{i + 1} at ({sorted_areas[i].row}, {sorted_areas[i].col}), size: {sorted_areas[i].size}")
