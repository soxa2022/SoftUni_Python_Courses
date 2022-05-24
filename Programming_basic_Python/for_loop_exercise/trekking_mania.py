count_groups = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0
total_people = 0
for i in range(1, count_groups + 1):
    people = int(input())
    total_people = total_people + people
    if people <= 5:
        group_1 += people
    elif people <= 12:
        group_2 += people
    elif people <= 25:
        group_3 += people
    elif people <= 40:
        group_4 += people
    elif people > 40:
        group_5 += people
# total_people = group_1 + group_2 + group_3 + group_4 + group_5
percent_group_1 = (group_1 / total_people) * 100
percent_group_2 = (group_2 / total_people) * 100
percent_group_3 = (group_3 / total_people) * 100
percent_group_4 = (group_4 / total_people) * 100
percent_group_5 = (group_5 / total_people) * 100
print(f"{percent_group_1:.2f}%")
print(f"{percent_group_2:.2f}%")
print(f"{percent_group_3:.2f}%")
print(f"{percent_group_4:.2f}%")
print(f"{percent_group_5:.2f}%")

