numbers = int(input())
sum_left = 0
sum_right = 0
for i in range(2 * numbers):
    current_number = int(input())
    if i < numbers:
        sum_left += current_number
    else:
        sum_right += current_number
if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    diff = abs(sum_left - sum_right)
    print(f"No, diff = {diff}")