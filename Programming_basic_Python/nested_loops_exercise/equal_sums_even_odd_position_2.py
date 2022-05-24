number_one = int(input())
number_two = int(input())
for i in range(number_one, number_two + 1):
    sum_odd_pos = 0
    sum_even_pos = 0
    count_position = 0
    current_number = int(i)
    while current_number > 0:
        digit = current_number % 10
        current_number = current_number // 10
        if count_position % 2 == 0:
            sum_even_pos += digit
        else:
            sum_odd_pos += digit
        count_position = count_position + 1
    if sum_even_pos == sum_odd_pos:
        print(f"{i}", end=' ')
