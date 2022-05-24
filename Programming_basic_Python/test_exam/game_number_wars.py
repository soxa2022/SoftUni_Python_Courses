first_player = input()
second_player = input()
first_player_points = 0
second_player_points = 0
input_line = input()
while input_line != "End of game":
    first_player_card = int(input_line)
    second_player_card = int(input())
    if first_player_card > second_player_card:
        first_player_points += first_player_card - second_player_card
    elif first_player_card < second_player_card:
        second_player_points += second_player_card - first_player_card
    elif first_player_card == second_player_card:
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            print("Number wars!")
            print(f"{first_player} is winner with {first_player_points} points")
            break
        else:
            print("Number wars!")
            print(f"{second_player} is winner with {second_player_points} points")
            break
    input_line = input()
if input_line == "End of game":
    print(f"{first_player} has {first_player_points} points")
    print(f"{second_player} has {second_player_points} points")

