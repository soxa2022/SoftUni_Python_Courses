import re

text = input()
word = input()
pattern = fr'\b{word}\b'
count_words = re.findall(pattern, text, flags=re.IGNORECASE)
# count_words = re.findall(word+"\\b", text, flags=re.I)
print(len(count_words))
