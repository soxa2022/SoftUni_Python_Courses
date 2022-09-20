from collections import deque


def operation_func(op, nums, string):
    res = nums.popleft()
    while nums:
        res = res + op + nums.popleft()
        res = str(int(eval(res)))
    string.appendleft(str(int(res)))
    return string


def expression_eval(string):
    numbers = deque()
    while string:
        char = string.popleft()
        if char in '+-*/':
            operation_func(char, numbers, string)
        else:
            numbers.append(char)
    return print(*numbers)


string_expression = deque(input().split())
expression_eval(string_expression)

# def expression_eval(string):
#     numbers = deque()
#     while string:
#         char = string.popleft()
#         if char in '+-*/':
#             if char == '+':
#                 result = numbers.popleft()
#                 while numbers:
#                     result += numbers.popleft()
#                 string.appendleft(str(result))
#
#             elif char == '*':
#                 result = numbers.popleft()
#                 while numbers:
#                     result *= numbers.popleft()
#                 string.appendleft(str(result))
#
#             elif char == '/':
#                 result = numbers.popleft()
#                 while numbers:
#                     result //= numbers.popleft()
#                 string.appendleft(str(result))
#
#             elif char == '-':
#                 result = numbers.popleft()
#                 while numbers:
#                     result -= numbers.popleft()
#                 string.appendleft(str(result))
#         else:
#             numbers.append(int(char))
#     return print(*numbers)
#
#
# string_expression = deque(input().split())
# expression_eval(string_expression)
