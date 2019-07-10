from GameEntities.Cannon import Cannonball
from GameEntities.AlienGun import AlienGun
from gamestats import Stats
import pygame


class Cover:
    size = Stats.WIDTH / 40

    def __init__(self, x, y):
        self.bags = []
        self.coor = [x, y]
        for i in range(2):
            self.bags.append(list())
            for j in range(4):
                self.bags[i].append(1)
        self.bags.append(list())
        self.bags[2].append(1)
        self.bags[2].append(0)
        self.bags[2].append(0)
        self.bags[2].append(1)

    def draw(self, screen, ball, gun):
        res = ball
        resG = gun
        for i in range(3):
            for j in range(4):
                if self.bags[i][j] != 0:
                    pygame.draw.rect(screen, (0, 153, 51),
                                     (self.coor[0] + j * Cover.size, self.coor[1] + i * Cover.size
                                      , Cover.size, Cover.size))
                    if res is not None and \
                            res.corX - Cannonball.size[0] / 2 <= self.coor[0] + j * Cover.size + Cover.size \
                            and res.corX + Cannonball.size[0] / 2 >= self.coor[0] + j * Cover.size - Cover.size\
                            and res.corY + Cannonball.size[1] / 2 >= self.coor[1] + i * Cover.size - Cover.size\
                            and res.corY - Cannonball.size[1] / 2 <= self.coor[1] + i * Cover.size + Cover.size:
                        if self.bags[i][j] > 0: self.bags[i][j] -= 1
                        res = None

                    if resG is not None and \
                            resG.cor[0] <= self.coor[0] + j * Cover.size + Cover.size \
                            and resG.cor[0] + AlienGun.size[0] >= self.coor[0] + j * Cover.size - Cover.size\
                            and resG.cor[1] + AlienGun.size[1] >= self.coor[1] + i * Cover.size - Cover.size\
                            and resG.cor[1] <= self.coor[1] + i * Cover.size + Cover.size:
                        if self.bags[i][j] > 0: self.bags[i][j] -= 1
                        resG = None
        return [res, resG]

