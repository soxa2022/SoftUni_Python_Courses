first_number = int(input())
second_number = int(input())
first_number = str(first_number)
second_number = str(second_number)
first_digit_one = int(first_number[0])
first_digit_two = int(second_number[0])
second_digit_one = int(first_number[1])
second_digit_two = int(second_number[1])
third_digit_one = int(first_number[2])
third_digit_two = int(second_number[2])
forth_digit_one = int(first_number[3])
forth_digit_two = int(second_number[3])
for first_digit in range(first_digit_one, first_digit_two + 1):
    if first_digit % 2 == 0:
        continue
    else:
        for second_digit in range(second_digit_one, second_digit_two + 1):
            if second_digit % 2 == 0:
                continue
            else:
                for third_digit in range(third_digit_one, third_digit_two + 1):
                    if third_digit % 2 == 0:
                        continue
                    else:
                        for forth_digit in range(forth_digit_one, forth_digit_two + 1):
                            if forth_digit % 2 == 0:
                                continue
                            else:
                                print(f"{first_digit}{second_digit}{third_digit}{forth_digit}", end=' ')
