word = input()
while word != "end":
    reversed_word = word[::-1]
    print(f"{word} = {reversed_word}")
    word = input()

# word = input()
# while word != "end":
#     reversed_word = ''
#     for ch in reversed(word):
#         reversed_word += ch
#     print(word + " = " + reversed_word)
#     word = input()