def shopping_list(budget, **kwargs):
    result = []
    products = {}
    if budget < 100:
        return "You do not have enough budget."

    for key, val in kwargs.items():
        price, quantity = val
        total_sum = int(quantity) * float(price)
        if len(products) == 5:
            break
        if total_sum <= budget:
            budget -= total_sum
            if key not in products:
                products[key] = 0
            products[key] += total_sum

    for product, value in products.items():
        result.append(f'You bought {product} for {value:.2f} leva.')

    return '\n'.join(result)