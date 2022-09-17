def matching_func(string):
    indices = []
    for index in range(len(string)):
        if string[index] == '(':
            indices.append(index)
        elif string[index] == ')':
            start_index = indices.pop()
            print(string[start_index:index + 1])


expression = input()
matching_func(expression)
