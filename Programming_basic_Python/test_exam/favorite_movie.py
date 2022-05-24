command_line = input()
name_movie = ''
max_points = 0
count_movies = 0
while command_line != "STOP":
    count_movies += 1
    count_points = 0
    for character in command_line:
        count_points += ord(character)
        if ord("A") <= ord(character) <= ord("Z"):
            count_points -= len(command_line)
        elif ord("a") <= ord(character) <= ord("z"):
            count_points -= 2 * len(command_line)
    if count_points > max_points:
        max_points = count_points
        name_movie = command_line
    if count_movies == 7:
        print("The limit is reached.")
        break
    command_line = input()
print(f"The best movie for you is {name_movie} with {max_points} ASCII sum.")
