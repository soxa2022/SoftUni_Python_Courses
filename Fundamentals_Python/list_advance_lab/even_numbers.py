lst_number = [int(num) for num in input().split(", ")]
lst_even = list()
for index, digit in enumerate(lst_number):
    if digit % 2 == 0:
        lst_even.append(index)
print(lst_even)
# lst_number = list(map(int, input().split(", ")))
# found_indices = map(lambda x: x if lst_number[x] % 2 == 0 else "none", range(len(lst_number)))
# even_indices = list(filter(lambda b: b != "none", found_indices))
# print(even_indices)
