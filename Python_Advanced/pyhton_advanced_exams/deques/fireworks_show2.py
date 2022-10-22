from collections import deque

effects = deque([int(x) for x in input().split(', ')])
powers = [int(x) for x in input().split(', ')]
fireworks = {'Palm': 0,
             'Willow': 0,
             'Crossette': 0,
             }

while effects and powers:
    if effects[0] <= 0:
        effects.popleft()
        continue
    if powers[-1] <= 0:
        powers.pop()
        continue
    effect = effects.popleft()
    power = powers.pop()
    value = effect + power
    if value % 5 == 0 and not value % 3 == 0:
        fireworks["Willow"] += 1
    elif value % 3 == 0 and not value % 5 == 0:
        fireworks["Palm"] += 1
    elif value % 5 == 0 and value % 3 == 0:
        fireworks["Crossette"] += 1
    else:
        effects.append(effect - 1)
        powers.append(power)

    if all([True if x >= 3 else False for x in fireworks.values()]):
        print('Congrats! You made the perfect firework show!')
        break
if any([True if x < 3 else False for x in fireworks.values()]):
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")
if powers:
    print(f"Explosive Power left: {', '.join(map(str, powers))}")

for key, value in fireworks.items():
    print(f"{key} Fireworks: {value}")
