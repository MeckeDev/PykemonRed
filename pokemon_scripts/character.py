import pygame

# Arrays mit Einzelbildern für die Animationen

# Animation beim nach unten laufen
walkDown = [pygame.image.load('pic/player/playerF1.png'), pygame.image.load('pic/player/playerF2.png'),
            pygame.image.load('pic/player/playerF3.png'), pygame.image.load('pic/player/playerF4.png')]

# Animation beim nach oben laufen
walkUp = [pygame.image.load('pic/player/playerB1.png'), pygame.image.load('pic/player/playerB2.png'),
          pygame.image.load('pic/player/playerB3.png'), pygame.image.load('pic/player/playerB4.png')]

# Animation beim nach rechts laufen
walkRight = [pygame.image.load('pic/player/playerR1.png'), pygame.image.load('pic/player/playerR2.png'),
             pygame.image.load('pic/player/playerR3.png'), pygame.image.load('pic/player/playerR4.png')]

# Animation beim nach links laufen
walkLeft = [pygame.image.load('pic/player/playerL1.png'), pygame.image.load('pic/player/playerL2.png'),
            pygame.image.load('pic/player/playerL3.png'), pygame.image.load('pic/player/playerL4.png')]


# Die Klasse Character wird erstellt
class Character:

    # Initialisierung eines neuen Characters
    def __init__(self, x, y, width, height):

        # Character Position x und y (0, 0) ist Oben Links
        self.x = x                  # Position auf der x - Achse // Oben - Unten
        self.y = y                  # Position auf der y - Achse // Links - Rechts

        # Character Größe und Geschwindigkeit
        self.width = width          # Breite des Characters
        self.height = height        # Höhe des Characters
        self.vel = 5                # Wie schnell bewegt sich der Character

        # Character Bewegungen // zu beginn bewegen wir uns in keine Richtung
        self.right = False          # Bewegung nach Rechts
        self.left = False           # Bewegung nach Links
        self.up = False             # Bewegung nach Oben
        self.down = False           # Bewegung nach Unten
        self.walkCount = 0          # Anzahl der Schritte werden gezählt, für den Ablauf der Animation
        self.lastpos = "d"          # Lässt uns wissen in welche Richtung der Character zuletzt geschaut hat

    # Funktion um den Character zum laufen zu bringen // Animation
    def draw(self, win):

        # Wenn der Schrittzähler > als 12 ist beginnt die Animation erneut
        if self.walkCount + 1 >= 12:
            self.walkCount = 0

        # Bewegt den Character nach Links und spielt die Animation ab
        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))       # Durchläuft die Animation - nach Links
            self.lastpos = "l"                                              # setzt die letzte Blickrichtung auf Links
            self.walkCount += 1                                             # Erhöht die Schrittzahl für die Animation

        # Bewegt den Character nach Rechts und spielt die Animation ab
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))      # Durchläuft die Animation - nach Rechts
            self.lastpos = "r"                                              # setzt die letzte Blickrichtung auf Rechts
            self.walkCount += 1                                             # Erhöht die Schrittzahl für die Animation

        # Bewegt den Character nach Oben und spielt die Animation ab
        elif self.up:
            win.blit(walkUp[self.walkCount // 3], (self.x, self.y))         # Durchläuft die Animation - nach Oben
            self.lastpos = "u"                                              # setzt die letzte Blickrichtung auf Oben
            self.walkCount += 1                                             # Erhöht die Schrittzahl für die Animation

        # Bewegt den Character nach Unten und spielt die Animation ab
        elif self.down:
            win.blit(walkDown[self.walkCount // 3], (self.x, self.y))       # Durchläuft die Animation - nach Unten
            self.lastpos = "d"                                              # setzt die letzte Blickrichtung auf Unten
            self.walkCount += 1                                             # Erhöht die Schrittzahl für die Animation

        # Wenn der Charcter aufhört sich zu bewegen bleibt er stehen und blickt in die letzte Laufrichtung
        else:
            if self.lastpos == "d":
                win.blit(walkDown[0], (self.x, self.y))                     # lässt den Chacter nach unten schauen
            if self.lastpos == "u":
                win.blit(walkUp[0], (self.x, self.y))                       # lässt den Chacter nach oben schauen
            if self.lastpos == "r":
                win.blit(walkRight[0], (self.x, self.y))                    # lässt den Chacter nach rechts schauen
            if self.lastpos == "l":
                win.blit(walkLeft[0], (self.x, self.y))                     # lässt den Chacter nach links schauen
