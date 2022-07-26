import re

pattern = r"(?P<name>[A-Za-z])|(?P<distance>[0-9])"
participants = {key: 0 for key in (input().split(", "))}

while True:
    name = ''
    distance = 0
    command = input()
    if command == "end of race":
        break
    info = re.finditer(pattern, command)
    for text in info:
        if not text.group("name") is None:
            name += text.group("name")
        if not text.group("distance") is None:
            distance += int(text.group("distance"))
    if name in participants:
        participants[name] += distance
sorted_participants = list(sorted(participants.items(), key=lambda x: -x[1]))
rank = ['1st', '2nd', '3rd']
for key in range(3):
    print(f"{rank[key]} place: {sorted_participants[key][0]}")
