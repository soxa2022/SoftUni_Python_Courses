secret_message = input().split(" ")
for i, word in enumerate(secret_message):
    digits = ""
    characters = ""
    for char in word:
        if char.isdigit():
            digits += char
        else:
            characters += char
    digits = chr(int(digits))
    secret_message[i] = digits + characters
for index, new_word in enumerate(secret_message):
    x = new_word[-1]
    y = new_word[1]
    new_word = new_word[:1] + x + new_word[2:]
    new_word = new_word[:-1] + y
    secret_message[index] = new_word
print(" ".join(secret_message))

# messages = input().split()
# final_message = []
# for message in messages:
#     number = ""
#     current_message = ""
#     for character in message:
#         if character.isdigit():
#             number += character
#         else:
#             break
#     message = message.replace(number, '')
#     number = int(number)
#     current_message += chr(number)
#     if len(message) >= 2:
#         message = message[-1] + message[1:-1] + message[0]
#     current_message += message
#     final_message.append(current_message)
# print(" ".join(final_message))
