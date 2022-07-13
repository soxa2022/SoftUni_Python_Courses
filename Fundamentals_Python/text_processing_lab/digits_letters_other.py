# text = input()
# dig_string = ''
# char_string = ''
# other_string = ''
# for char in text:
#     if char.isdigit():
#         dig_string += char
#     elif char.isalpha():
#         char_string += char
#     else:
#         other_string += char
# print(f"{dig_string}\n{char_string}\n{other_string}")

def digit_func(text):
    return ''.join(ch for ch in text if ch.isdigit())


def letter_func(text):
    return ''.join(ch for ch in text if ch.isalpha())


def others_func(text):
    return ''.join(ch for ch in text if not ch.isalnum())


data = input()
print(digit_func(data))
print(letter_func(data))
print(others_func(data))
