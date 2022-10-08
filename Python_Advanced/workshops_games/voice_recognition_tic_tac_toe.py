from pyfiglet import Figlet
import SpeechRecognition as sr


def check_for_win():
    player_name, player_symbol = players[0]
    size = len(board)

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size)])
    second_diagonal_win = all([board[i][size - 1 - i] == player_symbol for i in range(size)])

    print([all(True if pos == player_symbol else False for pos in row) for row in board])

    row_win = any([all(True if pos == player_symbol else False for pos in row) for row in board]) # True, False, False
    col_win = any([all(True if board[r][c] == player_symbol else False for r in range(size)) for c in range(size)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")

        raise SystemExit

    players.append(players.pop(0))


def place_symbol(position):
    row, col = (position - 1) // 3, (position - 1) % 3

    board[row][col] = players[0][1]

    check_for_win()

    print_board()
    choose_position()


def choose_position():
    while True:
        try:
            position = int(input(f"{players[0][0]} choose a free position [1-9]: "))
        except ValueError:
            print(f"{players[0][0]}, please select a valid position!")
            continue

        if 1 <= position <= len(board) * len(board):
            place_symbol(int(position))
            break
        else:
            print(f"{players[0][0]}, please select a valid position!")


def print_board(begin=False):
    if begin:
        print("This is the numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{players[0][0]} starts first!")

        for row in range(len(board)):
            for col in range(len(board)):
                board[row][col] = ' '
    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    figlet = Figlet(font='big')
    print(figlet.renderText("Tic-Tac-Toe"))

    with sr.Microphone() as source:
        r = sr.Recognizer()

        print("Player one, say your name")

        audio_data = r.record(source, duration=2)
        print("Recognizing...")
        player_one_name = r.recognize_google(audio_data)

        print("Player two, say your name")

        audio_data = r.record(source, duration=2)
        print("Recognizing...")
        player_two_name = r.recognize_google(audio_data)

    while True:
        player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

        if player_one_symbol not in ['X', 'O']:
            print(f"{player_one_name}, please select a valid option")
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board(begin=True)
    choose_position()


players = []
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]

start()
