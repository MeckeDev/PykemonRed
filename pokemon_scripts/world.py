
TileSize = 40
# Map_W = 29
Map_W = 24
Map_H = 12
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 40, 40)
Start = (255, 40, 40)
Route1 = (255, 40, 40)
VertaniaCity = (255, 40, 40)

B = "B"
W = "W"
R = "R"
R1 = "R1"
VC = "VC"
S = "Start"

TileColor = {
    "W": WHITE,
    "B": BLACK,
    "R": RED,
    "R1": Route1,
    "S": Start,
    "VC": VertaniaCity
}

Places = {
    "R1": "Route1",
    "S": "Start",
    "VC": "VertaniaCity"
}


class Map:

    def __init__(self, start):

        self.area = start

        self.can_walk = ["W", "T"]
        self.is_teleport = ["R1", "VC", "S"]

        for elem in self.is_teleport:
            self.can_walk.append(elem)

        self.world = [[]]

        self.set_area(start)

    def teleport(self, player, ziel):

        for short, long in Places.items():
            print(f"Short: {short}, Long: {long}")
            if short == ziel:
                ziel = long
                z = short

        for short, long in Places.items():
            if long == player.area:
                area = long
                a = short

        player.area = ziel
        print("Ziel: " + ziel)
        self.set_area(ziel)

        i = 0
        for elem in self.world:
            print(f"Elem: {elem} Ziel: {area}")
            if area in elem:
                player.x = i*10
                player.y = elem.index(area)

                print(f"x = {player.x} y = {player.y}")
            i += 1

    def check_wall(self, direction, char):

        p_top_left = 0
        p_down_left = 0
        p_top_right = 0
        p_down_right = 0
        p_left_up = 0
        p_right_up = 0
        p_left_down = 0
        p_right_down = 0

        vel = char.vel
        h0 = char.hitbox[0]
        h1 = char.hitbox[1]
        h2 = char.hitbox[2]
        h3 = char.hitbox[3]

        char.mid = self.world[round(((h1 + char.height/2) // TileSize))][round((h0 + char.width/2) // TileSize)]

        # self.world[2][4]  # [von oben nach unten][von links nach rechts]

        p_top_left = self.world[round((h1 // TileSize))][round((h0 - char.vel) // TileSize)]
        p_down_left = self.world[round(((h1 + h2)//TileSize))][round((h0 - char.vel)//TileSize)]

        p_top_right = self.world[round((h1 // TileSize))][round((h0 + h2 + char.vel) // TileSize)]
        p_down_right = self.world[round(((h1 + h3)//TileSize))][round((h0 + h2 + char.vel)//TileSize)]

        p_left_up = self.world[round(((h1 - char.vel)//TileSize))][round(h0 // TileSize)]
        p_right_up = self.world[round(((h1 - char.vel)//TileSize))][round((h0 + h2)//TileSize)]

        while True:
            try:
                p_left_down = self.world[round(((h1 + h3 + char.vel)//TileSize))][round(h0//TileSize)]
                p_right_down = self.world[round(((h1 + h3 + char.vel)//TileSize))][round((h0 + h2+1)//TileSize)]
                break
            except IndexError as e:
                break

        if direction == "left":
            if p_top_left in self.can_walk and p_down_left in self.can_walk and char.y - char.vel > 0:
                if char.mid in self.is_teleport:
                    self.teleport(char, char.mid)
                return True

        if direction == "right":
            if p_top_right in self.can_walk and p_down_right in self.can_walk and char.y + char.vel < Map_W*TileSize:
                if char.mid in self.is_teleport:
                    self.teleport(char, char.mid)
                return True

        if direction == "up":
            if p_left_up in self.can_walk and p_right_up in self.can_walk and char.x - char.vel > 0:
                if char.mid in self.is_teleport:
                    self.teleport(char, char.mid)
                return True

        if direction == "down":
            if p_left_down in self.can_walk and p_right_down in self.can_walk and char.x + char.vel < Map_H*TileSize:
                if char.mid in self.is_teleport:
                    self.teleport(char, char.mid)
                return True

    def set_area(self, area):

        self.area = area

        if self.area == "Start":
            self.world = [
                [B, B, W, VC, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, B, W, W, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, B, W, W, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, B, W, W, W, B, B, B, B, B, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, W, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, W, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, W, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, W, B, B, B, B, W, B, B, W, W, W, B, B, B, B, B, B, B, B],
                [B, B, B, W, W, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B]]

        if self.area == "VertaniaCity":
            self.world = [
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, R1],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [S, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B]]

        if self.area == "Route1":
            self.world = [
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [W, W, R, R, R, W, R, W, R, W, R, R, R, W, R, W, R, W, R, R, R, W, R, W, W, W, R, W, B],
                [W, W, R, W, R, W, R, W, R, W, W, R, W, W, R, W, R, W, R, W, R, W, R, W, W, W, R, W, B],
                [B, W, R, R, R, W, R, R, R, W, W, R, W, W, R, W, R, W, R, W, R, W, R, R, W, W, R, W, B],
                [VC, W, R, W, W, W, W, W, R, W, W, R, W, W, R, R, R, W, R, W, R, W, R, W, R, W, R, W, B],
                [B, W, R, W, W, W, W, W, R, W, W, R, W, W, R, W, R, W, R, W, R, W, R, W, W, R, R, W, B],
                [B, W, R, W, W, W, W, W, R, W, W, R, W, W, R, W, R, W, R, W, R, W, R, W, W, W, R, W, B],
                [B, W, R, W, W, W, W, W, R, W, W, R, W, W, R, W, R, W, R, R, R, W, R, W, W, W, R, W, B],
                [B, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, W, B],
                [B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B]]