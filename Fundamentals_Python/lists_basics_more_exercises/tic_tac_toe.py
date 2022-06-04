game_lst = [[int(i) for i in input().split(" ")] for j in range(3)]
checklist_1 = []
checklist_2 = []
for j in range(len(game_lst)):
    count_one_4 = game_lst[j].count(1)
    count_two_4 = game_lst[j].count(2)
    checklist = []
    for k in range(len(game_lst[j])):
        checklist.append(game_lst[k][j])
        if k == j:
            checklist_2.append(game_lst[j][k])
        if j + k == 2:
            checklist_1.append(game_lst[j][k])
    count_one = checklist.count(1)
    count_two = checklist.count(2)
    count_one_1 = checklist_1.count(1)
    count_two_1 = checklist_1.count(2)
    count_one_2 = checklist_2.count(1)
    count_two_2 = checklist_2.count(2)
    if count_two_1 == 3 or count_two_2 == 3 or count_two == 3 or count_two_4 == 3:
        print("Second player won")
        break
    elif count_one_1 == 3 or count_one_2 == 3 or count_one == 3 or count_one_4 == 3:
        print("First player won")
        break
else:
    print("Draw!")
