class Person:
    species = "mammal"

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.species = "mammal"

    def get_info(self):
        if self.first_name == "Ivan":
            self.first_name = "IvaN"
        return f"{self.first_name} {self.last_name}, {self.age} years old"


person = Person("Kiril", "Ivanov", 25)
person_two = Person("Ivan", "Ivanov", 44)
print(person.get_info())
print(person_two.get_info())
