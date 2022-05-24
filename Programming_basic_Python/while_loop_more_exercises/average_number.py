n = int(input())
sum_numbers = 0
for i in range(1, n + 1):
    numbers = int(input())
    sum_numbers += numbers
print(f"{(sum_numbers / n):.2f}")


