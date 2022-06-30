class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        self.__animals += 1
        # Zoo.__animals += 1
        if species == "mammal":
            zoo.mammals.append(name)
        elif species == "bird":
            zoo.birds.append(name)
        elif species == "fish":
            zoo.fishes.append(name)

    # def get_info(self, species):
    #     if species == "mammal":
    #         return f"{species.capitalize()}s in {self.name}: {', '.join(zoo.mammals)}\nTotal animals: {self.__animals}"
    #     elif species == "bird":
    #         return f"{species.capitalize()}s in {self.name}: {', '.join(zoo.birds)}\nTotal animals: {self.__animals}"
    #     elif species == "fish":
    #         return f"{species.capitalize()}es in {self.name}: {', '.join(zoo.fishes)}\nTotal animals: {self.__animals}"
    def get_info(self, species):
        animal_names = None
        result = ""
        if species == "mammal":
            animal_names = self.mammals
            result = "Mammals"
        elif species == "bird":
            animal_names = self.birds
            result = "Birds"
        elif species == "fish":
            animal_names = self.fishes
            result = "Fishes"
        animal_data = ', '.join(animal_names)
        return f"""{result} in {self.name}: {animal_data}
Total animals: {self.__animals}"""


names = input()
count_animals = int(input())
zoo = Zoo(names)
for i in range(count_animals):
    animals = input().split(" ")
    species = animals[0]
    animal = animals[1]
    zoo.add_animals(species, animal)
types = input()
print(zoo.get_info(types))
