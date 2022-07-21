# import re
#
# text = input()
# pattern = r"\b\d{2}([\-\.\/])[A-Z]{1}[a-z]{2}\1[0-9]{4}\b"
# for date in text.split():
#     valid_dates = re.match(pattern, date)
#     if valid_dates:
#         print(f"Day: {valid_dates.group()[0:2]}, Month: {valid_dates.group()[3:6]}, Year: {valid_dates.group()[7:]}")
# pattern = r"\b(?P<day>\d{2})([\.\-\/])(?P<month>[A-Z]{1}[a-z]{2})\2(?P<year>\d{4})\b"
# pattern = r"\b(?P<day>\d{2})(?P<sep>[\.\-\/])(?P<month>[A-Z]{1}[a-z]{2})(?P=sep)(?P<year>\d{4})\b"
# valid_date = re.finditer(pattern, text)
# for date in valid_date:
#     print(f"Day: {date.group('day')}, Month: {date.group('month')}, Year: {date.group('year')}")


import re

text = input()
pattern = r"\b(?P<day>\d{2})([\.\-\/])(?P<month>[A-Z]{1}[a-z]{2})\2(?P<year>\d{4})\b"
valid_date = re.finditer(pattern, text)
[print(f"Day: {x['day']}, Month: {x['month']}, Year: {x['year']}") for x in valid_date]
