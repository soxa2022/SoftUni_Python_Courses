some_text = input()
sum = 0
length = len(some_text)
for i in range(length):
    if some_text[i] == "a":
        sum += 1
    if some_text[i] == "e":
        sum += 2
    if some_text[i] == "i":
        sum += 3
    if some_text[i] == "o":
        sum += 4
    if some_text[i] == "u":
        sum += 5
print(sum)
