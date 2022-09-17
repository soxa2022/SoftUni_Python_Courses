from collections import deque


def fast_food(line, food):
    if line:
        print(max(line))
    else:
        print(len(line))
    if sum(line) <= food:
        print("Orders complete")
    else:
        while food > line[0]:
            food -= line.popleft()
        print(f"Orders left: {' '.join([str(s) for s in line])}")


quantity = int(input())
queue = deque([int(s) for s in input().split()])
fast_food(queue, quantity)
