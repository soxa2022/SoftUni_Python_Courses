students = int(input())
grade_one = 0
grade_two = 0
grade_three = 0
grade_four = 0
total_grades = 0
for number in range(1, students + 1):
    grade = float(input())
    if grade < 3:
        grade_one = grade_one + 1
    elif grade < 4:
        grade_two = grade_two + 1
    elif grade < 5:
        grade_three = grade_three + 1
    elif grade >= 5:
        grade_four = grade_four + 1
    total_grades = total_grades + grade
average_grade = total_grades / students
percent_grade_one = grade_one / students * 100
percent_grade_two = grade_two / students * 100
percent_grade_three = grade_three / students * 100
percent_grade_four = grade_four / students * 100
print(f"Top students: {percent_grade_four:.2f}%")
print(f"Between 4.00 and 4.99: {percent_grade_three:.2f}%")
print(f"Between 3.00 and 3.99: {percent_grade_two:.2f}%")
print(f"Fail: {percent_grade_one:.2f}%")
print(f"Average: {average_grade:.2f}")