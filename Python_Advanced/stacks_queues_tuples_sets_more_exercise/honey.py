from collections import deque

ops = {"+": lambda a, b: a + b,
       "-": lambda a, b: a - b,
       "*": lambda a, b: a * b,
       "/": lambda a, b: a / b,
       }


def honey(bees_seq, nectar_seq, symbols):
    honey_collect = 0
    while bees_seq and nectar_seq:
        bee = bees_seq.popleft()
        nectar = nectar_seq.pop()

        if nectar < bee:
            bees_seq.appendleft(bee)
        else:
            symbol = symbols.popleft()
            if not nectar == 0:
                honey_collect += abs(ops[symbol](bee, nectar))

    return honey_collect


working_bees = deque([int(s) for s in input().split()])
stack_nectar = [int(x) for x in input().split()]
symbols_queued = deque([x for x in input().split()])

print(f'Total honey made: {honey(working_bees, stack_nectar, symbols_queued)}')
if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}")
if stack_nectar:
    print(f"Nectar left: {', '.join(map(str, stack_nectar))}")