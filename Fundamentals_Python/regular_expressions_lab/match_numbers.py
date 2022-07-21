# import re
#
# text = input()
# pattern = r"(^|(?<=\s))(|-)([0]|[1-9][0-9]*)(|(\.\d+))($|(?=\s))"
# valid_numbers = re.finditer(pattern, text)
# for num in valid_numbers:
#     print(num.group(), end=' ')


import re

text = input().split()

pattern = r"(^|(?<=\s))(|-)([0]|[1-9][0-9]*)(|(\.\d+))($|(?=\s))"
# pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
for num in text:
    valid_numbers = re.match(pattern, num)
    if valid_numbers:
        print(num, end=' ')
