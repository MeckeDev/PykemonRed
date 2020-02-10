import pygame


TileSize = 32
Map_W = 24
Map_H = 12
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

B = "B"
W = "W"

TileColor = {
    "W": WHITE,
    "B": BLACK
}


class Map:

    def __init__(self):

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
        area = area

        if area == "test":
            self.world = [
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, B, W, W, W, W, W, W, B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, W, W, W, W, W, W, B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, B, W, W, W, B, B, B, B, B, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, B, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, B, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, B, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, B, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, B, W, W, B, B, B, B, B, B, B, W, W, B, B, B, B, B, B, B, B, B]]

        if area == "test2":
            self.world = [
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B]]
