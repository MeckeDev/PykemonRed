import json
import random


# Berechnung der XP nach einem Kampf
def fight_xp(self, target, trainer):

    # Ist das Pokemon von einem Trainer oder Wild
    if trainer:
        a = 1.5                                 # mehr XP wenn es von einem Trainer ist
    else:
        a = 1.0

    # die Basis-XP des eigenen Pokemons
    b = self.basis_xp

    # wurde das Pokemon mit einem anderem Trainer getauscht
    if self.getauscht:
        t = 1.5                                 # mehr XP wenn es mit einem anderem Trainer getauscht wurde
    else:
        t = 1

    # trägt das Pokemon ein Glücks-Ei
    if "Glücks-Ei" in self.items:
        g = 1.5                                 # mehr XP wenn es ein Glücks-Ei trägt
    else:
        g = 1

    # Level des besiegten Pokemons
    L = target.level

    # print(f"{a}*{b}*{t}*{g}*{L})//7")
    # Berechnung der XP die das Pokemon erhält
    xp = (a*b*t*g*L)//7

    # die XP werden auf die XP des Pokemon addiert
    self.xp += xp


# Berechnung der XP beim spawnen des Pokemon
def spawn_xp(level, xp_typ):

    # wenn das Pokemon XP-Typ 1 ist
    if xp_typ == 1:
        return (level ** 3) * 1.25

    # wenn das Pokemon XP-Typ 2 ist
    elif xp_typ == 2:
        return level ** 3

    # wenn das Pokemon XP-Typ 3 ist
    elif xp_typ == 3:
        return (1.2 * (level ** 3)) - (15 * (level ** 2)) + (100 * level - 140)

    # wenn das Pokemon XP-Typ 4 ist
    elif xp_typ == 4:
        return (level**3) * 0.8


# Funktion um den XP-Typ es Pokemons zu bestimmen
def xp_typen(entwicklungen):

    # öffnet die Liste der XP-Typen
    xp = open('XP-Typen.json', 'r', encoding='utf-8')
    xp_typ = json.load(xp)              # wandelt die Liste in Python um
    xp.close()

    xp1 = xp_typ["1"]                   # weist "xp1" alle Pokemon des Typs 1 zu
    xp2 = xp_typ["2"]                   # weist "xp2" alle Pokemon des Typs 2 zu
    xp3 = xp_typ["3"]                   # weist "xp3" alle Pokemon des Typs 3 zu
    xp4 = xp_typ["4"]                   # weist "xp4" alle Pokemon des Typs 4 zu

    # sucht die letzte mögliche Entwicklung des Pokemon
    for elem in entwicklungen:

        # prüft ob die letzte Entwicklung Typ 1 ist
        if elem in xp1:
            return 1

        # prüft ob die letzte Entwicklung Typ 2 ist
        if elem in xp2:
            return 2

        # prüft ob die letzte Entwicklung Typ 3 ist
        if elem in xp3:
            return 3

        # prüft ob die letzte Entwicklung Typ 4 ist
        if elem in xp4:
            return 4


# Funktion um das Geschlecht des Pokemon zu generieren
def geschlecht(self):

    # Prüft welche Geschlechter das Pokemon haben kann
    genders = self.geschlechter

    # generiert eine Zufällige Zahl
    rand_val = random.random()
    wahrscheinlichkeit = 0

    # weist dem Pokemon das Geschlecht nach Wahrscheinlichkeit zu
    for k, v in genders.items():
        wahrscheinlichkeit += v                     # die Wahrscheinlichkeit dass das Geschlecht gewählt wird

        if rand_val <= wahrscheinlichkeit/100:
            print(f"Wahrscheinlichkeit des Geschlechts: {rand_val}")    # gibt die Zufällige Zahl in der Konsole aus
            return k                                                    # weist dem Pokemon das Geschlecht zu
