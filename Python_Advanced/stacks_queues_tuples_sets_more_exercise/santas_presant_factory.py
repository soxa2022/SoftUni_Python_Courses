from collections import deque


def present_factory(materials, magic_levels):
    present_needed_magic = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
    produce_toys = {}
    while materials and magic_levels:
        material = materials.pop()
        magic = magic_levels.popleft()
        total_magic = magic * material
        if total_magic in present_needed_magic:
            toy = present_needed_magic[total_magic]
            if toy not in produce_toys:
                produce_toys[toy] = 0
            produce_toys[toy] += 1
        if total_magic < 0:
            materials.append(magic + material)
        if total_magic not in present_needed_magic and total_magic > 0:
            materials.append(material + 15)
        if magic == 0 and material == 0:
            continue
        if magic == 0:
            materials.append(material)
        if material == 0:
            magic_levels.appendleft(magic)
    if ('Bicycle' in produce_toys and 'Teddy bear' in produce_toys) or ('Doll' in produce_toys and 'Wooden train' in produce_toys):
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")
    if materials:
        print(f"Materials left: {', '.join(map(str,materials[::-1]))}")
    if magic_levels:
        print(f"Magic left: {', '.join(map(str,magic_levels))}")
    for key, val in sorted(produce_toys.items(), key=lambda x: x[0]):
        print(f"{key}: {val}")


materials_stack = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

present_factory(materials_stack, magic_level)





from collections import deque


def present_factory(materials, magic_levels):
    present_needed_magic = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
    produce_toys = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}
    while materials and magic_levels:
        material = materials.pop()
        magic = magic_levels.popleft()
        total_magic = magic * material
        if total_magic in present_needed_magic:
            toy = present_needed_magic[total_magic]
            produce_toys[toy] += 1
        if total_magic < 0:
            materials.append(magic + material)
        if total_magic not in present_needed_magic and total_magic > 0:
            materials.append(material + 15)
        if magic == 0 and material == 0:
            continue
        if magic == 0:
            materials.append(material)
        if material == 0:
            magic_levels.appendleft(magic)
    if (produce_toys['Bicycle'] and produce_toys['Teddy bear']) or (
            produce_toys['Doll'] and produce_toys['Wooden train']):
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")
    if materials:
        print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
    if magic_levels:
        print(f"Magic left: {', '.join(map(str, magic_levels))}")
    for key, val in sorted(produce_toys.items(), key=lambda x: x[0]):
        if val:
            print(f"{key}: {val}")


materials_stack = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

present_factory(materials_stack, magic_level)

