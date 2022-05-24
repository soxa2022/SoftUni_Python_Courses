text = input()
list_letters = list()
for index, char in enumerate(text):
    if 60 <= ord(char) <= 90:
        list_letters.append(index)
print(list_letters)
