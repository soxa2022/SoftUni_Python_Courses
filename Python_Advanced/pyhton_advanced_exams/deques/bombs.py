from collections import deque

effects = deque([int(s) for s in input().split(', ')])
casings = deque([int(s) for s in input().split(', ')])
bomb_pouch = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
is_succeed = False
while effects and casings:
    if effects[0] + casings[-1] == 40:
        bomb_pouch['Datura Bombs'] += 1
        effects.popleft()
        casings.pop()
    elif effects[0] + casings[-1] == 60:
        bomb_pouch['Cherry Bombs'] += 1
        effects.popleft()
        casings.pop()
    elif effects[0] + casings[-1] == 120:
        bomb_pouch['Smoke Decoy Bombs'] += 1
        effects.popleft()
        casings.pop()
    else:
        casings[-1] -= 5
    if bomb_pouch['Datura Bombs'] >= bomb_pouch['Smoke Decoy Bombs'] >= bomb_pouch['Cherry Bombs'] >= 3:
        is_succeed = True
        break

if is_succeed:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if effects:
    print(f"Bomb Effects: {', '.join(map(str, effects))}")
else:
    print("Bomb Effects: empty")
if casings:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")
else:
    print("Bomb Casings: empty")
for key, val in sorted(bomb_pouch.items()):
    print(f"{key}: {val}")

# from collections import deque
#
# effects = deque([int(s) for s in input().split(', ')])
# casings = deque([int(s) for s in input().split(', ')])
# dat, cherry, smoke = 0, 0, 0
# is_succeed = False
# while effects and casings:
#     if effects[0] + casings[-1] == 40:
#         dat += 1
#         effects.popleft()
#         casings.pop()
#     elif effects[0] + casings[-1] == 60:
#         cherry += 1
#         effects.popleft()
#         casings.pop()
#     elif effects[0] + casings[-1] == 120:
#         smoke += 1
#         effects.popleft()
#         casings.pop()
#     else:
#         casings[-1] -= 5
#     if dat >= smoke >= cherry >= 3:
#         is_succeed = True
#         break
#
# if is_succeed:
#     print("Bene! You have successfully filled the bomb pouch!")
# else:
#     print("You don't have enough materials to fill the bomb pouch.")
# if effects:
#     print(f"Bomb Effects: {', '.join(map(str, effects))}")
# else:
#     print("Bomb Effects: empty")
# if casings:
#     print(f"Bomb Casings: {', '.join(map(str, casings))}")
# else:
#     print("Bomb Casings: empty")
# print(f"Cherry Bombs: {cherry}\nDatura Bombs: {dat}\nSmoke Decoy Bombs: {smoke}")
