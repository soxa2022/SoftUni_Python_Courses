count_one = int(input())
count_two = int(input())
count_five = int(input())
paid_sum = int(input())
for i in range(0, count_one + 1):
    for j in range(0, count_two + 1):
        for k in range(0, count_five + 1):
            if i * 1 + j * 2 + k * 5 == paid_sum:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {paid_sum} lv.")