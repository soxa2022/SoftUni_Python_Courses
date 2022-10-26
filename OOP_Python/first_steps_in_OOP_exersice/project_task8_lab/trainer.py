from first_steps_in_OOP_exersice.project_task8_lab.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
            # return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        x = [s for s in self.pokemons if s.name == pokemon_name]
        if x:
            self.pokemons.remove(x[0])
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"
    # def release_pokemon(self, pokemon_name):
    #     for s in self.pokemons:
    #         if s.name == pokemon_name:
    #             self.pokemons.remove(s)
    #             return f"You have released {pokemon_name}"
    #     return "Pokemon is not caught"

    def trainer_data(self):
        result = ''
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for s in self.pokemons:
            # result += f"- {s.pokemon_details()}\n"
            result += f"- {s.name} with health {s.health}\n"

        return result.strip()


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
