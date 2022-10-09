from pyfiglet import Figlet


class ValueInputError(Exception):
    pass


def printing_board(boards):
    [print(f"| {' | '.join(str(x) for x in row)} |") for row in boards]


def game_play(pos, player_sign):
    row, col = board_pos[pos]
    if board[row][col] == ' ':
        board[row][col] = player_sign
        board_pos.pop(pos)


def check_result(sign):
    n = 3
    is_won = False
    primary_diagonal = set()
    column = set()
    second_diagonal = set()
    for row in range(len(board)):
        if board[row].count(sign) == 3 and board[row][0] == sign:
            is_won = True
            break

        for col in range(size):
            primary_diagonal.add(board[col][col])
            column.add(board[col][row])
            second_diagonal.add(board[n - col - 1][col])
        if len(column) == 1 and column == {sign}:
            is_won = True
            break
        elif len(primary_diagonal) == 1 and primary_diagonal == {sign}:
            is_won = True
            break
        elif len(second_diagonal) == 1 and second_diagonal == {sign}:
            is_won = True
            break
        elif not board_pos:
            print("\nResult is draw!")
            exit()

    return is_won


def number_input_validation(player):
    while True:
        try:
            chosen_position = int(input(f'{player} choose a free position [1-9]: '))
            if not 1 <= chosen_position <= 9 or chosen_position not in board_pos:
                raise ValueInputError
            break
        except (ValueInputError, ValueError):
            printing_board(board)
            print("\nEnter correct value\n")

    return chosen_position


def input_information():
    print(f"{first_player} would you like to play with 'X' or 'O'? ", end='')
    while True:

        try:
            first_player_sign = input().upper()
            if first_player_sign == 'X' or first_player_sign == 'O':
                if first_player_sign == 'X':
                    second_player_sign = 'O'
                else:
                    second_player_sign = 'X'
                break
            raise ValueInputError
        except ValueInputError:
            print("Enter correct value")

    print('This is numeration of the board: ')
    printing_board(press_board)
    print(f"{first_player} starts first!")
    return first_player_sign, second_player_sign


board_pos = {1: (0, 0),
             2: (0, 1),
             3: (0, 2),
             4: (1, 0),
             5: (1, 1),
             6: (1, 2),
             7: (2, 0),
             8: (2, 1),
             9: (2, 2)
             }
size = 3
figlet = Figlet(font='digital')
print(figlet.renderText("Tic-Tac-Toe"))
first_player = input('Player one name: ')
second_player = input('Player two name: ')
press_board = [[i, i + 1, i + 2] for i in range(1, 10, 3)]
board = [[' ' for x in range(size)] for _ in range(size)]
player_one_sign, player_two_sign = input_information()
turn = [[first_player, player_one_sign], [second_player, player_two_sign]]
while True:
    players, players_sign = turn[0]
    chosen_pos = number_input_validation(players)
    game_play(chosen_pos, players_sign)
    printing_board(board)
    if check_result(players_sign):
        print(f"\n{players} won!")
        break
    turn.append(turn.pop(0))
