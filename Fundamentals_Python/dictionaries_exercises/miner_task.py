dict_data = dict()
while True:
    data = input()
    if data == "stop":
        break
    quantity = int(input())
    # if data not in dict_data:
    #     dict_data[data] = quantity
    # else:
    #     dict_data[data] += quantity
    if data not in dict_data:
        dict_data[data] = 0
    dict_data[data] += quantity
for key, val in dict_data.items():
    print(f"{key} -> {val}")