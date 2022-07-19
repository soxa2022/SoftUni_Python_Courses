# text = input()
# result = ""
# for char in text:
#     result += chr(ord(char) + 3)
# print(result)


def cipher_func(data):
    # result = ""
    # for char in text:
    #     result += chr(ord(char) + 3)
    result = [chr(ord(char) + 3) for char in text]
    return f"{''.join(result)}"


text = input()
print(cipher_func(text))
