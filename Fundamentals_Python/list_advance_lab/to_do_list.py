# do_list = ["0"] * 10
# input_line = input()
# while input_line != "End":
#     note = input_line.split("-")
#     idx = int(note[0]) - 1
#     to_do = note[-1]
#     do_list.pop(idx)
#     do_list.insert(idx, to_do)
#     input_line = input()
# do_list = list(filter(lambda x: x != "0", do_list))
# # do_list = [item for item in do_list if item != "0"]
# print(do_list)


do_list = list()
result = list()
input_line = input()
while input_line != "End":
    note = input_line.split("-")
    result.append(int(note[0]))
    result.sort()
    idx = result.index(int(note[0]))
    do_list.insert(idx, note[-1])
    input_line = input()
print(do_list)

# do_list = list()
# while True:
#     note = input().split("-")
#     if note[0] == "End":
#         break
#     priority = int(note[0])
#     task = note[1]
#     do_list.append((priority, task))
# sorted_list = [data[1] for data in sorted(do_list)]
# print(sorted_list)
