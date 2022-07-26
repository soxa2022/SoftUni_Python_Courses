import re

text = input()
pattern_title = r"<title>(.*?)</title>"
pattern_body = r"<body>(.*?)</body>"
sub_pattern = r"(<.*?>)"
escape_pattern = r'(\\n)'
title = re.search(pattern_title, text)
body = re.search(pattern_body, text)
body = re.sub(sub_pattern, '', body.group())
title = re.sub(sub_pattern, '', title.group())
body = re.sub(escape_pattern,'', body)
print(f"Title: {title}")
print(f"Content: {body}")