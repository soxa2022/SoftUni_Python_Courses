num = int(input())
lst_numbers = []
for i in range(num):
    number = int(input())
    lst_numbers.append(number)
command = input()
new_list = []
if command == "even":
    for j in range(len(lst_numbers)):
        if lst_numbers[j] % 2 == 0:
            new_list.append(lst_numbers[j])
elif command == "odd":
    for j in range(len(lst_numbers)):
        if lst_numbers[j] % 2 != 0:
            new_list.append(lst_numbers[j])
elif command == "negative":
    for j in lst_numbers:
        if j < 0:
            new_list.append(j)
elif command == "positive":
    for j in lst_numbers:
        if j >= 0:
            new_list.append(j)
print(new_list)