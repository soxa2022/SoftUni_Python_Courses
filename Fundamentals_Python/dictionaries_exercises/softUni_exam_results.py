result = {}
submission = {}
while True:
    input_line = input()
    if input_line == "exam finished":
        break
    data = input_line.split("-")
    if "banned" not in data:
        user, lang, points = data[0], data[1], int(data[2])
        if user in result:
            if result.get(user) < points:
                result[user] = points
        else:
            result[user] = points
        if lang in submission:
            submission[lang] += 1
        else:
            submission[lang] = 1
    else:
        result.pop(data[0])
print("Results:")
[print(f"{key} | {value}") for key, value in result.items()]
print("Submissions:")
[print(f"{key} - {value}") for key, value in submission.items()]