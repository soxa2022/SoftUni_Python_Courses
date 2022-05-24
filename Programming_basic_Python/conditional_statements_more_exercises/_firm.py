import math
needed_hours = int(input())
days_for_project = int(input())
workers_overtime = int(input())
work_hours = math.floor(days_for_project * 8 * 0.9 + days_for_project * workers_overtime * 2)
diff = abs(work_hours - needed_hours)
if needed_hours <= work_hours:
    print(f"Yes!{diff} hours left.")
else:
    print(f"Not enough time!{diff} hours needed.")
