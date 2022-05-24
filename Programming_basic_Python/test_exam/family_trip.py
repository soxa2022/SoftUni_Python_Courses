budget = float(input())
nights = int(input())
price_for_night = float(input())
percent_add_cost = int(input())
if nights > 7:
    price_for_night = price_for_night * 0.95
else:
    price_for_night = price_for_night
cost_nights = price_for_night * nights
total_cost = cost_nights + percent_add_cost * budget / 100
diff = abs(total_cost - budget)
if total_cost <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
