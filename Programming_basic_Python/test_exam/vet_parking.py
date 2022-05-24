count_days = int(input())
count_hours = int(input())
tax = 0
total_sum = 0
day_sum = 0
for i in range(1, count_days + 1):
    for j in range(1, count_hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            tax = 2.50
        elif i % 2 != 0 and j % 2 == 0:
            tax = 1.25
        else:
            tax = 1
        day_sum += tax
    print(f"Day: {i} - {day_sum:.2f} leva")
    total_sum += day_sum
    day_sum = 0
print(f"Total: {total_sum:.2f} leva")