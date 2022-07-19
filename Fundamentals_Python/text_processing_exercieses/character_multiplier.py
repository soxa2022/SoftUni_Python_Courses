# first_string, second_string = input().split()
# total_sum = 0
# counter = 0
# i = 0
# while not counter == len(first_string) and not counter == len(second_string):
#     total_sum += ord(first_string[i:i + 1]) * ord(second_string[i:i + 1])
#     i += 1
#     counter += 1
# if not counter == len(first_string):
#     for ch in first_string[counter:]:
#         total_sum += ord(ch)
# else:
#     for ch in second_string[counter:]:
#         total_sum += ord(ch)
# print(total_sum)
def sum_func(first_word, second_word):
    total_sum = 0
    for idx in range(len(first_word)):
        if idx < len(second_word):
            total_sum += ord(first_word[idx]) * ord(second_word[idx])
        else:
            total_sum += ord(first_word[idx])
    return total_sum


def char_multiplier(first_word, second_word):
    if len(first_word) > len(second_word):
        total_sum = sum_func(first_word, second_word)
    else:
        total_sum = sum_func(second_word, first_word)
    return total_sum


first_string, second_string = input().split()
print(char_multiplier(first_string, second_string))
