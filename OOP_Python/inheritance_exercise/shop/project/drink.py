from project.product import Product


class Drink(Product):
    const_quantity = 10

    def __init__(self, name):
        super().__init__(name, self.const_quantity)

