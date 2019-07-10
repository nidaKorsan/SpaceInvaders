import pygame
from GameEntities.Cannon import Cannon, Cannonball
from gamestats import Stats


class AlienGun:
    size = [Stats.WIDTH / 64, Stats.HEIGHT / 24]
    speed = 0.1

    def __init__(self, x, y):
        self.cor = [x, y]

    def draw(self, screen, ball, cannon):#Coordinates are at the top-left
        rstB, rstC = ball, cannon
        pygame.draw.rect(screen, (204, 0, 102), (self.cor[0], self.cor[1], Cannonball.size[0], Cannonball.size[1]))

        if rstB is not None and \
                rstB.corX - Cannonball.size[0] / 2 <= self.cor[0] + AlienGun.size[0]\
                and rstB.corX + Cannonball.size[0] / 2 >= self.cor[0] \
                and rstB.corY + Cannonball.size[1] / 2 >= self.cor[1] \
                and rstB.corY - Cannonball.size[1] / 2 <= self.cor[1] + AlienGun.size[1]:
            rstB = None

        if rstC.canX - Cannon.size[0] / 2 <= self.cor[0] + AlienGun.size[0]\
                and rstC.canX + Cannon.size[0] / 2 >= self.cor[0] \
                and rstC.canY + Cannon.size[1] / 2 >= self.cor[1] \
                and rstC.canY - Cannon.size[1] / 2 <= self.cor[1] + AlienGun.size[1]:
            rstC = None

        self.cor[1] += AlienGun.speed * Stats.DELTATIME

        return rstB, rstC