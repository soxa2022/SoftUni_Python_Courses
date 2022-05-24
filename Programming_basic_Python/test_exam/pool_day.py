import math

people = int(input())
enter_tax = float(input())
price_chair = float(input())
price_umbr = float(input())
cost_enter_tax = people * enter_tax
cost_chair = price_chair * math.ceil(people * 0.75)
cost_umbr = price_umbr * math.ceil(people / 2)
total_cost = cost_umbr + cost_chair + cost_enter_tax
print(f"{total_cost:.2f} lv.")
