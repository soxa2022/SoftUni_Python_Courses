def func_char(char_1, char_2):
    string = ""
    for i in range(ord(char_1) + 1, ord(char_2)):
        string += chr(i)
    return string


first_char = input()
second_char = input()
print(" ".join(func_char(first_char, second_char)))

