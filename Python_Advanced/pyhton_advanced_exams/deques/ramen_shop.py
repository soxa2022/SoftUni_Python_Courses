from collections import deque

bowls = [int(s) for s in input().split(', ')]
customers = deque([int(s) for s in input().split(', ')])
while bowls and customers:
    bowl = bowls.pop()
    customer = customers.popleft()
    if customer > bowl:
        customers.appendleft(customer - bowl)
    elif customer < bowl:
        bowls.append(bowl - customer)
if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(map(str, bowls))}")
elif not bowls:
    print("Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(map(str, customers))}")
