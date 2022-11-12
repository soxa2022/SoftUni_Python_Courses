from project.animals.animal import Mammal
from project.food import Meat, Fruit, Vegetable


class Mouse(Mammal):
    food_const = 0.10

    def feed(self, food):
        if not (isinstance(food, Fruit) or isinstance(food, Vegetable)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Mouse.food_const * food.quantity
        self.food_eaten += food.quantity

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    food_const = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Dog.food_const * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    food_const = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not (isinstance(food, Meat) or isinstance(food, Vegetable)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Cat.food_const * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    food_const = 1

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += Tiger.food_const * food.quantity
        self.food_eaten += food.quantity
