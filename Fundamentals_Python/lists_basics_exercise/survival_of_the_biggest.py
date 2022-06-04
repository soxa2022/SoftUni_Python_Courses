lst_number = [int(number) for number in input().split(" ")]
count_num = int(input())
for num in range(count_num):
    # min_number = min(lst_number)
    min_number = lst_number[0]
    for i in range(len(lst_number)):
        if lst_number[i] < min_number:
            min_number = lst_number[i]
    lst_number.remove(min_number)
print(*lst_number, sep=', ')



