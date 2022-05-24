player_name = input()
best_player = ""
best_player_goals = 0
while player_name != "END":
    score_goals = int(input())
    if score_goals > best_player_goals:
        best_player_goals = score_goals
        best_player = player_name
    if best_player_goals >= 10:
        break
    player_name = input()
print(f"{best_player} is the best player!")
if best_player_goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")