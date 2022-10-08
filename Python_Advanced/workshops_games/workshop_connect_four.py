from colorama import Fore


class ValueNumberError(Exception):
    pass


def validation_input(name):
    while True:

        try:
            player = int(input(Fore.YELLOW + f'{name}, please choose a column [1-{count_cols}]\n'))
            if 0 < player <= count_cols:
                break
            raise ValueNumberError()

        except (ValueError, ValueNumberError):
            print('Enter correct number\n')

    return player


def reset_func():
    print(Fore.GREEN + "Game is over")
    if input(Fore.RED + 'Do you want to play again [y/n]: ') == 'y':
        start_game(count_cols, count_rows)
    else:
        exit()


def check_moves(board):
    moves = True
    for row in board:
        if not row.count(0) == 0:
            moves = False

    return moves


def printing_board(board):
    res = []
    for row in board:
        res.append(Fore.RED + f"[ {', '.join(map(str, row))} ]")
    return Fore.MAGENTA + '\n'.join(res)


def matrix_input(board, rows, col, num):
    for row in range(rows - 1, -1, -1):
        if board[row].count(0) == 0:
            continue
        if board[row][col - 1] == 0:
            board[row][col - 1] = num
            break
    return printing_board(board)


def check_result(board, num):
    directions = (
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    )
    is_won = False
    for row in range(count_rows):
        for col in range(count_cols):

            if board[row][col] == num:
                for direction in directions:
                    new_row = row
                    new_col = col
                    counter = 0
                    for _ in range(3):
                        new_row += direction[0]
                        new_col += direction[1]
                        if 0 <= new_row < count_rows and 0 <= new_col < count_cols:
                            if board[new_row][new_col] == num:
                                counter += 1
                        else:
                            break
                    if counter == 3:
                        is_won = True
                        return is_won
    return is_won


def play(board, name, rows, num):
    player = validation_input(f'{name}')
    print(matrix_input(board, rows, player, num))

    if check_result(board, num):
        print(Fore.GREEN + f'Winner is {name}')
        reset_func()


def game_four(board, rows):
    first, second = 'Player 1', 'Player 2'
    first_num, second_num = 1, 2
    turn = [[first, first_num], [second, second_num]]
    # '''option for add third player'''
    # first, second, third = 'Player 1', 'Player 2', 'Player 3'
    # first_num, second_num, third_num = 1, 2, 3
    # turn = [[first, first_num], [second, second_num], [third, third_num]]
    print(printing_board(board))
    while True:
        name, num = turn[0]
        play(board, name, rows, num)

        if check_moves(board):
            print(Fore.GREEN + 'Game is draw')
            reset_func()
            # 'second variant  to rotate players for two players'
        # first, second = second, first
        # first_num, second_num = second_num, first_num
        turn.append(turn.pop(0))


def start_game(size, count_row):
    game_board = [[0 for _ in range(size)] for _ in range(count_row)]
    # game_board = [[0] * count_cols for _ in range(count_rows)]
    game_four(game_board, count_row)


count_cols = 7
count_rows = 6
start_game(count_cols, count_rows)
