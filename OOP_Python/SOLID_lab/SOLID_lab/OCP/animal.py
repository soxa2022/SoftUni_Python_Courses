import abc


class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return "meow"


class Dog(Animal):

    def make_sound(self):
        return "woof-woof"


class Chicken(Animal):

    def make_sound(self):
        return "pi-pi"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
