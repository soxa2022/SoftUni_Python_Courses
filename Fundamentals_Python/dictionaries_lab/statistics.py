products = {}
item = input()
while item != "statistics":
    # key, value = item.split(": ")
    # value = int(value)
    item = item.split(": ")
    key = item[0]
    value = int(item[-1])
    if key not in products:
        products[key] = value
    else:
        products[key] += value
    item = input()
print("Products in stock:")
# for key, value in products.items():
#     print(f"- {key}: {value}")
product = [f"- {item}: {str(products[item])}" for item in products]
print("\n".join(product))
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
