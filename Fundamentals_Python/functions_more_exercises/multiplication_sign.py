# lst_numbers = list()
# count_negative = 0
# count_positive = 0
# for _ in range(3):
#     lst_numbers.append(int(input()))
# for digit in lst_numbers:
#     if digit < 0:
#         count_negative += 1
#     elif digit > 0:
#         count_positive += 1
# if count_negative + count_positive != 3:
#     print('zero')
# elif count_negative % 2 != 0:
#     print("negative")
# else:
#     print("positive")

lst_numbers = list()
count_negative = 0
for _ in range(3):
    lst_numbers.append(int(input()))
for digit in lst_numbers:
    if digit < 0:
        count_negative += 1
if not all(lst_numbers):
    print('zero')
elif count_negative % 2 != 0:
    print("negative")
else:
    print("positive")


