junk_dict = {}
legend_dict = {"shards": 0, "fragments": 0, "motes": 0}
winner_dict = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
is_over = False
while not is_over:
    data = input().split(" ")
    for idx in range(0, len(data), 2):
        key = data[idx + 1].lower()
        val = int(data[idx])
        if key not in legend_dict:
            if key not in junk_dict:
                junk_dict[key] = 0
            junk_dict[key] += val
        else:
            legend_dict[key] += val
            if legend_dict[key] >= 250:
                legend_dict[key] -= 250
                is_over = True
                print(f"{winner_dict[key]} obtained!")
                break
    if is_over:
        break
[print(f"{key}: {value}") for key, value in legend_dict.items()]
for key, val in junk_dict.items():
    print(f"{key}: {val}")