def data_types(command, string):
    result = 0
    if command == 'int':
        result = int(string) * 2
        return result
    elif command == "real":
        result = (float(string) * 1.50)
        return f"{result:.2f}"
    elif command == "string":
        result = "$" + string + "$"
        return result


command_input = input()
word = input()
print(data_types(command_input, word))
