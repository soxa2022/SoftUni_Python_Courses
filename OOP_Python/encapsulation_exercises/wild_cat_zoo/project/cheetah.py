from project.animal import Animal


class Cheetah(Animal):
    AMOUNT_MONEY = 60

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.AMOUNT_MONEY)  # Cheetah.AMOUNT_MONEY
