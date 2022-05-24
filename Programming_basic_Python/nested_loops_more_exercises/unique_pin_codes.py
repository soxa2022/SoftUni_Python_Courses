first_int = int(input())
second_int = int(input())
third_int = int(input())
num_one = 0
num_two = 0
num_three = 0
for i in range(1, first_int + 1):
    if i % 2 == 0 and i > 0:
        num_one = i
    else:
        continue
    for j in range(1, second_int + 1):
        if j == 2 or j == 3 or j == 5 or j == 7:
            num_two = j
        else:
            continue
        for k in range(1, third_int + 1):
            if k % 2 == 0 and k > 0:
                num_three = k
                print(f"{num_one} {num_two} {num_three}")

