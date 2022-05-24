input_line = input()
while input_line != 'End':
    if input_line != "SoftUni":
        for char in input_line:
            print(2 * char, end='')
        print()
    input_line = input()
