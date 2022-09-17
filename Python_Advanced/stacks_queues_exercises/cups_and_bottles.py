from collections import deque


def cups_func(cups, bottles):
    wasted_water = 0
    while cups and bottles:
        cup = cups.popleft()
        bottle = bottles.pop()
        if bottle >= cup:
            wasted_water += bottle - cup
        else:
            cups.appendleft(cup - bottle)
    if cups:
        return f"Cups: {' '.join([str(s) for s in cups])}\nWasted litters of water: {wasted_water}"
    return f"Bottles: {' '.join([str(s) for s in bottles])}\nWasted litters of water: {wasted_water}"


queue_cups = deque(map(int, input().split()))
stack_bottles = [int(x) for x in input().split()]
print(cups_func(queue_cups, stack_bottles))
