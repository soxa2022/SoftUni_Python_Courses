from project.animal import Animal


class Tiger(Animal):
    AMOUNT_MONEY = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.AMOUNT_MONEY) # Tiger.AMOUNT_MONEY
