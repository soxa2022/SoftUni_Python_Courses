from math import ceil,floor
area_grape = int(input())
grapes_kg = float(input())
wine_lt = int(input())
workers = int(input())
area_for_wine = area_grape * 0.4
wine = (area_for_wine * grapes_kg ) /2.5
diff = abs(wine - wine_lt)
if wine < wine_lt :
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(diff / workers)} liters per person.")
