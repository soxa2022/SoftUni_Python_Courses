lst_events = input().split('|')
energy = 100
coins = 100
is_opened = True
for event in lst_events:
    event = event.split("-")
    action = event[0]
    number = int(event[1])
    if action == "rest":
        energy += number
        gained_energy = number
        if energy > 100:
            gained_energy = number - (energy - 100)
            energy = 100
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif action == "order":
        if energy >= 30:
            coins += number
            print(f"You earned {number} coins.")
            energy -= 30
        else:
            print(f"You had to rest!")
            energy += 50
            continue
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {action}.")
        else:
            print(f"Closed! Cannot afford {action}.")
            is_opened = False
            break
if is_opened:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")