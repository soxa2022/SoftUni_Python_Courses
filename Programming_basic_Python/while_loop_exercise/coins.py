inlet_sum = float(input())
change = inlet_sum
count_coins = 0
while change != 0.00:
    if change >= 2:
        change -= 2.00
        count_coins += 1
        continue
    if change >= 1:
        change -= 1.00
        count_coins += 1
        continue
    if change >= 0.50:
        change = round(change - 0.50, 2)
        count_coins += 1
        continue
    if change >= 0.20:
        change = round(change - 0.20, 2)
        count_coins += 1
        continue
    if change >= 0.10:
        change = round(change - 0.10, 2)
        count_coins += 1
        continue
    if change >= 0.05:
        change = round(change - 0.05, 2)
        count_coins += 1
        continue
    if change >= 0.02:
        change = round(change - 0.02, 2)
        count_coins += 1
        continue
    if change >= 0.01:
        change = round(change - 0.01, 2)
        count_coins += 1
print(count_coins)

