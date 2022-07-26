import re

text = input()
pattern = r"\b(^|(?<=\s))[A-Za-z0-9][A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Z.|a-z.]{2,}\b"
valid_emails = re.finditer(pattern, text)
[print(mail.group()) for mail in valid_emails]

# import re
#
# some_string = input()
# pattern = r'(?<=\s)(([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'
# matches = re.findall(pattern, some_string)
# for match in matches:
#     print(match[0])