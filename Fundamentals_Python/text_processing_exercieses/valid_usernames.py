# text = input().split(", ")
# for word in text:
#     if not 3 < len(word) < 16:
#         continue
#     if not word.isalnum():
#         if "-" in word or "_" in word:
#             print(word)
#     else:
#         print(word)
import string


def valid_user(data):
    valid_chars = string.ascii_letters + string.digits + "_" + "-"
    for word in data:
        is_valid = True
        if not 3 < len(word) < 16:
            is_valid = False
        elif not len([x for x in word if x in valid_chars]) == len(word):
            is_valid = False
        elif is_valid:
            print(word)


text = input().split(", ")
valid_user(text)
