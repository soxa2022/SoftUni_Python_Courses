info_dict = {}
info_lst = []
while True:
    info = input()
    if info == "buy":
        break
    name, price, quantity = info.split()
    info_lst = [float(price), int(quantity)]
    if name not in info_dict:
        info_dict[name] = info_lst
    else:
        info_dict[name][1] += info_lst[1]
        info_dict[name][0] = info_lst[0]
# [print(f"{key} -> {(value[1]*value[0]):.2f}") for key, value in info_dict.items()]
for key, val in info_dict.items():
    print(f"{key} -> {(val[1] * val[0]):.2f}")