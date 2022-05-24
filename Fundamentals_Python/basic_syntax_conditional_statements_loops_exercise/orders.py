orders = int(input())
total_price = 0
for _ in range(orders):   # range(1, orders + 1)
    price_capsule = float(input())
    days = int(input())
    count_capsules = int(input())
    if 0.01 <= price_capsule <= 100 and 1 <= days <= 31 and 1 <= count_capsules <= 2000:
        order_price = price_capsule * days * count_capsules
        total_price += order_price
        print(f"The price for the coffee is: ${order_price:.2f}")
print(f"Total: ${total_price:.2f}")

# orders = int(input())
# total_price = 0
# for _ in range(orders):  # range(1, orders + 1)
#     price_capsule = float(input())
#     days = int(input())
#     count_capsules = int(input())
#     if 0.01 > price_capsule or price_capsule > 100:
#         continue
#     if 1 > days or days > 31:
#         continue
#     if 1 > count_capsules or count_capsules > 2000:
#         continue
#     order_price = price_capsule * days * count_capsules
#     total_price += order_price
#     print(f"The price for the coffee is: ${order_price:.2f}")
# print(f"Total: ${total_price:.2f}")
