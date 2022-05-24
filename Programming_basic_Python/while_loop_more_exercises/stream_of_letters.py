letters = input()
word = ''
counter_for_c = 0
counter_for_o = 0
counter_for_n = 0
while letters != "End":
    letters = ord(letters)
    if 65 <= letters <= 90:
        symbol = chr(letters)
        word = (word + symbol)
    if 97 <= letters <= 122:
        if letters == 110 and counter_for_n < 1:
            counter_for_n += 1
        elif letters == 99 and counter_for_c < 1:
            counter_for_c += 1
        elif letters == 111 and counter_for_o < 1:
            counter_for_o += 1
        else:
            symbol = chr(letters)
            word = (word + symbol)
        if counter_for_n == 1 and counter_for_c == 1 and counter_for_o == 1:
            print(word , end='')
            print(" ", end='')
            word = ""
            counter_for_c = counter_for_o = counter_for_n = 0
    letters = input()