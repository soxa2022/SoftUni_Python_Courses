numbers = int(input())
number = str(numbers)
largest_numbers = ''
while number != "":
    max_digit = max(number)
    largest_numbers += str(max_digit)
    number = number.replace(str(max_digit), "", 1)
print(largest_numbers)

# number = int(input())
# number = str(number)
# largest_number = ''
# while True:
#     max_digit = 0
#     max_index = 0
#     for index, digit in enumerate(number):
#         if int(digit) >= int(max_digit):
#             max_digit = str(digit)
#             max_index = index
#     largest_number += max_digit
#     number = number[:max_index] + number[max_index + 1:]
#     if number == "":
#         break
# print(largest_number)