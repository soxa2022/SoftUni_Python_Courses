def get_points(rows, cols, player_score):
    if board[rows][cols] == 'D':
        player_score -= sum(map(int, [board[0][cols], board[rows][0], board[6][cols], board[rows][6]])) * 2
    elif board[rows][cols] == 'T':
        player_score -= sum(map(int, [board[0][cols], board[rows][0], board[6][cols], board[rows][6]])) * 3
    elif board[rows][cols] == 'B':
        player_score -= 501
    else:
        player_score -= int(board[rows][cols])
    return player_score


def game(row, col,player_score, player_throws):
    if 0 <= row < 7 and 0 <= col < 7:
        player_throws += 1
        player_score = get_points(row, col, player_score)
    else:
        player_throws += 1
    return player_score, player_throws


first_player, second_player = input().split(", ")
size = 7
first_player_score = 501
second_player_score = 501
board = [input().split() for _ in range(size)]
first_player_throws = 0
second_player_throws = 0

while True:
    rows, cols = map(int, input().strip("(").strip(")").split(", "))
    first_player_score, first_player_throws = game(rows, cols, first_player_score, first_player_throws)
    if first_player_score <= 0:
        print(f"{first_player} won the game with {first_player_throws} throws!")
        break

    rows, cols = map(int, input().strip("(").strip(")").split(", "))
    second_player_score, second_player_throws = game(rows, cols, second_player_score, second_player_throws)
    if second_player_score <= 0:
        print(f"{second_player} won the game with {second_player_throws} throws!")
        break

