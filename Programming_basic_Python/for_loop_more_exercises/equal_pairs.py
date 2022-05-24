n = int(input())
diff_max = 0
total_2 = 0
number_1 = int(input())
number_2 = int(input())
total_1 = number_1 + number_2
for i in range(1, n):
    number_3 = int(input())
    number_4 = int(input())
    total_2 = number_3 + number_4
    diff = abs(total_2 - total_1)
    if diff > diff_max:
        diff_max = diff
    if total_2 != total_1:
        total_1 = total_2
if diff_max == 0:
    print(f"Yes, value={total_1}")
else:
    print(f"No, maxdiff={diff_max}")
