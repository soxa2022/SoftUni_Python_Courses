from math import ceil
speed = float(input())
expense_for_100km = float(input())
distance = 2 * 384400
time = ceil(distance / speed ) + 3
fuel = (expense_for_100km * distance) / 100
print(time)
print(int(fuel))
