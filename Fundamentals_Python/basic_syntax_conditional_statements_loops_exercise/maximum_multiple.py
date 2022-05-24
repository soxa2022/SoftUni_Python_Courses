# divisor = int(input())
# boundary_number = int(input())
# largest_number = 0
# for number in range(1, boundary_number + 1):
#     if number % divisor == 0:
#         if number > largest_number:
#             largest_number = number
# print(largest_number)
#
divisor = int(input())
boundary_number = int(input())
max_multiplier_number = 0
for number in range(boundary_number, divisor, -1):
    if number % divisor == 0:
        max_multiplier_number = number
        break
print(max_multiplier_number)

# divisor = int(input())
# boundary_number = int(input())
# max_multiplier_number = (boundary_number // divisor) * divisor
# print(max_multiplier_number)
