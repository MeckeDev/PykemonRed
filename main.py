import pygame

pygame.init()


screenwidth = 144*3
screenheight = 160*3

right = False
left = False
walkCount = 0

# Character Position x and y
x, y = 20, 20

# Character Size width and height
width, height = 32, 32

# Character Speed velocity
vel = 5

win = pygame.display.set_mode((screenheight, screenwidth))

pygame.display.set_caption("Pykemon Rot by Mecke_Dev")

lastpos = "d"

walkDown = [pygame.image.load('pic/player/playerF1.png'), pygame.image.load('pic/player/playerF2.png'),
            pygame.image.load('pic/player/playerF3.png'), pygame.image.load('pic/player/playerF4.png')]

walkUp = [pygame.image.load('pic/player/playerB1.png'), pygame.image.load('pic/player/playerB2.png'),
          pygame.image.load('pic/player/playerB3.png'), pygame.image.load('pic/player/playerB4.png')]

walkRight = [pygame.image.load('pic/player/playerR1.png'), pygame.image.load('pic/player/playerR2.png'),
             pygame.image.load('pic/player/playerR3.png'), pygame.image.load('pic/player/playerR4.png')]

walkLeft = [pygame.image.load('pic/player/playerL1.png'), pygame.image.load('pic/player/playerL2.png'),
            pygame.image.load('pic/player/playerL3.png'), pygame.image.load('pic/player/playerL4.png')]

clock = pygame.time.Clock()


def redrawGameWindow():
    global walkCount
    global lastpos

    win.fill((0, 0, 0))

    if walkCount + 1 >= 12:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        lastpos = "l"
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        lastpos = "r"
        walkCount += 1
    elif up:
        win.blit(walkUp[walkCount // 3], (x, y))
        lastpos = "u"
        walkCount += 1
    elif down:
        win.blit(walkDown[walkCount // 3], (x, y))
        lastpos = "d"
        walkCount += 1

    else:
        if lastpos == "d":
            win.blit(walkDown[0], (x, y))
        if lastpos == "u":
            win.blit(walkUp[0], (x, y))
        if lastpos == "r":
            win.blit(walkRight[0], (x, y))
        if lastpos == "l":
            win.blit(walkLeft[0], (x, y))

    pygame.display.update()


# The Game
run = True
while run:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
        up = False
        down = False

    elif keys[pygame.K_RIGHT] and x < screenwidth - width:
        x += vel
        right = True
        left = False
        up = False
        down = False

    elif keys[pygame.K_UP] and y > vel:
        y -= vel
        left = False
        right = False
        up = True
        down = False

    elif keys[pygame.K_DOWN] and y < screenheight - height - vel:
        y += vel
        left = False
        right = False
        up = False
        down = True

    else:
        left = False
        right = False
        up = False
        down = False
        walkCount = 0

    redrawGameWindow()

pygame.quit()
