# lst_numbers = [int(number) for number in input().split(", ")]
# for idx in range(len(lst_numbers) - 1, -1, -1):
#     if lst_numbers[idx] == 0:
#         zero = lst_numbers.pop(idx)
#         lst_numbers.append(zero)
# print(lst_numbers)


lst_numbers = input().split(", ")
for number in lst_numbers:
    if int(number) == 0:
        lst_numbers.remove(number)
        lst_numbers.append(number)
# print([int(num) for num in lst_numbers])
lst_ints_num = []
for num in lst_numbers:
    lst_ints_num.append(int(num))
print(lst_ints_num)
