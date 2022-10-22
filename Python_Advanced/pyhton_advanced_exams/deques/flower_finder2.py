from collections import deque

vowels = deque(input().split())
consonants = list(input().split())
is_found = False
flowers = {"rose": 0, "tulip": 0, "lotus": 0, "daffodil": 0}
used_letters = []

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower in flowers:
        if vowel not in used_letters:
            flowers[flower] += flower.count(vowel)
        if consonant not in used_letters:
            flowers[flower] += flower.count(consonant)
        if flowers[flower] == len(flower):
            is_found = True
            print(f"Word found: {flower}")
            break
    used_letters.append(vowel)
    used_letters.append(consonant)
    if is_found:
        break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)} ")
