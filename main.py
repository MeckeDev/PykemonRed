from pokemon_scripts.game import *
from pokemon_scripts.world import *
from pokemon_scripts.character import *

# Das Spiel wird initialisiert
pygame.init()


trainers = []

# Test-Gegner generieren
t1 = Character(150, 150, 32, 32, "t1", "Start", True, True)
trainers.append(t1)
t2 = Character(500, 200, 32, 32, "t1", "Route1", False, False)
trainers.append(t2)

# Eine Uhr wird erstellt um die FPS für die Animationen festzulegen
clock = pygame.time.Clock()

game = Game()
karte = Map("Start")

# Der Character des Spielers wird erstellt
player = Character(90, 90, 32, 32, "player", "Start")


# Das Fenster wird nach einer Bewegung erneut "gezeichnet"
def redrawGameWindow():
    for row in range(Map_H):
        for col in range(Map_W):
            pygame.draw.rect(game.win, TileColor[karte.world[row][col]], (col * TileSize, row * TileSize, TileSize, TileSize))

    player.draw(game.win)  # Zeichnet den Character an seiner aktuellen Position
    for y in trainers:
        if y.area == player.area:
            y.draw(game.win)  # Zeichnet den Test-Gegner an seiner aktuellen Position
    pygame.display.update()  # Zeigt uns das neu "gezeichnete" Bild an


redrawGameWindow()

# Die Endlos-Schleife die das Spiel am laufen hält, bis wir es beenden
run = True
while run:

    # Hier legen wir die FPS fest, also wie oft das Bild in unserem Fenster aktualisiert werden soll
    clock.tick(24)

    # Funktion um das Spiel zu beenden wenn der Nutzer den Schließen-Knopf benutzt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for x in trainers:
        x.is_collided_with(player)

    # keys beinhaltet alle möglichen Tasten die man auf der Tastatur drücken kann
    keys = pygame.key.get_pressed()

    # Hier lernt unser Character laufen

    # Wenn der Spieler A oder Pfeil nach Links drückt, bewegt der Character sich nach Links
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if karte.check_wall("left", player):
            player.y -= player.vel                  # versetzt die Position des Characters nach links
        player.left = True                      # aktiviert die Bewegung nach links    <---
        player.right = False                    # deaktiviert die Bewegung nach rechts
        player.up = False                       # deaktiviert die Bewegung nach oben
        player.down = False                     # deaktiviert die Bewegung nach unten

    # Wenn der Spieler D oder Pfeil nach Rechts drückt, bewegt der Character sich nach Links
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if karte.check_wall("right", player):
            player.y += player.vel                  # versetzt die Position des Characters nach rechts
        player.right = True                     # aktiviert die Bewegung nach rechts      <---
        player.left = False                     # deaktiviert die Bewegung nach links
        player.up = False                       # deaktiviert die Bewegung nach oben
        player.down = False                     # deaktiviert die Bewegung nach unten

    # Wenn der Spieler W oder Pfeil nach Oben drückt, bewegt der Character sich nach Oben
    elif keys[pygame.K_w] or keys[pygame.K_UP]:
        if karte.check_wall("up", player):
            player.x -= player.vel                  # versetzt die Position des Characters nach oben
        player.left = False                     # deaktiviert die Bewegung nach links
        player.right = False                    # deaktiviert die Bewegung nach rechts
        player.up = True                        # aktiviert die Bewegung nach oben        <---
        player.down = False                     # deaktiviert die Bewegung nach unten

    # Wenn der Spieler S oder Pfeil nach Unten drückt, bewegt der Character sich nach Unten
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if karte.check_wall("down", player):
            player.x += player.vel                  # versetzt die Position des Characters nach unten
        player.left = False                     # deaktiviert die Bewegung nach links
        player.right = False                    # deaktiviert die Bewegung nach rechts
        player.up = False                       # deaktiviert die Bewegung nach oben
        player.down = True                      # aktiviert die Bewegung nach unten        <---

    # ################################ DEBUG ########################### #

    elif keys[pygame.K_j]:
        player.x = 180
        player.y = 80

    elif keys[pygame.K_l]:
        player.x = 180
        player.y = 780

    elif keys[pygame.K_LALT] and keys[pygame.K_F4]:
        break

    # Wenn der Spieler keine Richtungstaste drückt, bleibt der Character stehen und schaut in die Richtung --
    # -- in die er zuletzt gelaufen ist
    else:
        player.left = False                     # deaktiviert die Bewegung nach links
        player.right = False                    # deaktiviert die Bewegung nach rechts
        player.up = False                       # deaktiviert die Bewegung nach oben
        player.down = False                     # deaktiviert die Bewegung nach unten
        player.walkCount = 0                    # setzt den Schrittzähler für die Animation wieder auf 0

    # nach jeder Bewegung wird das Fenster neu "gezeichnet" bzw. während der Bewegung wird der Character animiert
    redrawGameWindow()

# Schließt das Spiel wenn es beendet wird
pygame.quit()
