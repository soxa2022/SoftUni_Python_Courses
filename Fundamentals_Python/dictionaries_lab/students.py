data = input()
dict_student = {}
while not data[0].islower():
    data = data.split(":")
    key = data[-1]
    if key not in dict_student:
        dict_student[key] = [data[0] + ' - ' + data[1]]
    else:
        dict_student[key] += [data[0] + ' - ' + data[1]]
    data = input()
data = data.split("_")
for keys, value in dict_student.items():
    if keys.startswith(data[0]):
        print("\n".join(value))