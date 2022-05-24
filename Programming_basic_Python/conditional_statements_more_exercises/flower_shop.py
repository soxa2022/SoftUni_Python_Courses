from math import ceil,floor
magnoli_count = int(input())
zumbul_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())
magnoli_cost = magnoli_count * 3.25
zumbul_cost = zumbul_count * 4
roses_cost = roses_count * 3.50
cactus_cost = cactus_count * 8
total_cost = roses_cost + cactus_cost + zumbul_cost + magnoli_cost
total_cost = total_cost * 0.95
diff = abs(total_cost-gift_price)
if total_cost >= gift_price :
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")

