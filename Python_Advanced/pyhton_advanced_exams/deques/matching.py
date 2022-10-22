from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0
while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue

    if males[-1] % 25 == 0 and not males[-1] == 0:
        males.pop()
        males.pop()
        continue

    if females[0] % 25 == 0 and not females[0] == 0:
        females.popleft()
        females.popleft()
        continue

    female = females.popleft()
    male = males.pop()
    if female == male:
        matches += 1
    else:
        male -= 2
        males.append(male)
print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")
