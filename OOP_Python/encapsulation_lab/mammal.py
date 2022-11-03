class Mammal:
    __kingdom = "animals"

    def __init__(self, name: str, type_: str, sound: str):
        self.name = name
        self.type = type_
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def info(self):
        return f"{self.name} is of type {self.type}"

    def get_kingdom(self):
        return self.__kingdom
