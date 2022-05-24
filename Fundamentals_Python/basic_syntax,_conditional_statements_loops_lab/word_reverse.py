# word = input()
# index = 0
# for letter in range(len(word)):
#     index -= 1
#     print(word[index], end='')

word = input()
reversed_word = ''
for letter in range(len(word) - 1, -1, -1):
    reversed_word += word[letter]
print(reversed_word)

# word = input()
# print(word[::-1])
