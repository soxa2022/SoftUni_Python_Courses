from math import ceil
lst_nums = [int(num) for num in input().split(", ")]
max_number = max(lst_nums)
for i in range(1, ceil(max_number / 10) + 1):
    group = i * 10
    list_numbers = [number for number in lst_nums if number <= group]
    print(f"Group of {group}'s: {list_numbers}")
    lst_nums = list((filter(lambda x: x not in list_numbers, lst_nums)))