# text = input()
# result = text[0]
# for i in range(1, len(text)):
#     if text[i] != result[-1]:
#         result += text[i]
# print(result)


def repeating_chars(data):
    result = text[0]
    for i in range(1, len(text)):
        if text[i] != result[-1]:
            result += text[i]
    return result


text = input()
print(repeating_chars(text))
