class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        lst_products = [item for item in self.products if item[0] == first_letter]
        # lst_products = [item for item in self.products if item.startswith(first_letter)]
        return lst_products

    def __repr__(self):
        self.products.sort()
        result = f"Items in the {self.name} catalogue:\n"+'\n'.join(self.products)
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
