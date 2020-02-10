import pygame
from character import *

# Das Spiel wird initialisiert
pygame.init()

# Die Auflösung des Fensters wird festgelegt
screenheight = 576                           # Höhe des Fensters
screenwidth = 640                            # Breite des Fensters

# Das Fenster wird mit den angegeben Maßen erstellt
win = pygame.display.set_mode((screenwidth, screenheight))

# Der Titel des Fensters wird festgelegt
pygame.display.set_caption("Pykemon Rot by Mecke_Dev")

# Der Character des Spielers wird erstellt
player = Character(50, 50, 32, 32, "player")

# Test-Gegner generieren
t1 = Character(150, 150, 32, 32, "t1", True, True)

# Eine Uhr wird erstellt um die FPS für die Animationen festzulegen
clock = pygame.time.Clock()


# Das Fenster wird nach einer Bewegung erneut "gezeichnet"
def redrawGameWindow():
    win.fill((0, 0, 0))                         # Füllt das Fenster mit Schwarzer Farbe
    player.draw(win)                            # Zeichnet den Character an seiner aktuellen Position
    t1.draw(win)                            # Zeichnet den Test-Gegner an seiner aktuellen Position
    pygame.display.update()                     # Zeigt uns das neu "gezeichnete" Bild an


trainers = [t1]

# Die Endlos-Schleife die das Spiel am laufen hält, bis wir es beenden
run = True
while run:

    # Hier legen wir die FPS fest, also wie oft das Bild in unserem Fenster aktualisiert werden soll
    clock.tick(16)

    # Funktion um das Spiel zu beenden wenn der Nutzer den Schließen-Knopf benutzt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t1.is_collided_with(player)

    # keys beinhaltet alle möglichen Tasten die man auf der Tastatur drücken kann
    keys = pygame.key.get_pressed()

    # Hier lernt unser Character laufen

    # Wenn der Spieler A oder Pfeil nach Links drückt, bewegt der Character sich nach Links
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.y > player.vel:
        player.y -= player.vel                  # versetzt die Position des Characters nach links
        player.left = True                      # aktiviert die Bewegung nach links    <---
        player.right = False                    # deaktiviert die Bewegung nach rechts
        player.up = False                       # deaktiviert die Bewegung nach oben
        player.down = False                     # deaktiviert die Bewegung nach unten

    # Wenn der Spieler D oder Pfeil nach Rechts drückt, bewegt der Character sich nach Links
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.y + player.width < screenwidth:
        player.y += player.vel                  # versetzt die Position des Characters nach rechts
        player.right = True                     # aktiviert die Bewegung nach rechts      <---
        player.left = False                     # deaktiviert die Bewegung nach links
        player.up = False                       # deaktiviert die Bewegung nach oben
        player.down = False                     # deaktiviert die Bewegung nach unten

    # Wenn der Spieler W oder Pfeil nach Oben drückt, bewegt der Character sich nach Oben
    elif (keys[pygame.K_w] or keys[pygame.K_UP]) and player.x - player.vel > 0:
        player.x -= player.vel                  # versetzt die Position des Characters nach oben
        player.left = False                     # deaktiviert die Bewegung nach links
        player.right = False                    # deaktiviert die Bewegung nach rechts
        player.up = True                        # aktiviert die Bewegung nach oben        <---
        player.down = False                     # deaktiviert die Bewegung nach unten

    # Wenn der Spieler S oder Pfeil nach Unten drückt, bewegt der Character sich nach Unten
    elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.x < screenheight - player.height:
        player.x += player.vel                  # versetzt die Position des Characters nach unten
        player.left = False                     # deaktiviert die Bewegung nach links
        player.right = False                    # deaktiviert die Bewegung nach rechts
        player.up = False                       # deaktiviert die Bewegung nach oben
        player.down = True                      # aktiviert die Bewegung nach unten        <---

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
