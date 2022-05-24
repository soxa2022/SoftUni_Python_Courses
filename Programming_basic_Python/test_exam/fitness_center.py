people_in_fitness = int(input())
total_work_out = 0
total_protein = 0
count_legs = 0
count_abs = 0
count_chest = 0
count_back = 0
count_bar = 0
count_shake = 0
for human in range(1, people_in_fitness + 1):
    input_lime = input()
    if input_lime == "Back":
        count_back += 1
    elif input_lime == "Chest":
        count_chest += 1
    elif input_lime == "Legs":
        count_legs += 1
    elif input_lime == "Abs":
        count_abs += 1
    elif input_lime == "Protein shake":
        count_shake += 1
    elif input_lime == "Protein bar":
        count_bar += 1
total_work_out = count_legs + count_back + count_abs + count_chest
total_protein = count_shake + count_bar
percent_work_out = total_work_out / people_in_fitness * 100
percent_protein = total_protein / people_in_fitness * 100
print(f"{count_back} - back")
print(f"{count_chest} - chest")
print(f"{count_legs} - legs")
print(f"{count_abs} - abs")
print(f"{count_shake} - protein shake")
print(f"{count_bar} - protein bar")
print(f"{percent_work_out:.2f}% - work out")
print(f"{percent_protein:.2f}% - protein")

