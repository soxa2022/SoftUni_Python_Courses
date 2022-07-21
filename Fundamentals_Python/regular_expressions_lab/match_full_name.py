import re

text = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

valid_names = re.findall(pattern, text)
print(' '.join(valid_names))
# valid_names = re.finditer(pattern, text)
# print(' '.join([x.group() for x in valid_names]))
