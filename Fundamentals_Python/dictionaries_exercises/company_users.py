users_dict = {}
while True:
    input_line = input()
    if input_line == "End":
        break
    name, id_employee = input_line.split(" -> ")
    if name not in users_dict:
        users_dict[name] = [id_employee]
    else:
        if id_employee not in users_dict[name]:
            users_dict[name].append(id_employee)
for key, val in users_dict.items():
    print(f"{key}\n" + "-- " + "\n-- ".join(val))
