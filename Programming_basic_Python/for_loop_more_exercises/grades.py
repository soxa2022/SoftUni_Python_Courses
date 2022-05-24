students = int(input())
grade_1 = 0
grade_2 = 0
grade_3 = 0
grade_4 = 0
total_grades = 0
for i in range(1, students + 1):
    grade = float(input())
    if grade < 3:
        grade_1 = grade_1 + 1
    elif grade < 4:
        grade_2 = grade_2 + 1
    elif grade < 5:
        grade_3 = grade_3 + 1
    elif grade >= 5:
        grade_4 = grade_4 + 1
    total_grades = total_grades + grade
average_grade = total_grades / students
row_1 = grade_1 / students * 100
row_2 = grade_2 / students * 100
row_3 = grade_3 / students * 100
row_4 = grade_4 / students * 100
print(f"Top students: {row_4:.2f}%")
print(f"Between 4.00 and 4.99: {row_3:.2f}%")
print(f"Between 3.00 and 3.99: {row_2:.2f}%")
print(f"Fail: {row_1:.2f}%")
print(f"Average: {average_grade:.2f}")