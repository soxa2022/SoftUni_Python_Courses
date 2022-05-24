age = int(input())
price_machine = float(input())
price_toy = int(input())

saved_money = 0
toy = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        saved_money = saved_money + i / 2 * 10
        saved_money = saved_money - 1
    if i % 2 != 0:
        toy += 1
saved_money = saved_money + toy * price_toy
diff = abs(saved_money - price_machine)
if saved_money >= price_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
