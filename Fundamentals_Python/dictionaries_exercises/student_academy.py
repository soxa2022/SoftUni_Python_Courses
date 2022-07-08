count_students = int(input())
student_info = {}
for _ in range(count_students):
    name = input()
    grade = float(input())
    if name not in student_info:
        student_info[name] = []
        student_info[name].append(grade)
    else:
        student_info[name].append(grade)
for key, val in student_info.items():
    average_grade = sum(val) / len(val)
    student_info[key] = average_grade
[print(f"{key} -> {value:.2f}") for key, value in student_info.items() if value >= 4.50]

