def game(player_row, player_col, player_turn, first_players, second_players):
    if player_turn:
        if maze[player_row][player_col] == "E":
            print(f"{first_players} found the Exit and wins the game!")
            exit()
        elif maze[player_row][player_col] == "T":
            print(f"{first_players} is out of the game! The winner is {second_players}.")
            exit()
        elif maze[player_row][player_col] == "W":
            player_turn = False
            print(f"{first_players} hits a wall and needs to rest.")
    else:
        player_turn = True
    return player_turn


first_player, second_player = input().split(', ')
maze = []
for _ in range(6):
    maze.append(input().split())
first_player_turn = True
second_player_turn = True
while True:
    first_player_row, first_player_col = [int(s) for s in input() if s.isdigit()]
    first_player_turn = game(first_player_row, first_player_col, first_player_turn, first_player, second_player)
    second_player_row, second_player_col = [int(s) for s in input() if s.isdigit()]
    second_player_turn = game(second_player_row, second_player_col, second_player_turn, second_player, first_player)
