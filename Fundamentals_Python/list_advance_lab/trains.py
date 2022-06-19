number_wagons = int(input())
lst_wagons = [0 for wagon in range(number_wagons)]
command_line = input()

while command_line != "End":
    command = command_line.split(" ")
    action = command[0]
    people = int(command[-1])
    idx = int(command[1])
    if action == "add":
        lst_wagons[-1] += people
    elif action == "insert":
        lst_wagons[idx] += people
    elif action == "leave":
        lst_wagons[idx] -= people
    command_line = input()
print(lst_wagons)