from project.animals.animal import Mammal
from project.food import Meat, Fruit, Vegetable


class Mouse(Mammal):
    @property
    def get_weight(self):
        return 0.10

    @property
    def eaten_food(self):
        return [Fruit, Vegetable]

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):

    def make_sound(self):
        return "Woof!"

    @property
    def get_weight(self):
        return 0.40

    @property
    def eaten_food(self):
        return [Meat]


class Cat(Mammal):

    def make_sound(self):
        return "Meow"

    @property
    def get_weight(self):
        return 0.30

    @property
    def eaten_food(self):
        return [Meat, Vegetable]


class Tiger(Mammal):

    def make_sound(self):
        return "ROAR!!!"

    @property
    def get_weight(self):
        return 1

    @property
    def eaten_food(self):
        return [Meat]


