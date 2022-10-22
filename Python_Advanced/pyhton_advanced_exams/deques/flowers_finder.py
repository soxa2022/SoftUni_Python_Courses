from collections import deque

main = ["rose", "tulip", "lotus", "daffodil"]
words = main.copy()
vowels_list = deque(input().split())
consonants_list = deque(input().split())
is_found = False
while vowels_list and consonants_list:
    vowel = vowels_list.popleft()
    consonant = consonants_list.pop()
    for idx, word in enumerate(words):
        if vowel in word:
            word = word.replace(vowel, '')
        if consonant in word:
            word = word.replace(consonant, '')
        words[idx] = word
        if not word:
            print(f"Word found: {main[idx]}")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print("Cannot find any word!")
if vowels_list:
    print(f"Vowels left: {' '.join(vowels_list)}")
if consonants_list:
    print(f"Consonants left: {' '.join(consonants_list)}")
