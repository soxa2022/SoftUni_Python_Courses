def modification(matrix):
    while True:
        commands = input().split()
        if commands[0] == "END":
            break
        command = commands[0]
        row, col, value = [int(x) for x in commands[1:]]
        if 0 <= row < rows and 0 <= col < rows:
            if command == "Subtract":
                matrix[row][col] -= value
            elif command == "Add":
                matrix[row][col] += value
        else:
            print("Invalid coordinates")
    return matrix


rows = int(input())
matrix_mod = [[int(el) for el in input().split()] for _ in range(rows)]
# matrix_mod = []
# for _ in range(rows):
#     nums = [int(el) for el in input().split()]
#     matrix_mod.append(nums)
[print(*x) for x in (modification(matrix_mod))]
