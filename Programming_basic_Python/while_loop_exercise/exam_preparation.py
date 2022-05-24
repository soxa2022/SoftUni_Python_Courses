poor_grade = int(input())
poor_counter = 0
total_grades = 0
brake_time = False
count_grades = 0
last_problem = ''
name_problem = input()
while name_problem != "Enough":
    grade = int(input())
    if grade <= 4:
        poor_counter += 1
    if poor_counter == poor_grade:
        brake_time = True
        break
    last_problem = name_problem
    count_grades += 1
    total_grades += grade
    name_problem = input()
average_grade = total_grades / count_grades
if brake_time:
    print(f"You need a break, {poor_counter} poor grades.")
else:
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem}")


