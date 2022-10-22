from collections import deque

milligrams = [int(x) for x in input().split(', ')]
drinks = deque([int(x) for x in input().split(", ")])
total_caffeine = 0

while milligrams and drinks:
    milligram = milligrams.pop()
    drink = drinks.popleft()

    current_caffeine = milligram * drink

    if current_caffeine + total_caffeine <= 300:
        total_caffeine += current_caffeine

    elif current_caffeine + total_caffeine > 300:
        drinks.append(drink)
        if total_caffeine - 30 < 0:
            total_caffeine = 0
        else:
            total_caffeine -= 30
if drinks:
    print(f"Drinks left: {', '.join(map(str, drinks))}")

else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
