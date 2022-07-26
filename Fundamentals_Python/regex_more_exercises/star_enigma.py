import re


def count_char(strings):
    new_string = ''
    a = r"[star]"
    x = re.findall(a, strings, flags=re.IGNORECASE)
    counter = len(x)
    for ch in strings:
        new_string += chr(ord(ch) - counter)
    return new_string


number = int(input())
pattern = r"@(?P<planet>[A-za-z]+)[^@\-\!\:\>]*:(?P<population>\d+)[^@\-\!\:\>]*!(?P<types>A|D)![^@\-\!\:\>]*->(?P<soldiers>\d+)"
attacks = []
destroy = []
for _ in range(number):
    command = input()
    info = re.finditer(pattern, count_char(command))

    for data in info:
        if data.group("types") == "A":
            attacks.append(data.group("planet"))
        elif data.group("types") == "D":
            destroy.append(data.group("planet"))
a = "/n" + '->'
print(f"Attacked planets: {len(attacks)}")
attacks.sort()
[print(f"-> {i}") for i in attacks]
print(f"Destroyed planets: {len(destroy)}")
destroy.sort()
[print(f"-> {i}") for i in destroy]
