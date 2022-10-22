from collections import deque

males = [int(s) for s in input().split()]
females = deque(int(s) for s in input().split())
total_matches  = 0

while males and females:
    male = males.pop()
    female = females.popleft()

    if male <= 0:
        females.appendleft(female)
        continue

    if female <= 0:
        males.append(male)
        continue

    if female % 25 == 0:
        males.append(male)
        females.popleft()
        continue

    if male % 25 == 0:
        females.appendleft(female)
        males.pop()
        continue

    if not male == female:
        males.append(male-2)

    else:
        total_matches += 1

print(f"Matches: {total_matches}")
if males:
    print(f"Males left: {', '.join(map(str,males[::-1]))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")