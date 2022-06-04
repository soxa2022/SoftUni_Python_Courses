factor = int(input())
count = int(input())
lst_numbers = []
for number in range(1, count + 1):
    num = factor * number
    lst_numbers.append(num)
print(lst_numbers)


# factor = int(input())
# count = int(input())
# lst_numbers = list(range(factor, factor * count + 1, factor))
# print(lst_numbers)