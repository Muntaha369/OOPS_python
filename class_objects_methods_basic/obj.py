class Pokemon:
    def __init__(self, pokemon, type, evolution, weakness):
        self.pokemon = pokemon
        self.type = type
        self.evolution = evolution
        self.weakness = weakness

    def pokedex(self):
        print(f"{self.pokemon} is a {self.type} pokemon its evolution is {self.evolution} and its weak againts {self.weakness} type pokemon")

    def master(self, owner):
        print(f"Master of this pokemon is {owner}")

pokemon1 = Pokemon("pikachu", "electric", "raichu", "ground")
pokemon2 = Pokemon("bulbasaur", "leaf", "ivysaur", "fire")
pokemon3 = Pokemon("squirtle", "water", "waturtle", "leaf")
pokemon4 = Pokemon("charmender", "fire", "charmelion", "water")
pokemon5 = Pokemon("centepiede", "bug", "metapod", "flying")
pokemon6 = Pokemon("pidgeoto", "flying", "pidgeot", "electric")

print(pokemon1.pokemon, pokemon1.type, pokemon1.evolution, pokemon1.weakness)
print(pokemon2.pokemon, pokemon2.type, pokemon2.evolution, pokemon2.weakness)
print(pokemon3.pokemon, pokemon3.type, pokemon3.evolution, pokemon3.weakness)
print(pokemon4.pokemon, pokemon4.type, pokemon4.evolution, pokemon4.weakness)
print(pokemon5.pokemon, pokemon5.type, pokemon5.evolution, pokemon5.weakness)
print(pokemon6.pokemon, pokemon6.type, pokemon6.evolution, pokemon6.weakness)

pokemon4.pokedex()

pokemon1.master("Ash Ketchum")