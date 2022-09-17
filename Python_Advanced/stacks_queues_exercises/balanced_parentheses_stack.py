def brackets(data):
    stack = []
    for bracket in data:
        if bracket in ["(", '[', '{']:
            stack.append(bracket)
        elif bracket in [')', ']', '}']:
            if len(stack) == 0:
                return "NO"
            if (stack.pop() + bracket) in ['[]', '()', '{}']:
                continue
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    return "NO"


input_line = input()
print(brackets(input_line))
