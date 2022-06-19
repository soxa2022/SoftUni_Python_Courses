schedule_list = input().split(", ")
command_input = input()
while command_input != "course start":
    command = command_input.split(":")
    action = command[0]
    lesson = command[1]
    if action == "Add":
        if lesson not in schedule_list:
            schedule_list.append(lesson)
    elif action == "Insert":
        index = int(command[2])
        if lesson not in schedule_list:
            if 0 <= index < len(schedule_list):
                schedule_list.insert(index, lesson)
    elif action == "Remove":
        if lesson in schedule_list:
            schedule_list.remove(lesson)
            if f"{lesson}-Exercise" in schedule_list:
                schedule_list.remove(f"{lesson}-Exercise")
    elif action == "Swap":
        lesson_swap = command[2]
        if lesson in schedule_list and lesson_swap in schedule_list:
            idx = schedule_list.index(lesson)
            idx_s = schedule_list.index(lesson_swap)
            schedule_list[idx], schedule_list[idx_s] = schedule_list[idx_s], schedule_list[idx]
            if f"{lesson}-Exercise" in schedule_list and f"{lesson_swap}-Exercise" in schedule_list:
                schedule_list[idx + 1], schedule_list[idx_s + 1] = schedule_list[idx_s + 1], schedule_list[idx + 1]
            elif f"{lesson}-Exercise" in schedule_list and f"{lesson_swap}-Exercise" not in schedule_list:
                schedule_list.insert(idx_s + 1, (schedule_list.pop(idx + 1)))
            elif f"{lesson}-Exercise" not in schedule_list and f"{lesson_swap}-Exercise" in schedule_list:
                schedule_list.insert(idx + 1, (schedule_list.pop(idx_s + 1)))
    elif action == "Exercise":
        if lesson in schedule_list and f"{lesson}-Exercise" not in schedule_list:
            index = schedule_list.index(lesson)
            schedule_list.insert(index + 1, f"{lesson}-Exercise")
        elif lesson not in schedule_list:
            schedule_list.append(lesson)
            schedule_list.append(f"{lesson}-Exercise")
    command_input = input()
for i in range(len(schedule_list)):
    print(f"{i + 1}.{schedule_list[i]}")
