import re


def multi_line(multilines):
    while True:
        line = input()
        if line != '':
            multilines += line + '\n'
        else:
            break
    return multilines


text = ''
pattern = r"\d+"
numbers = re.findall(pattern, multi_line(text))
print(" ".join(numbers))

# lines = []
# while True:
#     line = input()
#     if line:
#         lines.append(line)
#     else:
#         break
# text = '\n'.join(lines)