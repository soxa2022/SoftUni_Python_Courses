name = input()
level = 1
total_grades = 0
k = 0
is_ejected = False
while level <= 12:
    grade = float(input())
    if grade < 4:
        k = k + 1
        if k == 2:
            is_ejected = True
            break
        continue
    level += 1
    total_grades += grade
if is_ejected:  # if is_ejected == True:
    print(f"{name} has been excluded at {level} grade")
else:
    average_grade = total_grades / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")

