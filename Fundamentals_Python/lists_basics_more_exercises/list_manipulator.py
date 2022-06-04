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
        list_even = []
        for num in list_numbers:
            if num % 2 == 0:
                list_even.append(num)
        if len(list_even) == 0 and (type_number == "max" or type_number == 'min'):
            print("No matches")
        elif len(list_even) == 0 and (type_number == "first" or type_number == 'last'):
            print("[]")
        elif type_number == "min":
            min_num = min(list_even)
            index = list_numbers.index(min_num)
            for ind, digit in enumerate(list_numbers):
                if digit == min_num and ind >= index:
                    index = ind
            if 0 <= index < len(list_numbers):
                print(index)
            else:
                print("No matches")
        elif type_number == "max":
            max_num = max(list_even)
            index = list_numbers.index(max_num)
            for ind, digit in enumerate(list_numbers):
                if digit == max_num and ind >= index:
                    index = ind
            if 0 <= index < len(list_numbers):
                print(index)
            else:
                print("No matches")
        elif type_number == "first":
            count = int(command[1])
            list_even = list_even[:count]
            print(list_even)
        elif type_number == 'last':
            count = int(command[1])
            list_even = list_even[-count:]
            print(list_even)
    elif action == "odd":
        list_odd = []
        for num in list_numbers:
            if num % 2 != 0:
                list_odd.append(num)
        if len(list_odd) == 0 and (type_number == "max" or type_number == 'min'):
            print("No matches")
        elif len(list_odd) == 0 and (type_number == "first" or type_number == 'last'):
            print("[]")
        elif type_number == "min":
            min_num = min(list_odd)
            index = list_numbers.index(min_num)
            for ind, digit in enumerate(list_numbers):
                if digit == min_num and ind >= index:
                    index = ind
            if 0 <= index < len(list_numbers):
                print(index)
            else:
                print("No matches")
        elif type_number == "max":
            max_num = max(list_odd)
            index = list_numbers.index(max_num)
            for ind, digit in enumerate(list_numbers):
                if digit == max_num and ind >= index:
                    index = ind
            if 0 <= index < len(list_numbers):
                print(index)
            else:
                print("No matches")
        elif type_number == "first":
            count = int(command[1])
            list_odd = list_odd[:count]
            print(list_odd)
        elif type_number == 'last':
            count = int(command[1])
            list_odd = list_odd[-count:]
            print(list_odd)
    command_line = input()
print(list_numbers)
