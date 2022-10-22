from collections import deque

orders = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]
total_pizzas = 0

while orders and employees:
    order = orders.popleft()
    employee = employees.pop()
    if order > 10 or order <= 0:
        employees.append(employee)
        continue
    if employee >= order:
        total_pizzas += order
    else:
        order -= employee
        total_pizzas += employee
        orders.appendleft(order)
if orders:
    print('Not all orders are completed.')
    print(f"Orders left: {', '.join(map(str, orders))}")
else:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {f", ".join(map(str, employees))}')
