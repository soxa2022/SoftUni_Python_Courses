first_player_eggs = int(input())
second_player_eggs = int(input())
command_line = input()
is_end_game = True
while command_line != "End":
    if command_line == "one":
        second_player_eggs -= 1
        if second_player_eggs == 0:
            is_end_game = False
            print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
            break
    elif command_line == "two":
        first_player_eggs -= 1
        if first_player_eggs == 0:
            is_end_game = False
            print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
            break
    command_line = input()
if is_end_game:
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")
