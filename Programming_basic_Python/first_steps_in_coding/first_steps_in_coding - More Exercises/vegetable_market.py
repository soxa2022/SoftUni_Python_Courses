price_veg_lv = float(input())
price_fruits_lv = float(input())
veg_kg = int(input())
fruits_kg = int(input())
total_price_lv = veg_kg * price_veg_lv + fruits_kg * price_fruits_lv
total_price_eur = total_price_lv / 1.94
print(f"{total_price_eur:.2f}")
