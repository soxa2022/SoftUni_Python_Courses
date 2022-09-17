from collections import deque


def supermarket():
    queue = deque()
    while True:
        customer = input()
        if customer == 'End':
            print(f"{len(queue)} people remaining.")
            break
        if customer == "Paid":
            while queue:
                print(queue.popleft())
            continue
        queue.append(customer)


supermarket()
