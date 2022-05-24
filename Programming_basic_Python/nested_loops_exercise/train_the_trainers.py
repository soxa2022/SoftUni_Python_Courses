members = int(input())
pres_name = input()
total_grades = 0
count_pres = 0
sum_aver_grades = 0
while pres_name != "Finish":

    for i in range(1, members + 1):
        grade = float(input())
        total_grades += grade

    print(f"{pres_name} - {(total_grades / members):.2f}.")
    sum_aver_grades += (total_grades / members)
    total_grades = 0
    count_pres += 1
    pres_name = input()
print(f"Student's final assessment is {(sum_aver_grades / count_pres):.2f}.")

