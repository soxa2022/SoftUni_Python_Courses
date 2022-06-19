lst_numbers = [int(num) for num in input().split(" ")]
summed_value = 0
while len(lst_numbers) != 0:
    current_index = int(input())
    current_number = 0
    if current_index < 0:
        add_number = lst_numbers[-1]
        current_number = lst_numbers.pop(0)
        lst_numbers.insert(0, add_number)
        # current_number = lst_numbers[0]
        # lst_numbers[0] = lst_numbers[-1]
    elif current_index >= len(lst_numbers):
        add_number = lst_numbers[0]
        current_number = lst_numbers.pop()
        lst_numbers.append(add_number)
        # current_number = lst_numbers[-1]
        # lst_numbers[-1] = lst_numbers[0]
    else:
        current_number = lst_numbers.pop(current_index)
    summed_value += current_number
    # for idx in range(len(lst_numbers)):
    #     if lst_numbers[idx] <= current_number:
    #         lst_numbers[idx] += current_number
    #     elif lst_numbers[idx] > current_number:
    #         lst_numbers[idx] -= current_number
    # lst_numbers = list(map(lambda x: x + current_number if x <= current_number else x - current_number, lst_numbers))
    lst_numbers = [x + current_number if x <= current_number else x - current_number for x in lst_numbers]
print(summed_value)
