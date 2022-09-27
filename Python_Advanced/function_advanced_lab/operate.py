def operate(operator, *args):
    def add():
        return sum(args)

    # def subtract():
    #     result = args[0]
    #     for el in args[1:]:
    #         result -= el
    #     return result
    def subtract():
        return args[0] + sum(-s for s in args[1:])

    def multiply():
        result = 1
        for el in args:
            result *= el
        return result

    def divide():
        result = args[0]
        for el in args[1:]:
            result /= el
        return result

    if operator == '+':
        return add()
    elif operator == '-':
        return subtract()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()

# from functools import reduce
#
#
# def operate(operator, *args):
#     def add():
#         return sum(args)
#
#     def subtract():
#         return reduce(lambda x, y: x - y, args)
#
#     def multiply():
#         return reduce(lambda x, y: x * y, args)
#
#     def divide():
#         try:
#             return reduce(lambda x, y: x / y, args)
#         except:
#             return
#
#     if operator == '+':
#         return add()
#     elif operator == '-':
#         return subtract()
#     elif operator == '*':
#         return multiply()
#     elif operator == '/':
#         return divide()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
