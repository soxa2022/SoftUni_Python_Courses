# lst_stings = input().split(" ")
# command_input = input()
# while command_input != "3:1":
#     command = command_input.split(" ")
#     action = command[0]
#     start_index = int(command[1])
#     end_index = int(command[2])
#     if action == "merge":
#         if start_index < 0:
#             start_index = 0
#         if end_index > len(lst_stings) - 1:
#             end_index = len(lst_stings) - 1
#         lst_stings[start_index:end_index + 1] = [''.join(lst_stings[start_index:end_index + 1])]
#     elif action == "divide":
#         partitions = int(command[-1])
#         string = lst_stings[start_index]
#         new_string = []
#         parts = len(string) // partitions
#         for i in range(1, partitions + 1):
#             if i == partitions:
#                 new_string.append(string[:])
#                 string = string[:]
#             else:
#                 new_string.append(string[:parts])
#                 string = string[parts:]
#         lst_stings = lst_stings[:start_index] + new_string + lst_stings[start_index + 1:]
#     command_input = input()
# print(" ".join(lst_stings))


lst_stings = input().split(" ")
command_input = input()
while command_input != "3:1":
    command = command_input.split(" ")
    action = command[0]
    start_index = int(command[1])
    end_index = int(command[2])
    if action == "merge":
        if start_index < 0:
            start_index = 0
        if end_index > len(lst_stings) - 1:
            end_index = len(lst_stings) - 1
        lst_stings[start_index:end_index + 1] = [''.join(lst_stings[start_index:end_index + 1])]
    elif action == "divide":
        partitions = int(command[-1])
        index = int(command[1])
        string = lst_stings.pop(index)
        parts = len(string) // partitions
        begin = 0
        for char in range(1, partitions):
            lst_stings.insert(index, string[begin:begin + parts])
            index += 1
            begin += parts
        lst_stings.insert(index, string[begin:])
    command_input = input()
print(" ".join(lst_stings))
