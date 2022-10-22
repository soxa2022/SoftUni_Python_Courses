from collections import deque

elfs_energy = deque(map(int, input().split()))
materials = [int(x) for x in input().split()]
toys = 0
counter = 0
total_spent_energy = 0
while elfs_energy and materials:
    elf = elfs_energy.popleft()
    if elf < 5:
        continue
    material = materials.pop()
    counter += 1
    if counter % 3 == 0:
        if elf >= 2 * material:
            toys += 2
            elf -= 2 * material
            elfs_energy.append(elf+1)
            total_spent_energy += 2 * material
            if counter % 5 == 0:
                toys -= 2
                elfs_energy.append(elfs_energy.pop()-1)
        else:
            materials.append(material)
            elfs_energy.append(elf * 2)
    elif counter % 5 == 0:
        if elf >= material:
            elf -= material
            elfs_energy.append(elf)
            total_spent_energy += material
        else:
            materials.append(material)
            elfs_energy.append(elf * 2)
    else:
        if elf >= material:
            toys += 1
            elf -= material
            elfs_energy.append(elf+1)
            total_spent_energy += material
        else:
            materials.append(material)
            elfs_energy.append(elf * 2)
print(f"Toys: {toys}")
print(f"Energy: {total_spent_energy}")
if elfs_energy:
    print(f"Elves left: {', '.join(map(str,elfs_energy))}")
if materials:
    print(f"Boxes left: {', '.join(map(str,materials))}")
