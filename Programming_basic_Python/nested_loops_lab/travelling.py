destination = input()
while destination != "End":
    budget = float(input())
    total_money = 0
    while budget > total_money:
        saved_money = float(input())
        total_money += saved_money
        if total_money >= budget:
            print(f"Going to {destination}!")
    destination = input()

