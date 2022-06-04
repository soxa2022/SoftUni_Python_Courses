# lst_gifts = [gift for gift in input().split(" ")]
lst_gifts = input().split(" ")
command_input = input()
while command_input != "No Money":
    command = command_input.split(" ")
    action = command[0]
    if action == "OutOfStock":
        if command[1] in lst_gifts:
            for i in range(len(lst_gifts)):
                if lst_gifts[i] == command[1]:
                    lst_gifts[i] = "None"
    elif action == "Required":
        index = int(command[-1])
        if 0 <= index < len(lst_gifts):
            lst_gifts[index] = command[1]
    elif action == "JustInCase":
        lst_gifts.remove(lst_gifts[-1])
        lst_gifts.append(command[-1])
    command_input = input()
for i in range(len(lst_gifts)-1, -1, -1):
    if lst_gifts[i] == "None":
        lst_gifts.remove(lst_gifts[i])
# lst_gifts = [gift for gift in lst_gifts if gift != "None"]
print(" ".join(lst_gifts))
