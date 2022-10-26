from first_steps_in_OOP_exersice.project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        exist_pokemon = [x for x in self.pokemons if x.name == pokemon_name]
        if exist_pokemon:
            self.pokemons.remove(exist_pokemon[0])
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"]
        for item in self.pokemons:
            result.append(f"- {item.pokemon_details()}")
        return "\n".join(result)

    # def release_pokemon(self, pokemon_name: str):
    #     try:
    #         exist_pokemon = next(filter(lambda x: x.name == pokemon_name, self.pokemons))
    #     except StopIteration:
    #         return "Pokemon is not caught"
    #
    #     self.pokemons.remove(exist_pokemon)
    #     return f"You have released {pokemon_name}"
    #
    # def trainer_data(self):
    #     result = [f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}"]
    #     [result.append(f"- {x.pokemon_details()}") for x in self.pokemons]
    #     return "\n".join(result)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data)
