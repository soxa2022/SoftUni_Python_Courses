import re

text = input()
pattern = r'\+359( |-)2\1[0-9]{3}\1[0-9]{4}\b'
# pattern = r"(\+359 2 [0-9]{3} [0-9]{4})\b|(\+359-2-[0-9]{3}-[0-9]{4})\b"
valid_numbers = re.finditer(pattern, text)
print(", ".join([s.group() for s in valid_numbers]))
