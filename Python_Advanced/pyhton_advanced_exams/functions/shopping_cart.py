def shopping_cart(*args):
    cart = {'Pizza': [], 'Soup': [], 'Dessert': []}
    result = []
    for element in args:
        if element == 'Stop':
            break
        meal, product = element
        if meal == 'Pizza':
            if product not in cart[meal] and len(cart[meal]) < 4:
                cart[meal].append(product)
        elif meal == 'Soup':
            if product not in cart[meal] and len(cart[meal]) < 3:
                cart[meal].append(product)
        elif meal == 'Dessert':
            if product not in cart[meal] and len(cart[meal]) < 2:
                cart[meal].append(product)
    if not cart['Pizza'] and not cart['Soup'] and not cart['Dessert']:
        return f"No products in the cart!"
    for key, val in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{key}:")
        result.extend([f' - {s}' for s in sorted(val)])
    return '\n'.join(result)