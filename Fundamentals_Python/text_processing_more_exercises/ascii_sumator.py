def calc_sum(a, b, text):
    total_sum = 0
    for char in text:
        if ord(char) in range(ord(a) + 1, ord(b)):
            total_sum += ord(char)
    return f"{total_sum}"


first_char = input()
second_char = input()
data = input()

if ord(first_char) < ord(second_char):
    print(calc_sum(first_char, second_char, data))
else:
    print(calc_sum(second_char, first_char, data))

# 1- # 2- + STRING - asdasd+$#^sdfd

# def calc_sum(a, b, text):
#     total_sum = 0
#     for char in text:
#         if ord(char) in range(a, b):
#             total_sum += ord(char)
#     return f"{total_sum}"
#
#
# first_char = input()
# second_char = input()
# data = input()
# start = min(ord(first_char), ord(second_char))
# end = max(ord(first_char), ord(second_char))
# print(calc_sum(start, end, data))
