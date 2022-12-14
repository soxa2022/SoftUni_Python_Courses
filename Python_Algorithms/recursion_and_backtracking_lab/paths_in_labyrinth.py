def validation(row, col, lab):
    if not (0 <= row < len(lab) and 0 <= col < len(lab[row])):
        return False
    if lab[row][col] == "*":
        return False
    if lab[row][col] == "v":
        return False
    return True


def find_all_paths(row, col, lab, direction, path):
    if not validation(row, col, lab):
        return
    path.append(direction)
    if lab[row][col] == "e":
        print("".join(path))
    else:
        lab[row][col] = "v"
        find_all_paths(row + 1, col, lab, 'D', path)
        find_all_paths(row - 1, col, lab, 'U', path)
        find_all_paths(row, col - 1, lab, 'L', path)
        find_all_paths(row, col + 1, lab, 'R', path)
        lab[row][col] = "-"
    path.pop()


N = int(input())
M = int(input())

labyrinth = []
for _ in range(N):
    labyrinth.append(list(input()))

find_all_paths(0, 0, labyrinth, '', [])