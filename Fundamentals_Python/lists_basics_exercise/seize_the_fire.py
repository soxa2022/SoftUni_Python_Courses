lst_fires = [[cell for cell in fire.split(' = ')] for fire in input().split("#")]
water = int(input())
total_fire = 0
effort = 0
print(f"Cells:")
for i in range(len(lst_fires)):
    types = lst_fires[i][0]
    value = int(lst_fires[i][1])
    if water - value < 0:
        continue
    if types == "High":
        if 81 <= value <= 125:
            water -= value
            total_fire += value
            effort += value * 0.25
            print(f" - {value}")
    elif types == "Medium":
        if 51 <= value <= 80:
            water -= value
            total_fire += value
            effort += value * 0.25
            print(f" - {value}")
    elif types == "Low":
        if 1 <= value <= 50:
            water -= value
            total_fire += value
            effort += value * 0.25
            print(f" - {value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")