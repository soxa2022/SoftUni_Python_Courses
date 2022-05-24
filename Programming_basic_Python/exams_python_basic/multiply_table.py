number = int(input())
number = str(number)
for first_digit in range(1, int(number[2]) + 1):
    if first_digit <= 0:
        continue
    for second_digit in range(1, int(number[1]) + 1):
        if second_digit <= 0:
            continue
        for third_digit in range(1, int(number[0]) + 1):
            if third_digit <= 0:
                continue
            multiplication = first_digit * second_digit * third_digit
            print(f"{first_digit} * {second_digit} * {third_digit} = {multiplication};")
