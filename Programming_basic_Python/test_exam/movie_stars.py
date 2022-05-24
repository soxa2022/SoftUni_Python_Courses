budget = float(input())
actor_name = input()
is_enough = True
while actor_name != "ACTION":
    if len(actor_name) <= 15:
        salary = float(input())
    else:
        salary = budget * 0.20
    budget -= salary
    if budget < 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        is_enough = False
        break
    actor_name = input()
if is_enough:
    print(f"We are left with {budget:.2f} leva.")
