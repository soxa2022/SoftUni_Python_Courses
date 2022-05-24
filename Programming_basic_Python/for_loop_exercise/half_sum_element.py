import sys
numbers = int(input())
sum = 0
max_number = - sys.maxsize
for i in range(numbers):
    current_number = int(input())
    sum += current_number
    if current_number > max_number:
        max_number = current_number
sum = sum - max_number
if sum == max_number:
    print("Yes")
    print(f"Sum = {sum}")
else:
    diff = abs(sum - max_number)
    print("No")
    print(f"Diff = {diff}")
