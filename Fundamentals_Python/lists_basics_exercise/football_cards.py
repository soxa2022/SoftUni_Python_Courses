# lst_input_line = [team for team in input().split(' ')]
lst_input_line = input().split(" ")
lst_a_team = []
lst_b_team = []
team_lost = False
for card in lst_input_line:
    if 'A' in card and card not in lst_a_team:
        lst_a_team.append(card)
    elif 'B' in card and card not in lst_b_team:
        lst_b_team.append(card)
    if len(lst_a_team) >= 5 or len(lst_b_team) >= 5:
        team_lost = True
        break
# lst_b_team = list(set(lst_b_team))
# lst_a_team = list(set(lst_a_team))
print(f"Team A - {11 - len(lst_a_team)}; Team B - {11 - len(lst_b_team)}")
if team_lost:
    print("Game was terminated")

