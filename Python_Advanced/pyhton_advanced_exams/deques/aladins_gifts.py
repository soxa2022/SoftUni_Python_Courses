from collections import deque


def check_product(products):
    for gift, ranges in gifts_dict.items():
        if products in range(ranges[0], ranges[1]):
            gifts_crafted[gift] += 1
            return gifts_crafted
    return gifts_crafted


gifts_dict = {'Gemstone': (100, 200),
              'Porcelain Sculpture': (200, 300),
              'Gold': (300, 400),
              'Diamond Jewellery': (400, 500)
              }
gifts_crafted = {'Gemstone': 0,
                 'Porcelain Sculpture': 0,
                 'Gold': 0,
                 'Diamond Jewellery': 0
                 }
materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

while magic_level and materials:
    material = materials.pop()
    magic = magic_level.popleft()
    product = material + magic
    if 100 <= product < 500:
        gifts_crafted = check_product(product)
    elif product < 100:
        if product % 2 == 0:
            product = 2 * material + 3 * magic
            gifts_crafted = check_product(product)
        else:
            product += product
            gifts_crafted = check_product(product)
    else:
        product //= 2
        gifts_crafted = check_product(product)

if all([gifts_crafted['Gemstone'], gifts_crafted['Porcelain Sculpture']]) \
        or all([gifts_crafted['Gold'], gifts_crafted['Diamond Jewellery']]):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(map(str,materials))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str,magic_level))}")
for key, val in sorted(gifts_crafted.items()):
    if val:
        print(f'{key}: {val}')
