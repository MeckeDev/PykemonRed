import os
import json
from berechnungen import *


def cls():

    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')


class Pokemon:

    def __init__(self, num, level):

        with open('pokemon.json', 'r', encoding='utf-8') as p:
            all_pokemon = json.load(p)

        poke = all_pokemon[f"{num}"][0]

        self.nummer             = poke["Nummer"]
        self.name               = poke["Name"]
        self.typ                = poke["Typ"]
        self.schwaechen         = poke["Schwächen"]

        # Pokemon Inventar
        self.items              = []

        self.beschreibung       = poke["Beschreibung"]
        self.getauscht          = False

        self.entwicklungen      = poke["Entwicklungen"]
        self.needs              = poke["Needs"]

        self.faehigkeiten       = poke["Fähigkeiten"]
        self.geschlechter       = poke["Geschlechter"]
        self.geschlecht         = geschlecht(self)
        self.basiswerte         = poke["Basiswerte"]
        self.basis_xp           = poke["Basis-XP"]
        self.xp_typ             = xp_typen(self.entwicklungen)
        self.xp                 = spawn_xp(level, self.xp_typ)
        self.fundorte           = poke["Fundorte"]
        self.attacken           = poke["Attacken"]
        self.level              = level

        self.tms                = poke["TMs"]
        self.tps                = poke["TPs"]
        self.fangrate           = poke["Fangrate"]
        self.ei_zyklen          = poke["Ei-Zyklen"]

    def get_stats(self):

        print(f"Name\t\t: {self.name}")
        print(f"Nummer\t\t: #{self.nummer}")
        print(f"XP\t\t: {self.xp}")
        print(f"Level\t\t: {self.level}")

        y = "Typ\t\t: "
        i = 0
        while i < len(self.typ):
            y += f"{self.typ[i]}, "
            i += 1
        y = y[:-2]
        print(y)

        print(f"XP-Typ\t\t: {self.xp_typ}")
        print(f"Geschlecht\t: {self.geschlecht}")
        
        print()        
        print("Stats: ")
        print()
        
        i = 0
        for w in self.basiswerte:
            print(f"{tuple(self.basiswerte.items())[i][0]}".ljust(25, ' ') + ":" + f"{tuple(self.basiswerte.items())[i][1]}".ljust(10, ' '))
            i += 1


cls()

with open('pokemon.json', 'r', encoding='utf-8') as pokemons:
    pokes = json.load(pokemons)


while True:

    dex = input("Bitte gib die Pokedex-Nummer ein: \n0 für Ende\n")
    dex = dex.split(' ')

    cls()
    if dex == 0:
        break

    elif int(dex[0]) <= len(pokes):
        test = Pokemon(int(dex[0]), int(dex[1]))
        test.get_stats()

    else:
        print("Pokemon noch nicht im Pokedex!")
