first_player, second_player = input().split(', ')
maze = []
for _ in range(6):
    maze.append(input().split())
first_player_turn = True
second_player_turn = True
while True:
    first_player_row, first_player_col = [int(s) for s in input() if s.isdigit()]
    if first_player_turn:
        if maze[first_player_row][first_player_col] == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
        elif maze[first_player_row][first_player_col] == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        elif maze[first_player_row][first_player_col] == "W":
            first_player_turn = False
            print(f"{first_player} hits a wall and needs to rest.")
    else:
        first_player_turn = True
    second_player_row, second_player_col = [int(s) for s in input() if s.isdigit()]
    if second_player_turn:
        if maze[second_player_row][second_player_col] == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        elif maze[second_player_row][second_player_col] == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        elif maze[second_player_row][second_player_col] == "W":
            second_player_turn = False
            print(f"{second_player} hits a wall and needs to rest.")
    else:
        second_player_turn = True
