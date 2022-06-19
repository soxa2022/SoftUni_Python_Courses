# lst_numbers = [int(number) for number in input().split(", ")]
# lst_pos = [num for num in lst_numbers if num >= 0]
# lst_neg = [num for num in lst_numbers if num < 0]
# lst_even = [num for num in lst_numbers if num % 2 == 0]
# lst_odd = [num for num in lst_numbers if num % 2 != 0]
# print(f"Positive: {', '.join(map(str, lst_pos))}")
# print("Negative: ", end='')
# print(*lst_neg, sep=', ')
# print(f"Even: {str(lst_even)[1:-1]}")
# print(f"Odd: {', '.join(map(str, lst_odd))}")


# nums_string = input().split(", ")
# print(f"Positive: {', '.join(number for number in nums_string if int(number) >= 0)}")
# print(f"Negative: {', '.join(number for number in nums_string if int(number) < 0)}")
# print(f"Even: {', '.join(number for number in nums_string if int(number) %2 == 0)}")
# print(f"Odd: {', '.join(number for number in nums_string if int(number) %2 != 0)}")

# nums_string = input().split(", ")
# print(f"Positive: {', '.join(number for number in nums_string if int(number) >= 0)}")
# print(f"Negative: {', '.join(number for number in nums_string if int(number) < 0)}")
# print(f"Even: {', '.join(number for number in nums_string if int(number) %2 == 0)}")
# print(f"Odd: {', '.join(number for number in nums_string if int(number) %2 != 0)}")


def positive_nums(numbers):
    return [number for number in numbers if int(number) >= 0]


def negative_nums(numbers):
    return [number for number in numbers if int(number) < 0]


def even_nums(numbers):
    return [number for number in numbers if int(number) % 2 == 0]


def odd_nums(numbers):
    return [number for number in numbers if int(number) % 2 != 0]


nums_string = input().split(", ")
print(f"Positive: {', '.join(positive_nums(nums_string))}")
print(f"Negative: {', '.join(negative_nums(nums_string))}")
print(f"Even: {', '.join(even_nums(nums_string))}")
print(f"Odd: {', '.join(odd_nums(nums_string))}")
