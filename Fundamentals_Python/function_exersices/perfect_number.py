def perfect_number(number):
    # sum_digits = 0
    # for digit in range(1, number ):
    #     if number % digit == 0:
    #         sum_digits += digit
    sum_digits = sum([digit for digit in range(1, number ) if number % digit == 0])
    if sum_digits == number:
        return "We have a perfect number!"
    return "It's not so perfect."


current_number = int(input())
print(perfect_number(current_number))
