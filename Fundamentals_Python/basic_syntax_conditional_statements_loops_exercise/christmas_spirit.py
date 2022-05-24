quantity = int(input())
days = int(input())
total_cost = 0
total_spirit = 0
count_days = 0
for day in range(1, days + 1):
    count_days += 1
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += quantity * 2
        total_spirit += 5
    if day % 3 == 0:
        total_cost += quantity * 5 + quantity * 3
        total_spirit += 13
    if day % 5 == 0:
        total_cost += quantity * 15
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += 23
        if count_days == days:
            total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

# quantity = int(input())
# days = int(input())
# total_cost = 0
# total_spirit = 0
# count_days = 0
# ornament_set = 2
# tree_skirt = 5
# tree_garland = 3
# tree_lights = 15
# for day in range(1, days + 1):
#     count_days += 1
#     if day % 11 == 0:
#         quantity += 2
#     if day % 2 == 0:
#         total_cost += quantity * ornament_set
#         total_spirit += 5
#     if day % 3 == 0:
#         total_cost += quantity * (tree_skirt + tree_garland)
#         total_spirit += 13
#     if day % 5 == 0:
#         total_cost += quantity * tree_lights
#         total_spirit += 17
#         if day % 3 == 0:
#             total_spirit += 30
#     if day % 10 == 0:
#         total_spirit -= 20
#         total_cost += tree_lights + tree_skirt + tree_garland
# if days % 10 == 0:
#     total_spirit -= 30
# print(f"Total cost: {total_cost}")
# print(f"Total spirit: {total_spirit}")
