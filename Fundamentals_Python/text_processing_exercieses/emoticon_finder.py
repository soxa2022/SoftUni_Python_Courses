# text = input()
# for i in range(len(text)):
#     if text[i] == ":":
#         print(text[i] + text[i + 1])
def emo_finder(data):
    result = [data[i] + data[i + 1] for i in range(len(data)) if data[i] == ":"]
    sep = "\n"
    return f"{sep.join(result)}"


text = input()
print(emo_finder(text))
