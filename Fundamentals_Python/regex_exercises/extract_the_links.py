import re

pattern = r"www\.[A-Za-z0-9-]+(\.[a-z]+){1,}"
# pattern = r"(?P<link>www\.[A-Za-z0-9-]+(\.[a-z]+){1,})"

while True:
    text = input()
    if text == '':
        break
    valid_links = re.finditer(pattern, text)
    for link in valid_links:
        print(link.group())

# import re
#
# valid_urls = []
# pattern = '((w{3})\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
# sentence = input()
# while sentence:
#     matches = re.search(pattern, sentence)
#     if matches:
#         valid_urls.append(matches.group(0))
#     sentence = input()
# for valid_url in valid_urls:
#     print(valid_url)
