tournament_name = input()
counter_win = 0
counter_lost = 0
total_games = 0
while tournament_name != "End of tournaments":
    number_games = int(input())
    counter_games = 0
    for i in range(1, number_games + 1):
        counter_games += 1
        team_points = int(input())
        rival_points = int(input())
        diff = abs(team_points - rival_points)
        if team_points > rival_points:
            counter_win += 1
            print(f"Game {counter_games} of tournament {tournament_name}: win with {diff} points.")
        else:
            counter_lost += 1
            print(f"Game {counter_games} of tournament {tournament_name}: lost with {diff} points.")
    total_games += counter_games
    tournament_name = input()
percent_win_games = counter_win / total_games * 100
percent_lost_games = counter_lost / total_games * 100
print(f"{percent_win_games:.2f}% matches win")
print(f"{percent_lost_games:.2f}% matches lost")
