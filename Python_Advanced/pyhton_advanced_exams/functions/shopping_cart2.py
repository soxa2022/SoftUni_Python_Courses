def shopping_cart(*args):
    products_dict = {"Soup": [], "Pizza": [], "Dessert": []}
    products = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    result = []

    for items in args:
        if items == "Stop":
            break
        meal, product = items

        if product not in products_dict[meal] and meal in products and len(products_dict[meal]) < products[meal]:
            products_dict[meal].append(product)

    for key, val in sorted(products_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f'{key}:')
        for el in sorted(val):
            result.append(f" - {el}")

    if any(products_dict.values()):
        return '\n'.join(result)
    return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
