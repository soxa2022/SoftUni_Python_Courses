from project.animals.animal import Bird
from project.food import Meat, Fruit, Vegetable, Seed


class Owl(Bird):

    @property
    def get_weight(self):
        return 0.25

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def eaten_food(self):
        return [Meat]


class Hen(Bird):
    @property
    def get_weight(self):
        return 0.35

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def eaten_food(self):
        return [Meat, Fruit, Vegetable, Seed]
