SIZE = 7
SCORE = 501

first_player, second_player = list(input().split(', '))
darts = [[int(x) if not x.isalpha() else x for x in input().split()] for _ in range(SIZE)]
turn = [first_player, second_player]
first = first_player
second = second_player
score = {first_player: SCORE, second_player: SCORE}
throws = {first_player: 0, second_player: 0}

while True:

    row, col = [int(x) for x in input().strip('()').split(', ')]
    throws[first] += 1

    if 0 <= row < SIZE and 0 <= col < SIZE:
        if darts[row][col] == 'B':
            print(f"{first} won the game with {throws[first]} throws!")
            break

        elif darts[row][col] == 'D':
            sum_rows_cols = (darts[0][col] + darts[SIZE - 1][col] + darts[row][0] + darts[row][SIZE - 1]) * 2
            score[first] -= sum_rows_cols
        elif darts[row][col] == 'T':
            sum_rows_cols = (darts[0][col] + darts[SIZE - 1][col] + darts[row][0] + darts[row][SIZE - 1]) * 3
            score[first] -= sum_rows_cols

        else:
            score[first] -= darts[row][col]

    if score[first] <= 0:
        print(f"{first} won the game with {throws[first]} throws!")
        break
    turn.append(turn.pop(0))
    first, second = second, first
