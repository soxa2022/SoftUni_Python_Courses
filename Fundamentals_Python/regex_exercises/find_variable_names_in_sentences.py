import re

text = input()
pattern = r"\b[_*][A-Za-z0-9]+\b"
x = r'_([A-Za-z0-9]+)\b'
valid_names = re.findall(pattern, text)
print(','.join(s[1:] for s in valid_names))

