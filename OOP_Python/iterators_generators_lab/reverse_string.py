# def reverse_text(string):
#     index = -1
#     while index >= - len(string):
#         yield string[index]
#         index -= 1
def reverse_text(string):
    index = 0
    n = len(string)
    while index < n:
        yield string[n - index - 1]
        index += 1
