from project.product import Product


class ProductRepository:
    # products = []
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        product = self.find(product_name)
        # for product in self.products:
        if product.name == product_name:
            self.products.remove(product)

    def __repr__(self):
        result = [f"{item.name}: {item.quantity}" for item in self.products]
        return "\n".join(result)
