import re

names = input()
demons = {}
x = r", *"
pattern_health = r"[^\d\+\-\*\/\.]"
pattern_damage = r"\-?\d*\.?\d*"
op_pattern = r"[\*/]"
list_demons = [line.strip() for line in re.split(x, names)]
for name in list_demons:
    lst_health = re.findall(pattern_health, name)
    lst_damage = re.findall(pattern_damage, name)
    lst_signs = re.findall(op_pattern, name)
    damage = sum([float(x) for x in lst_damage if not x == ''])
    health = sum([ord(s) for s in lst_health])
    damage *= 2 ** lst_signs.count('*')
    damage /= 2 ** lst_signs.count("/")
    demons[name] = [health, damage]
for key, value in sorted(demons.items()):
    print(f"{key} - {value[0]} health, {value[1]:.2f} damage")