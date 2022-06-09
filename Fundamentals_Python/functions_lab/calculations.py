import operator


def calculator(action, a, b):
    operation_dict = {"divide": operator.truediv, "subtract": operator.sub, "add": operator.add,
                      "multiply": operator.mul}
    return int(operation_dict[action](a, b))


actions = input()
first_num = int(input())
second_num = int(input())
print(calculator(actions, first_num, second_num))

# print(calculator(action=input(), a=int(input()), b=int(input())))
# def calculator(action, a, b):
#     if action == "multiply":
#         return a * b
#     elif action == "add":
#         return a + b
#     elif action == "subtract":
#         return a - b
#     elif action == "divide":
#         return int(a / b)
#
#
# actions = input()
# first_num = int(input())
# second_num = int(input())
# print(calculator(actions, first_num, second_num))

