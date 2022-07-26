import re

pattern = r"%(?P<customer>[A-Z][a-z]+)%[^\|\$\%\.]*\<(?P<product>\w+)\>[^\|\$\%\.]*\|(?P<count>\d+)\|[^\|\$\%\.]*(?P<price>(?<!\d)\d+.?\d+)\$"
total_income = 0
while True:
    command = input()
    if command == "end of shift":
        break
    valid_order = re.finditer(pattern, command)
    for data in valid_order:
        customer = data.group('customer')
        product = data.group('product')
        total_price = (int(data.group('count')) * float(data.group('price')))
        print(f"{customer}: {product} - {total_price:.2f}")
        total_income += total_price
print(f"Total income: {total_income:.2f}")
