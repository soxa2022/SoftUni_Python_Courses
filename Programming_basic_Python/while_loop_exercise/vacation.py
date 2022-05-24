needed_money = float(input())
account_money = float(input())
total_money = account_money
day_counter = 0
total_days = 0
failed = False
while total_money < needed_money:
    total_days += 1
    action = input()
    money_for_action = float(input())
    if action == "save":
        day_counter = 0
        total_money = total_money + money_for_action
    elif action == "spend":
        day_counter += 1
        total_money = total_money - money_for_action
        if total_money < 0:
            total_money = 0
    if day_counter == 5:
        failed = True
        break
if failed:
    print("You can't save the money.")
    print(total_days)
else:
    print(f"You saved the money for {total_days} days.")



