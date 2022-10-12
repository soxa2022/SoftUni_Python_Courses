from febonacii import create_sequence, locate_number

while True:
    command = input().split()
    if command == 'Stop':
        break
    result = None
    if command[0] == 'Create':
        result = create_sequence(int(command[-1]))

    elif command[0] == 'Locate':
        result = locate_number(int(command[-1]))
    print(result)
