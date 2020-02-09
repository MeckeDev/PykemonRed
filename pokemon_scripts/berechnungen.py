import json
import numpy
import random


def fight_xp(self, target):

    trainer = True

    if trainer:
        a = 1.5
    else:
        a = 1.0

    b = self.basis_xp

    if self.getauscht:
        t = 1.5
    else:
        t = 1

    if "Glücks-Ei" in self.items:
        g = 1.5
    else:
        g = 1

    L = target.level

    # print(f"{a}*{b}*{t}*{g}*{L})//7")
    xp = (a*b*t*g*L)//7

    print(xp)


def spawn_xp(level, xp_typ):

    # XP-Typ 1
    if xp_typ == 1:
        return (level ** 3) * 1.25

    # XP-Typ 2
    elif xp_typ == 2:
        return level ** 3

    # XP-Typ 3
    elif xp_typ == 3:
        return (1.2 * (level ** 3)) - (15 * (level ** 2)) + (100 * level - 140)

    # XP-Typ 4
    elif xp_typ == 4:
        return (level**3) * 0.8


def xp_typen(entwicklungen):

    with open('XP-Typen.json', 'r', encoding='utf-8') as xp:
        xp_typ = json.load(xp)

        xp1 = xp_typ["1"]
        xp2 = xp_typ["2"]
        xp3 = xp_typ["3"]
        xp4 = xp_typ["4"]

        for elem in entwicklungen:

            if elem in xp1:
                return 1

            if elem in xp2:
                return 2

            if elem in xp3:
                return 3

            if elem in xp4:
                return 4


def geschlecht(self):

    genders = self.geschlechter

    rand_val = random.random()
    total = 0
    for k, v in genders.items():
        total += v
        if rand_val <= total/100:
            print(rand_val)
            return k
