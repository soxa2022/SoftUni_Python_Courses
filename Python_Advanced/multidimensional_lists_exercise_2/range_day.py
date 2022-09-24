def shooter_pos(field):
    for rows in range(size):
        for cols in range(size):
            if field[rows][cols] == "A":
                return rows, cols


def count_target(field):
    count = 0
    for rows in range(size):
        for cols in range(size):
            if field[rows][cols] == 'x':
                count += 1
    return count


def move_func(step, field):
    if direct == 'left':
        if col - step >= 0 and field[row][col - step] == '.':
            field[row][col] = '.'
            field[row][col - step] = 'A'
    elif direct == 'up':
        if row - step >= 0 and field[row - step][col] == '.':
            field[row][col] = '.'
            field[row - step][col] = 'A'
    elif direct == 'down':
        if row + step < size and field[row + step][col] == '.':
            field[row][col] = '.'
            field[row + step][col] = 'A'
    elif direct == 'right':
        if col + step < size and field[row][col + step] == '.':
            field[row][col] = '.'
            field[row][col + step] = 'A'


def shoot_func(field):
    shooting_target = 0
    pos = []
    if direct == 'left':
        if col > 0:
            for i in range(col - 1, -1, -1):
                if field[row][i] == 'x':
                    shooting_target += 1
                    pos = [row, i]
                    field[row][i] = '.'
                    break
    elif direct == 'up':
        if row > 0:
            for i in range(row - 1, -1, -1):
                if field[i][col] == 'x':
                    shooting_target += 1
                    pos = [i, col]
                    field[i][col] = '.'
                    break
    elif direct == 'right':
        if col < size - 1:
            for i in range(col + 1, size):
                if field[row][i] == 'x':
                    shooting_target += 1
                    pos = [row, i]
                    field[row][i] = '.'
                    break
    elif direct == 'down':
        if row < size - 1:
            for i in range(row + 1, size):
                if field[i][col] == 'x':
                    shooting_target += 1
                    pos = [i, col]
                    field[i][col] = '.'
                    break
    return shooting_target, pos


size = 5
# field = [[s for s in input().split()] for _ in range(size)]
field = []
for _ in range(size):
    field.append(input().split())
num_commands = int(input())
shooting_targets = 0
hits_targets = []
count_targets = count_target(field)
for _ in range(num_commands):
    row, col = shooter_pos(field)
    command = input().split()
    action = command[0]
    direct = command[1]
    if action == 'move':
        steps = int(command[2])
        move_func(steps, field)
    elif action == 'shoot':
        shoot_targets, hit_pos = shoot_func(field)
        shooting_targets += shoot_targets
        hits_targets.append(hit_pos)
    if count_targets == shooting_targets:
        break
if count_targets - shooting_targets == 0:
    print(f"Training completed! All {count_targets} targets hit.")
else:
    print(f"Training not completed! {count_targets - shooting_targets} targets left.")
[print(el) for el in hits_targets if el]

