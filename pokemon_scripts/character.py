import pygame


# Die Klasse Character wird erstellt
class Character:

    # Initialisierung eines neuen Characters
    def __init__(self, y, x, width, height, sprite, walk=False, is_trainer= False):

        self.i = 1

        # Character Position x und y (0, 0) ist Oben Links
        self.position = [y, x]
        self.y = self.position[0]                  # Position auf der x - Achse // Oben - Unten
        self.x = self.position[1]                  # Position auf der y - Achse // Links - Rechts

        # Character Größe und Geschwindigkeit
        self.width = width          # Breite des Characters
        self.height = height        # Höhe des Characters
        self.vel = 5                # Wie schnell bewegt sich der Character
        self.sprite = sprite        # Aussehen des Characters

        # Hitbox for Character
        self.hitbox = (self.x, self.y, 32, 32)

        # Character Bewegungen // zu beginn bewegen wir uns in keine Richtung
        self.right = False          # Bewegung nach Rechts
        self.left = False           # Bewegung nach Links
        self.up = False             # Bewegung nach Oben
        self.down = False           # Bewegung nach Unten
        self.walkCount = 0          # Anzahl der Schritte werden gezählt, für den Ablauf der Animation
        self.lastpos = "l"          # Lässt uns wissen in welche Richtung der Character zuletzt geschaut hat

        self.pokemon = []           # Pokemon die der Spieler bei sich trägt

        # 10 Boxen in denen der Spieler seine Pokemon lagern kann
        self.pokebox1 = []
        self.pokebox2 = []
        self.pokebox3 = []
        self.pokebox4 = []
        self.pokebox5 = []
        self.pokebox6 = []
        self.pokebox7 = []
        self.pokebox8 = []
        self.pokebox9 = []
        self.pokebox10 = []

        # Variablen die für Trainer benötigt werden die sich bewegen

        self.walk = walk
        self.end = 250
        self.path = [self.x, self.end]
        self.trainer = is_trainer

        # Flags um zu überprüfen ob Spieler bestimmte Events im Spiel getriggert hat
        self.flags = []

        # Bilder für Character und ANimation festlegen
        self.walkDown = []
        self.walkUp = []
        self.walkRight = []
        self.walkLeft = []

        self.set_sprite(sprite)
        self.img = self.walkDown[0]
        self.rect = self.img.get_rect()

    # Funktion um den Character zum laufen zu bringen // Animation
    def draw(self, win):

        # Funktion um bewegliche NPC laufen zu lassen
        if self.walk:
            self.move()
            if self.walkCount + 1 > 12:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.y, self.x))  # Durchläuft die Animation - nach Links
                self.lastpos = "r"                                               # setzt die letzte Blickrichtung auf Links
                self.walkCount += 1                                              # Erhöht die Schrittzahl für die Animation

            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.y, self.x))   # Durchläuft die Animation - nach Links
                self.lastpos = "l"                                               # setzt die letzte Blickrichtung auf Links
                self.walkCount += 1                                              # Erhöht die Schrittzahl für die Animation

            if self.trainer:
                if self.lastpos == "d":
                    self.hitbox = (self.y, self.x+32, 32, 160)
                if self.lastpos == "r":
                    self.hitbox = (self.y+32, self.x, 160, 32)
                if self.lastpos == "l":
                    self.hitbox = (self.y - 192, self.x, 192, 32)
                if self.lastpos == "u":
                    self.hitbox = (self.y, self.x-192, 32, 192)
            else:
                self.hitbox = (self.y, self.x, 32, 32)

            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        #                                                                            ###    Spieler bewegt sich    ###
        else:
            # Wenn der Schrittzähler > als 12 ist beginnt die Animation erneut
            if self.walkCount + 1 >= 12:
                self.walkCount = 0

            # Bewegt den Character nach Links und spielt die Animation ab
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.y, self.x))   # Durchläuft die Animation - nach Links
                self.lastpos = "l"                                               # setzt die letzte Blickrichtung auf Links
                self.walkCount += 1                                              # Erhöht die Schrittzahl für die Animation

            # Bewegt den Character nach Rechts und spielt die Animation ab
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.y, self.x))  # Durchläuft die Animation - nach Rechts
                self.lastpos = "r"                                               # setzt die letzte Blickrichtung auf Rechts
                self.walkCount += 1                                              # Erhöht die Schrittzahl für die Animation

            # Bewegt den Character nach Oben und spielt die Animation ab
            elif self.up:
                win.blit(self.walkUp[self.walkCount // 3], (self.y, self.x))     # Durchläuft die Animation - nach Oben
                self.lastpos = "u"                                               # setzt die letzte Blickrichtung auf Oben
                self.walkCount += 1                                              # Erhöht die Schrittzahl für die Animation

            # Bewegt den Character nach Unten und spielt die Animation ab
            elif self.down:
                win.blit(self.walkDown[self.walkCount // 3], (self.y, self.x))   # Durchläuft die Animation - nach Unten
                self.lastpos = "d"                                               # setzt die letzte Blickrichtung auf Unten
                self.walkCount += 1                                              # Erhöht die Schrittzahl für die Animation

            # Wenn der Charcter aufhört sich zu bewegen bleibt er stehen und blickt in die letzte Laufrichtung
            else:
                if self.lastpos == "d":
                    win.blit(self.walkDown[0], (self.y, self.x))                 # lässt den Chacter nach unten schauen
                if self.lastpos == "u":
                    win.blit(self.walkUp[0], (self.y, self.x))                   # lässt den Chacter nach oben schauen
                if self.lastpos == "r":
                    win.blit(self.walkRight[0], (self.y, self.x))                # lässt den Chacter nach rechts schauen
                if self.lastpos == "l":
                    win.blit(self.walkLeft[0], (self.y, self.x))                 # lässt den Chacter nach links schauen
            self.hitbox = (self.y, self.x, 32, 32)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def is_collided_with(self, p):
        # if p.hitbox[1] < self.hitbox[1] + self.hitbox[3] and p.hitbox[1] + p.hitbox[3] > self.hitbox[1]:        # Checkt Hitboxen Oben und Unten
        #    print("Battle")
        if self.lastpos == "r":
            if self.hitbox[1] < p.hitbox[1] + p.hitbox[3] and self.hitbox[1] + self.hitbox[3] > p.hitbox[1]:
                if self.hitbox[0] + self.hitbox[2] > p.hitbox[0] and self.hitbox[0] < p.hitbox[0] + p.hitbox[2]:
                    print(f"Kampf gefunden: \t{self.i}")
                    self.i += 1
        if self.lastpos == "l":
            if self.hitbox[1] < p.hitbox[1] + p.hitbox[3] and self.hitbox[1] + self.hitbox[3] > p.hitbox[1]:
                if self.hitbox[0] + self.hitbox[2] > p.hitbox[0] and self.hitbox[0] < p.hitbox[0] + p.hitbox[2]:
                    print(f"Kampf gefunden: \t{self.i}")
                    self.i += 1

    def set_sprite(self, sprite):
        # Arrays mit Einzelbildern für die Animationen für jeden Character

        #    Player   #                                                                 #   Player  #

        if sprite == "player":
            # Animation beim nach unten laufen
            self.walkDown = [pygame.image.load('pic/player/playerF1.png'),
                             pygame.image.load('pic/player/playerF2.png'),
                             pygame.image.load('pic/player/playerF3.png'),
                             pygame.image.load('pic/player/playerF4.png')]

            # Animation beim nach oben laufen
            self.walkUp = [pygame.image.load('pic/player/playerB1.png'),
                           pygame.image.load('pic/player/playerB2.png'),
                           pygame.image.load('pic/player/playerB3.png'),
                           pygame.image.load('pic/player/playerB4.png')]

            # Animation beim nach rechts laufen
            self.walkRight = [pygame.image.load('pic/player/playerR1.png'),
                              pygame.image.load('pic/player/playerR2.png'),
                              pygame.image.load('pic/player/playerR3.png'),
                              pygame.image.load('pic/player/playerR4.png')]

            # Animation beim nach links laufen
            self.walkLeft = [pygame.image.load('pic/player/playerL1.png'),
                             pygame.image.load('pic/player/playerL2.png'),
                             pygame.image.load('pic/player/playerL3.png'),
                             pygame.image.load('pic/player/playerL4.png')]

        #   Trainer 1   #                                                               #   Trainer 1   #

        if sprite == "t1":
            # Animation beim nach unten laufen
            self.walkDown = [pygame.image.load('pic/player/playerF1.png'),
                             pygame.image.load('pic/player/playerF2.png'),
                             pygame.image.load('pic/player/playerF3.png'),
                             pygame.image.load('pic/player/playerF4.png')]

            # Animation beim nach oben laufen
            self.walkUp = [pygame.image.load('pic/player/playerB1.png'),
                           pygame.image.load('pic/player/playerB2.png'),
                           pygame.image.load('pic/player/playerB3.png'),
                           pygame.image.load('pic/player/playerB4.png')]

            # Animation beim nach rechts laufen
            self.walkRight = [pygame.image.load('pic/player/playerR1.png'),
                              pygame.image.load('pic/player/playerR2.png'),
                              pygame.image.load('pic/player/playerR3.png'),
                              pygame.image.load('pic/player/playerR4.png')]

            # Animation beim nach links laufen
            self.walkLeft = [pygame.image.load('pic/player/playerL1.png'),
                             pygame.image.load('pic/player/playerL2.png'),
                             pygame.image.load('pic/player/playerL3.png'),
                             pygame.image.load('pic/player/playerL4.png')]

    def move(self):
        if self.vel > 0:
            if self.y + self.vel < self.path[1]:
                self.y += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.y - self.vel > self.path[0]:
                self.y += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
