class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, milliliters):
        if self.left_milliliters() >= milliliters:
            self.quantity += milliliters

    def status(self):
        return self.left_milliliters()

    def left_milliliters(self):
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
