def orders(items: str, counts: int):
    result = 0
    if items == "coffee":
        result = counts * 1.50
    elif items == "water":
        result = counts * 1
    elif items == "coke":
        result = counts * 1.40
    elif items == "snacks":
        result = counts * 2.00
    return f"{result:.2f}"


product = input()
count = int(input())
print(orders(product, count))
# total_price = orders(counts=count, items=product)
