data = input()
symbols = ""
explosion = 0
for index, char in enumerate(data):
    if char == ">":
        explosion += int(data[index + 1])
        symbols += char
    elif char != ">" and explosion > 0:
        explosion -= 1
    else:
        symbols += char

print(symbols)
