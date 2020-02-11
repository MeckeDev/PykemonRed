import pygame
import game

TileSize = 32
# Map_W = 29
Map_W = 24
Map_H = 12
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TELEPORT = (255, 40, 40)
Route1 = (255, 40, 40)
VertaniaCity = (255, 40, 40)

B = "B"
W = "W"
T = "T"
R1 = "R1"
VC = "VC"

TileColor = {
    "W": WHITE,
    "B": BLACK,
    "T": TELEPORT,
    "R1": Route1,
    "VC": VertaniaCity
}


class Map:

    def __init__(self):

        self.area = "test"

        self.can_walk = ["W", "T"]
        self.is_teleport = ["R1", "VC"]

        self.world = [
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, W, W, W, W, W, W, B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
            [B, B, W, W, W, W, W, W, B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W, W, W, B, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W, W, W, B, W, W, W, W, W, W, W, W, W, W],
            [W, W, W, W, W, W, W, W, W, W, W, W, W, B, W, W, W, W, W, W, W, W, W, W],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
            [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B]]

    def set_area(self, area):

        self.area = area

        if area == "test":
            self.world = [
                [B, B, W, W, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, B, W, W, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, B, W, W, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [VC, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [R1, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, B, W, W, W, B, B, B, B, B, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, W, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, W, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, W, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, W, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B]]

        if area == "test2":
            self.world = [
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, R1],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [VC, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B]]

        '''
        if area == "py":
            self.world = [
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [W, W, R, R, R, W, R, W, R, W, R, R, R, W, R, W, R, W, R, R, R, W, R, W, W, W, R, W, B],
                [W, W, R, W, R, W, R, W, R, W, W, R, W, W, R, W, R, W, R, W, R, W, R, W, W, W, R, W, B],
                [B, W, R, R, R, W, R, R, R, W, W, R, W, W, R, W, R, W, R, W, R, W, R, R, W, W, R, W, B],
                [B, W, R, W, W, W, W, W, R, W, W, R, W, W, R, R, R, W, R, W, R, W, R, W, R, W, R, W, B],
                [B, W, R, W, W, W, W, W, R, W, W, R, W, W, R, W, R, W, R, W, R, W, R, W, W, R, R, W, B],
                [B, W, R, W, W, W, W, W, R, W, W, R, W, W, R, W, R, W, R, W, R, W, R, W, W, W, R, W, B],
                [B, W, R, W, W, W, W, W, R, W, W, R, W, W, R, W, R, W, R, R, R, W, R, W, W, W, R, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B]]
        '''

    def teleport(self, player, gebiet, ziel):

        self.set_area(gebiet)

        i = 0
        for elem in self.world:
            if ziel in self.world[i]:
                player.x = i*10
                player.y = self.world[i].index(ziel)
            i += 1

    def check_wall_left(self, char):

        vel = char.vel
        h0 = char.hitbox[0]
        h1 = char.hitbox[1]
        h2 = char.hitbox[2]
        h3 = char.hitbox[3]

        map0 = self[0]
        map1 = self[1]

        self.world = [map0, map1]

        '''
        print(
            f"{h0} .. {h1} ... {h0 + h2} .... {h1 + h3}")
        if karte.world[(self.x // self.width) + 1][(self.y - self.vel) // self.width] in karte.can_walk:
            if karte.world[(self.x // self.width) + 1][self.y // self.width] in karte.is_teleport:
                karte.teleport(player, "test2",
                               karte.world[(self.x // self.width) + 1][((self.y + self.vel) // self.width)])
        '''
