player_name = input()
max_points = 0
winner = ''
while player_name != "Stop":
    current_points = 0
    for number in range(len(player_name)):
        num = int(input())
        if num == ord(player_name[number]):
            current_points += 10
        else:
            current_points += 2
    if current_points >= max_points:
        max_points = current_points
        winner = player_name
    player_name = input()
print(f"The winner is {winner} with {max_points} points!")
