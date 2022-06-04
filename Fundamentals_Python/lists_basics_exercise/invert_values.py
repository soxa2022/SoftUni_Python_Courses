lst_numbers = [int(number) for number in input().split(' ')]
new_lst = []
for number in lst_numbers:
    if int(number) >= 0:
        number -= 2 * number
    else:
        number = abs(int(number))
    new_lst.append(number)
print(new_lst)


lst_numbers = input().split()
new_lst = []
for number in lst_numbers:
    new_lst.append(-int(number))
print(new_lst)