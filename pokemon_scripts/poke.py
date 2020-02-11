import os
from berechnungen import *


# Funktion zum leeren der Konsole
def cls():

    # Überprüfung des Betriebssystems // Windows oder Linux
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Die Klasse Pokemon wird erstellt
class Pokemon:

    # Initialisierung eines neuen Pokemons
    def __init__(self, num, level):

        # Die Liste der Pokemon wird geöffnet
        p = open('pokemon.json', 'r', encoding='utf-8')
        all_pokemon = json.load(p)                          # Die Pokemonliste wird von Json in Python umgewandelt
        p.close()

        poke = all_pokemon[f"{num}"][0]                         # wählt das Pokemon mit der Nummer aus der Liste

        self.nummer             = poke["Nummer"]                # legt die Nummer des Pokemon fest
        self.name               = poke["Name"]                  # legt den Namen des Pokemon fest
        self.typ                = poke["Typ"]                   # legt den Typ des Pokemon fest
        self.schwaechen         = poke["Schwächen"]             # legt die Schwächen des Pokemon fest

        # Pokemon Inventar
        self.items              = []                            # beinhaltet die Items die das Pokemon trägt

        self.beschreibung       = poke["Beschreibung"]          # legt die Beschreibung des Pokemon fest
        self.getauscht          = False                         # legt fest ob das Pokemon von einem anderem Trainer ist

        self.entwicklungen      = poke["Entwicklungen"]         # legt die Entwicklungen des Pokemon fest

        # legt fest ob das Pokemon Vorraussetzungen für die Entwicklung hat // z.B. Mondstein, Donnerstein, ...
        self.needs              = poke["Needs"]

        self.faehigkeiten       = poke["Fähigkeiten"]           # legt die Fähigkeiten des Pokemon fest
        self.geschlechter       = poke["Geschlechter"]          # legt fest welche Geschlechter das Pokemon haben kann

        # legt das Geschlecht des Pokemon fest // z.B. zu 85% Männlich und zu 15% Weiblich
        self.geschlecht         = geschlecht(self)

        # legt die  KP, Angriff, Verteidigung, Spezial-Angriff, Spezial-Verteidigung, Initiative fest
        self.basiswerte         = poke["Basiswerte"]

        # Basis-XP sind bei jedem Pokemon unterschiedlich und werden zu berechnung der Erfahrung benötigt
        self.basis_xp           = poke["Basis-XP"]

        # es gibt 4 XP-Typen welche festlegen wie schnell ein Pokemon Level 100 erreicht
        self.xp_typ             = xp_typen(self.entwicklungen)

        # legt die XP beim spawnen fest, abhängig vom Level des Pokemon
        self.xp                 = spawn_xp(level, self.xp_typ)

        self.fundorte           = poke["Fundorte"]              # legt fest wo man das Pokemon finden kann
        self.attacken           = poke["Attacken"]              # legt die Attacken des Pokemon fest
        self.level              = level                         # legt das Level des Pokemon fest

        self.tms                = poke["TMs"]                   # eine Liste mit TMs die das Pokemon erlernen kann
        self.tps                = poke["TPs"]                   # eine Liste mit TPs die das Pokemon erlernen kann
        self.fangrate           = poke["Fangrate"]              # legt fest wie schwer es ist das Pokemon zu fangen

        # legt fest wie lange die Eier des Pokemons benötigen um zu schlüpfen
        self.ei_zyklen          = poke["Ei-Zyklen"]

    # Funktion um die Statistiken eines Pokemons in der Konsole auszugeben
    def get_stats(self):

        print(f"Name\t\t: {self.name}")                 # gibt den Namen des Pokemon in der Konsole aus
        print(f"Nummer\t\t: #{self.nummer}")            # gibt die Nummer des Pokemon in der Konsole aus
        print(f"XP\t\t\t: {self.xp}")                     # gibt die aktuellen XP des Pokemon in der Konsole aus
        print(f"Level\t\t: {self.level}")               # gibt ds aktuelle Level des Pokemon in der Konsole aus

        # Gibt die unterschiedlichen Typen des Pokemon aus // z.B. Feuer, Drache
        y = "Typ\t\t\t: "
        i = 0
        while i < len(self.typ):
            y += f"{self.typ[i]}, "
            i += 1
        y = y[:-2]
        print(y)
        # ##################################################################### #

        print(f"XP-Typ\t\t: {self.xp_typ}")             # gibt den XP-Typ des Pokemons in der Konsole aus
        print(f"Geschlecht\t: {self.geschlecht}")       # gibt das Geschlecht des Pokemons in der Konsole aus
        
        print()        
        print("Stats: ")
        print()
        
        i = 0

        # gibt die Basiswerte des Pokemon in der Konsole aus // KP, Angriff, Verteidigung, ...
        for w in self.basiswerte:
            print(f"{tuple(self.basiswerte.items())[i][0]}".ljust(25, ' ') + ":" +
                  f"{tuple(self.basiswerte.items())[i][1]}".ljust(10, ' '))
            i += 1

        print(fight_xp(self, dummy, False))

# leert die Konsole
cls()

# erstellt einen Dummy um die Funktion der XP-Berechnung nach einem Kampf zu testen
# in dem Bespiel wird ein Bisflor mit Level 40 generiert
dummy = Pokemon(3, 40)

# öffnet die Liste der Pokemon
pokemons = open('pokemon.json', 'r', encoding='utf-8')
pokes = json.load(pokemons)                         # wandelt die Json-Pokemon in Python um
pokemons.close()

# startet die Testkonsole, bis sie beendet wird
while True:

    # Hier kann eine Zahl aus dem Pokedex eingegeben werden
    dex = input("Bitte gib die Pokedex-Nummer ein: \n0 für Ende\n")     # fragt nach einer Nummer
    dex = int(dex)                                                      # wandelt Nummer in Zahl um

    # leert die Konsole erneut
    cls()

    # beendet den Pokedex wenn die Zahl 0 ist
    if dex == 0:
        break

    # Wenn die Zahl gültig ist werden die Statistiken zu dem Pokemon mit der eingegebenen Nummer ausgegeben
    elif int(dex) <= len(pokes):

        # erstellt ein test-Pokemon auf Level 10 mit der eingegeben Nummer aus dem Pokedex
        test = Pokemon(dex, 10)

        test.get_stats()               # gibt die Statistiken des gewählten Pokemon in der Konsole aus
        print("-"*30)                  # erstellt eine gestichelte Linie

        # zeigt die Zahl der XP die das gewählte Pokemon erhalten würde wenn es das Level 40 Bisaflor besiegt hätte
        fight_xp(test, dummy, False)

    else:
        print("Pokemon noch nicht im Pokedex!")  # Ausgabe wenn die eingegebene Zahl nicht gültig ist
