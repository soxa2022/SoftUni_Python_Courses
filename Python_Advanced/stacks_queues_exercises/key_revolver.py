from collections import deque

price_bullet = int(input())
size_barrel = int(input())
stack_bullets = [int(s) for s in input().split()]
queue_locks = deque(map(int, input().split()))
value_int = int(input())
amount_bullets = 0
shoots = 0
while stack_bullets and queue_locks:
    bullet = stack_bullets[-1]
    lock = queue_locks[0]
    if bullet <= lock:
        stack_bullets.pop()
        queue_locks.popleft()
        amount_bullets += 1
        shoots += 1
        print("Bang!")
    else:
        stack_bullets.pop()
        amount_bullets += 1
        shoots += 1
        print('Ping!')
    if shoots == size_barrel and stack_bullets:
        shoots = 0
        print("Reloading!")
if not queue_locks:
    money_earned = value_int - (amount_bullets * price_bullet)
    print(f"{len(stack_bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(queue_locks)}")