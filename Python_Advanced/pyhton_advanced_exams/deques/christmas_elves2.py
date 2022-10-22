from collections import deque

elfs = deque(int(x) for x in input().split())
materials = [int(x) for x in input().split()]

used_energy = 0
toys = 0
counter = 0

while elfs and materials:

    elf = elfs.popleft()
    material = materials.pop()

    if elf < 5:
        materials.append(material)
        continue

    counter += 1
    if elf >= material:

        if counter % 3 == 0:
            if elf >= material * 2:
                elf = elf - 2 * material + 1
                toys += 2
                used_energy += 2 * material
                if counter % 5 == 0:
                    toys -= 2
                    elf -= 1
                elfs.append(elf)
            else:
                materials.append(material)
                elfs.append(elf * 2)

        elif counter % 5 == 0:
            elf = elf - material
            used_energy += material
            elfs.append(elf)

        else:
            elf = elf - material + 1
            toys += 1
            used_energy += material
            elfs.append(elf)
    else:
        materials.append(material)
        elfs.append(elf * 2)

print(f"Toys: {toys}")
print(f"Energy: {used_energy}")
if elfs:
    print(f"Elves left: {', '.join(map(str, elfs))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")
