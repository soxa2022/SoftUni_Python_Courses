def odd_even_sum(number):
    # sum_even = 0
    # sum_odd = 0
    # for digit in number:
    #     if int(digit) % 2 == 0:
    #         sum_even += int(digit)
    #     else:
    #         sum_odd += int(digit)
    sum_even = sum([digit for digit in map(int, number) if digit % 2 == 0])
    sum_odd = sum([digit for digit in map(int, number) if digit % 2 != 0])
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"


input_number = input()
print(odd_even_sum(input_number))
