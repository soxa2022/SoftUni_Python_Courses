from collections import deque

orders = deque([int(s) for s in input().split(', ')])
employees = [int(s) for s in input().split(', ')]
total_pizza = 0
while orders and employees:
    order = orders.popleft()
    employee = employees.pop()
    if order > 10 or order < 1:
        employees.append(employee)
        continue
    if order <= employee:
        total_pizza += order
    else:
        left_pizza = order - employee
        total_pizza += employee
        orders.appendleft(left_pizza)
if orders:
    print(f'Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str,orders))}')
else:
    print(f'All orders are successfully completed!')
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join(map(str,employees))}")




