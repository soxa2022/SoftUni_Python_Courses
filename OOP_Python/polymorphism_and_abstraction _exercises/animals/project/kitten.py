from project.cat import Cat


class Kitten(Cat):
    gender = 'Female'

    def __init__(self, name: str, age: int):
        super().__init__(name, age, Kitten.gender)

    def make_sound(self):
        return "Meow"
