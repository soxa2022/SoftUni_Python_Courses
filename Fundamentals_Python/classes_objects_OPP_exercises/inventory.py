class Inventory:

    def __init__(self, count: int):
        self.items = []
        self.__capacity = count

    def add_item(self, item: str):
        if self.__capacity > len(self.items):
            self.items.append(item)

        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {Inventory.get_capacity(self) - len(self.items)}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
