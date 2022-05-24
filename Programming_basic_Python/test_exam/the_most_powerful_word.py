import math
word = input()
max_points = 0
the_most_word = ''
list_letters = ['a', 'e', 'i', 'o', 'u', 'y']
list_letters_upper = ['A', 'E', 'I', 'O', 'U', 'Y']
while word != "End of words":
    word_points = 0
    for character in word:
        word_points += ord(character)
    if word[0] in list_letters or word[0] in list_letters_upper:
        word_points *= len(word)
    else:
        word_points = math.floor(word_points / len(word))
    if word_points > max_points:
        max_points = word_points
        the_most_word = word
    word = input()
print(f"The most powerful word is {the_most_word} - {max_points}")



