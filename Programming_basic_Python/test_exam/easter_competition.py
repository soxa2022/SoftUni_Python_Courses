count_breads = int(input())
max_score = 0
best_baker = ''
for i in range(1, count_breads + 1):
    name_baker = input()
    input_line = input()
    total_score = 0
    while input_line != "Stop":
        score = int(input_line)
        total_score += score
        input_line = input()
    print(f"{name_baker} has {total_score} points.")
    if total_score > max_score:
        max_score = total_score
        best_baker = name_baker
        print(f"{name_baker} is the new number 1!")
print(f"{best_baker} won competition with {max_score} points!")
