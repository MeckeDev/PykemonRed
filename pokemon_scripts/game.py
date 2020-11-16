from pokemon_scripts.world import *
from pokemon_scripts.character import *


class Game:

    def __init__(self):

        # Die Auflösung des Fensters wird festgelegt
        self.screenheight = Map_H * TileSize  # Höhe des Fensters
        self.screenwidth = Map_W * TileSize  # Breite des Fensters
        # self.scale = 15

        # Das Fenster wird mit den angegeben Maßen erstellt
        self.win = pygame.display.set_mode((Map_W * TileSize, Map_H * TileSize))

        # Der Titel des Fensters wird festgelegt
        pygame.display.set_caption("Pykemon Rot by Mecke_Dev")
