def shopping_list(budget, **kwargs):
    bought_items = []
    if budget < 100:
        return "You do not have enough budget."
    for product, tuple_ in kwargs.items():
        price, quantity = tuple_
        total_price = float(price) * int(quantity)
        if budget >= total_price:
            budget -= total_price
            bought_items.append(f"You bought {product} for {total_price:.2f} leva.")
        if len(bought_items) == 5:
            return '\n'.join(bought_items)
    return '\n'.join(bought_items)