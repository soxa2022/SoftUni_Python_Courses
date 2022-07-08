dict_sides = {}
while True:
    data_input = input()
    if data_input == "Lumpawaroo":
        break
    if "|" in data_input:
        side, name = data_input.split(" | ")
        if any(name in value for value in dict_sides.values()) is False:
            if side not in dict_sides:
                dict_sides[side] = [name]
            else:
                dict_sides[side].append(name)
    elif "->" in data_input:
        name, side = data_input.split(" -> ")
        for k, v in dict_sides.items():
            if name in v:
                v.remove(name)
                break
        if side not in dict_sides:
            dict_sides[side] = [name]
            print(f"{name} joins the {side} side!")
        elif side in dict_sides and name not in dict_sides[side]:
            dict_sides[side].append(name)
            print(f"{name} joins the {side} side!")
for key, val in dict_sides.items():
    if len(val):  # len(val) > 0:
        # print(f"Side: {key}, Members: {len(val)}\n" + "! " + "\n! ".join(val))
        print(f"Side: {key}, Members: {len(val)}")
        [print(f"! {user}") for user in val]
