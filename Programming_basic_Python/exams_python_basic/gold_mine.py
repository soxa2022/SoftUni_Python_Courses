location = int(input())
for place in range(location):
    expect_gold_per_day = float(input())
    days = int(input())
    total_gold = 0
    average_gold = 0
    for number in range(days):
        gold_per_day = float(input())
        total_gold += gold_per_day
    average_gold = total_gold / days
    if average_gold >= expect_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    else:
        diff = abs(expect_gold_per_day - average_gold)
        print(f"You need {diff:.2f} gold.")
