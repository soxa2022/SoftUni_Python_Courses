import string


def cal_letters(data):
    total_sum = 0
    for word in data:
        first_pos = string.ascii_lowercase.index(word[0].lower()) + 1
        last_pos = string.ascii_lowercase.index(word[-1].lower()) + 1
        number = int(word[1:len(word) - 1])
        if word[0].isupper():
            number /= first_pos
        elif word[0].islower():
            number *= first_pos
        if word[-1].isupper():
            number -= last_pos
        elif word[-1].islower():
            number += last_pos
        total_sum += number
    return total_sum


text = input().strip().split()
print(f"{cal_letters(text):.2f}")


# def cal_letters(data):
#     total_sum = 0
#     for word in data:
#         number = int(word[1:len(word) - 1])
#         if word[0].isupper():
#             number /= (ord(word[0]) - 64)
#         elif word[0].islower():
#             number *= (ord(word[0]) - 96)
#         if word[-1].isupper():
#             number -= (ord(word[-1]) - 64)
#         elif word[-1].islower():
#             number += (ord(word[-1]) - 96)
#         total_sum += number
#     return total_sum
#
#
# text = input().strip().split()
# print(f"{cal_letters(text):.2f}")
