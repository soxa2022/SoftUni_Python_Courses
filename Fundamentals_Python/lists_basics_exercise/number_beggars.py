# lst_numbers = [int(number) for number in input().split(", ")]
lst_numbers = input().split(", ")
count_begs = int(input())
lst_takes = []
for index in range(count_begs):
    sum = 0
    while index < len(lst_numbers):
        sum += int(lst_numbers[index])  # sum += lst_numbers[index]
        index += count_begs
    lst_takes.append(sum)
print(lst_takes)
