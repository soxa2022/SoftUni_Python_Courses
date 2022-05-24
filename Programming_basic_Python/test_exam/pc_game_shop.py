number_of_sold_games = int(input())
heartstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
others_counter = 0
for game in range(number_of_sold_games):
    current_game_name = input()
    if current_game_name == "Hearthstone":
        heartstone_counter += 1
    elif current_game_name == "Fornite":
        fornite_counter += 1
    elif current_game_name == "Overwatch":
        overwatch_counter += 1
    else:
        others_counter += 1
heartstone_percent = heartstone_counter / number_of_sold_games * 100
fornite_percent = fornite_counter / number_of_sold_games * 100
overwatch_percent = overwatch_counter / number_of_sold_games * 100
others_percent = others_counter / number_of_sold_games * 100
print(f"Hearthstone - {heartstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {others_percent:.2f}%")
