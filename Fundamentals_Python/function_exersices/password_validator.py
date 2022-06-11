# def validator(text):
#     is_valid = True
#     count_chars = 0
#     count_digits = 0
#     mistake = ''
#     for char in text:
#         if 97 <= ord(char) <= 122 or 65 <= ord(char) <= 90: # if char.isalpha():
#             count_chars += 1
#         if 48 <= ord(char) <= 57:  # if char.isdigit():
#             count_digits += 1
#     if len(text) < 6 or len(text) > 10:
#         is_valid = False
#         mistake = "Password must be between 6 and 10 characters\n"
#     if count_chars + count_digits != len(text):
#         is_valid = False
#         mistake += "Password must consist only of letters and digits\n"
#     if count_digits < 2:
#         is_valid = False
#         mistake += "Password must have at least 2 digits\n"
#     if is_valid:
#         return "Password is valid"
#     else:
#         return mistake
#
#
# password = input()
# print(validator(password))


def length_is_valid(some_string):
    if 6 <= len(some_string) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def symbols_are_valid(some_string):
    if some_string.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def have_at_least_two_digits(some_string):
    digits_counter = 0
    for character in some_string:
        if character.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


some_password = input()
validated = [length_is_valid(some_password), symbols_are_valid(some_password), have_at_least_two_digits(some_password)]
if all(validated):
    print("Password is valid")
