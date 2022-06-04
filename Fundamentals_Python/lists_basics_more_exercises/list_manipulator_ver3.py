# def get_max(list_num, list_e):
#     for idx in range(len(list_num) - 1, -1, -1):
#         if len(list_e) > 0:
#             if list_num[idx] == max(list_e):
#                 print(idx)
#         else:
#             print("No matches")
#             break

def min_func(list_num, list_e):
    min_num = min(list_e)
    index = list_num.index(min_num)
    for ind, digit in enumerate(list_num):
        if digit == min_num and ind >= index:
            index = ind
    if 0 <= index < len(list_num):
        print(index)
    else:
        print("No matches")


def max_func(list_num, list_e):
    max_num = max(list_e)
    index = list_num.index(max_num)
    for ind, digit in enumerate(list_num):
        if digit == max_num and ind >= index:
            index = ind
    if 0 <= index < len(list_num):
        print(index)
    else:
        print("No matches")


def last_func(list_e):
    counts = int(command[1])
    list_e = list_e[-counts:]
    print(list_e)


def first_func(list_e):
    counts = int(command[1])
    list_e = list_e[:counts]
    print(list_e)


list_numbers = [int(number) for number in input().split(" ")]
command_line = input()
while command_line != "end":
    command = command_line.split(" ")
    action = command[-1]
    type_number = command[0]
    if (type_number == "first" or type_number == 'last') and int(command[1]) > len(list_numbers):
        print("Invalid count")
    elif "exchange" in command:
        count = int(command[-1])
        if 0 <= count < len(list_numbers):
            list_numbers = list_numbers[count + 1:] + list_numbers[:count + 1]
        else:
            print("Invalid index")
    elif action == "even":
        list_even = list(filter(lambda x: x % 2 == 0, list_numbers))
        if len(list_even) == 0 and (type_number == "max" or type_number == 'min'):
            print("No matches")
        elif len(list_even) == 0 and (type_number == "first" or type_number == 'last'):
            print("[]")
        elif type_number == "min":
            min_func(list_numbers, list_even)
        elif type_number == "max":
            max_func(list_numbers, list_even)
        elif type_number == "first":
            first_func(list_even)
        elif type_number == 'last':
            last_func(list_even)
    elif action == "odd":
        list_odd = list(filter(lambda x: x % 2 != 0, list_numbers))
        if len(list_odd) == 0 and (type_number == "max" or type_number == 'min'):
            print("No matches")
        elif len(list_odd) == 0 and (type_number == "first" or type_number == 'last'):
            print("[]")
        elif type_number == "min":
            min_func(list_numbers, list_odd)
        elif type_number == "max":
            max_func(list_numbers, list_odd)
        elif type_number == "first":
            first_func(list_odd)
        elif type_number == 'last':
            last_func(list_odd)
    command_line = input()
print(list_numbers)
