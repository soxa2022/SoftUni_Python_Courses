courses_dict = {}
while True:
    input_line = input()
    if input_line == 'end':
        break
    course, student = input_line.split(" : ")
    if course not in courses_dict:
        courses_dict[course] = []
        courses_dict[course].append(student)
    else:
        courses_dict[course].append(student)
for key, val in courses_dict.items():
    print(f"{key}: {len(val)}\n" + "-- " + "\n-- ".join(val))