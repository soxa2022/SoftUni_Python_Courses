import re

pattern = r">>(?P<furniture>[A-Z][A-Za-z]+)<<(?P<price>\d+.?\d+)!(?P<quantity>\d+)"

total_cost = 0
furniture = []
while True:
    command = input()
    if command == 'Purchase':
        break
    valid_furniture = re.finditer(pattern, command)
    for fur in valid_furniture:
        furniture.append(fur.group('furniture'))
        price = float(fur.group("price"))
        quantity = int(fur.group("quantity"))
        total_cost += price * quantity
    # valid_furniture = re.match(pattern, command)
    # if valid_furniture:
    # furniture.append(fur.groupdict()['furniture'])
    # price = float(fur.groupdict()["price"])
    # quantity = int(fur.groupdict()["quantity"])
    # total_cost += price * quantity

print("Bought furniture:")
if furniture:
    print('\n'.join(furniture))
print(f'Total money spend: {total_cost:.2f}')

# pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
# total_cost = 0
# bought_furniture = []
# command = input()
# while command != "Purchase":
#     match = re.search(pattern, command)
#     if match:
#         furniture, price , quantity = match.groups()
#         bought_furniture.append(furniture)
#         total_cost += int(quantity) * float(price)
#     command = input()
# print("Bought furniture:")
# for furniture in bought_furniture:
#     print(furniture)
# print(f"Total money spend: {total_cost:.2f}")