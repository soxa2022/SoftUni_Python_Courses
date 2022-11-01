from project.product import Product


class Food(Product):
    const_quantity = 15

    def __init__(self, name):
        super().__init__(name, self.const_quantity)
