def reverse_func(string):
    while string:
        print(string.pop(), end='')


text = list(input())
reverse_func(text)

# def reversed_func(string, stack):
#     for i in range(len(string)):
#         stack.append(string.pop())
#     return stack
#
#
# main_string = list(input())
# stack = []
# print(''.join(reversed_func(main_string, stack)))


