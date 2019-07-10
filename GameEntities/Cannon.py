import pygame
from pygame.locals import *
from gamestats import Stats


class Cannon:
    canY = Stats.HEIGHT * 0.9
    size = [Stats.WIDTH / 10, Stats.HEIGHT / 20]
    speed = 0.5

    def __init__(self):
        self.canX = Stats.WIDTH / 2 - Cannon.size[0] / 2

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 153, 51),(self.canX, Cannon.canY, Cannon.size[0], Cannon.size[1]))

    def moveRight(self):
        self.canX += Cannon.speed * Stats.DELTATIME

    def moveLeft(self):
        self.canX -= Cannon.speed * Stats.DELTATIME

    def move(self, left, right):
        if left:
            self.moveLeft()
        if right:
            self.moveRight()


class Cannonball:
    size = [Stats.WIDTH / 64, Stats.HEIGHT / 32]
    speed = 0.3

    def __init__(self, x, y):
        self.corX = x
        self.corY = y

    def draw(self, screen):
        pygame.draw.rect(screen, (204, 0, 102),
                         (self.corX - Cannonball.size[0] / 2, self.corY - Cannonball.size[1] / 2, Cannonball.size[0],
                          Cannonball.size[1]))
        self.corY -= Cannonball.speed * Stats.DELTATIME
