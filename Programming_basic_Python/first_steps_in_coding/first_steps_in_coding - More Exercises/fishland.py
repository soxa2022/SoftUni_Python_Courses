price_skumria = float(input())
price_caca = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())
price_palamud = price_skumria * 1.6
price_safrid = price_caca * 1.8
total_costs = palamud_kg * price_palamud + safrid_kg * price_safrid + midi_kg * 7.50
# print(f"{total_costs:.2f}")
print("{:0.2f}".format(total_costs))