lst_vowels = ['a', 'o', 'u', 'e', 'i']
word = input()
lst_letters = [letter for letter in word if letter.lower() not in lst_vowels]
print(''.join(lst_letters))



# lst_vowels = ['a', 'o', 'u', 'e', 'i']
# lst_letters = list()
# word = input()
# for char in word:
#     if char.lower() not in lst_vowels:
#         lst_letters.append(char)
# print(''.join(lst_letters))