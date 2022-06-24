def find_position(maze):
    position = []
    for row in range(len(maze)):
        for el in maze[row]:
            if el == 'k':
                position.append(row)
                position.append(maze[row].index('k'))
                return position


def possible_movies(maze):
    pos_moves = []
    for row in range(len(maze)):
        for el in maze[row]:
            lst_moves = []
            if el == ' ':
                lst_moves.append(row)
                idx = maze[row].index(" ")
                lst_moves.append(maze[row].index(" "))
                maze[row][idx] = "x"
                pos_moves.append(lst_moves)
    return pos_moves


def func_moves(maze):
    num_moves = 1
    kate_pos = find_position(maze)
    lst_moves = possible_movies(maze)
    counter = 0
    while counter < len(lst_moves):
        for digit in lst_moves:
            if kate_pos[0] == digit[0] and kate_pos[1] == digit[1] - 1:
                num_moves += 1
                kate_pos = digit
                lst_moves.remove(digit)
                counter = 0
            elif kate_pos[0] == digit[0] and kate_pos[1] == digit[1] + 1:
                num_moves += 1
                kate_pos = digit
                lst_moves.remove(digit)
                counter = 0
            elif kate_pos[1] == digit[1] and kate_pos[0] == digit[0] - 1:
                num_moves += 1
                kate_pos = digit
                lst_moves.remove(digit)
                counter = 0
            elif kate_pos[1] == digit[1] and kate_pos[0] == digit[0] + 1:
                num_moves += 1
                kate_pos = digit
                lst_moves.remove(digit)
                counter = 0
            else:
                counter += 1
    if kate_pos[0] == 0 or kate_pos[0] == (len(maze) - 1) or kate_pos[1] == 0 or kate_pos[1] == len(maze[0]):
        return f'Kate got out in {num_moves} moves'
    return f'Kate cannot get out'


rows = int(input())
matrix = [[row for row in input()] for i in range(rows)]
print(func_moves(matrix))


