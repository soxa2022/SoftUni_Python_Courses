projection = input()
rows = int(input())
columns = int(input())
price = 0
if projection == "Premiere":
    price = 12
elif projection == "Normal":
    price = 7.50
elif projection == "Discount":
    price = 5.00
total_price = price * columns * rows
print(f"{total_price:.2f} leva")

