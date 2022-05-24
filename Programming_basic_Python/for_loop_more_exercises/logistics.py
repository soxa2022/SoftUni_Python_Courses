# •	До 3 тона – микробус (200 лева на тон)
# •	От 4 до 11 тона – камион (175 лева на тон)
# •	12 и повече тона – влак (120 лева на тон)
count_loads = int(input())
micro_bus = 0
truck = 0
train = 0
for i in range (1, count_loads + 1):
    weight_tons = int(input())
    if weight_tons <= 3:
        micro_bus = micro_bus + weight_tons
    elif weight_tons <= 11:
        truck = truck + weight_tons
    else:
        train = train + weight_tons
total_weight = micro_bus + truck + train
average_price = (micro_bus * 200 + truck * 175 + train * 120) / total_weight
percent_bus = micro_bus / total_weight * 100
percent_truck = truck / total_weight * 100
percent_train = train / total_weight *100
print(f"{average_price:.2f}")
print(f"{percent_bus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")
