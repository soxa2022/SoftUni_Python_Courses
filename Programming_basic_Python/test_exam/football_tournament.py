team = input()
count_matches = int(input())
count_wins = 0
count_loses = 0
count_draws = 0
points = 0
if count_matches > 0:
    for number in range(1, count_matches + 1):
        result = input()
        if result == 'W':
            points += 3
            count_wins += 1
        elif result == 'D':
            points += 1
            count_draws += 1
        elif result == 'L':
            count_loses += 1
    print(f"{team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {count_wins}")
    print(f"## D: {count_draws}")
    print(f"## L: {count_loses}")
    percent_wins = count_wins / count_matches * 100
    print(f"Win rate: {percent_wins:.2f}%")
else:
    print(f"{team} hasn't played any games during this season.")