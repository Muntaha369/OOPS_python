#Nested classes --> class inside a class

class Trainer:
    class Pokemon:
        def __init__(self, pokemon, type, evolution):
            self.pokemon = pokemon
            self.type = type
            self.evolution = evolution

        def list_detail(self):
            print(f"{self.pokemon} is an {self.type} pokemon")
            
    def __init__(self, trainer):
        self.trainer = trainer
        self.pokemon = []

    def add_pokemon(self, pokemon, type, evolution):
        new_pokemon = self.Pokemon(pokemon, type, evolution)
        self.pokemon.append(new_pokemon)

    def list_pokemon(self):
        for pokemon in self.pokemon:
            pokemon.list_detail()

trainer1 = Trainer("Ash")
trainer2 = Trainer("Garry")

trainer1.add_pokemon("Pikachu", "Electric", "Raichu")
trainer1.add_pokemon("Pidgeoto", "Fly", "Pidgeot")
trainer1.add_pokemon("Charmender", "Fire", "Charmelion")
trainer2.add_pokemon("Squirtle", "Water", "Waturtle")
trainer2.add_pokemon("Krabby", "Water", "Kingler")

trainer1.list_pokemon()
print('\n')
trainer2.list_pokemon()