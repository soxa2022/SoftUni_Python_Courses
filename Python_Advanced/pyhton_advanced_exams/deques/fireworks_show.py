from collections import deque

fireworks_effects = deque([int(s) for s in input().split(', ')])
explosive_power = [int(s) for s in input().split(', ')]
palm_fireworks = 0
willow_fireworks = 0
cross_fireworks = 0
is_succeed = False
while fireworks_effects and explosive_power:
    effect = fireworks_effects.popleft()
    power = explosive_power.pop()
    if effect <= 0:
        explosive_power.append(power)
        continue
    if power <= 0:
        fireworks_effects.appendleft(effect)
        continue
    product = effect + power
    if product % 3 == 0 and product % 5 == 0:
        cross_fireworks += 1
    elif product % 3 == 0:
        palm_fireworks += 1
    elif product % 5 == 0:
        willow_fireworks += 1
    else:
        effect -= 1
        fireworks_effects.append(effect)
        explosive_power.append(power)
    if palm_fireworks >= willow_fireworks >= cross_fireworks >= 3:
        is_succeed = True
        break

if is_succeed:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    print(f"Firework Effects left: {', '.join(map(str, fireworks_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
print(
    f"Palm Fireworks: {palm_fireworks}\nWillow Fireworks: {willow_fireworks}\nCrossette Fireworks: {cross_fireworks}")
