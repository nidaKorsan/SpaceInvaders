import pygame
from pygame.locals import *
from gamestats import Stats


class Alien:
    size = [Stats.WIDTH / 20, Stats.HEIGHT / 20]
    speed = 0.02

    def __init__(self, x, y):
        self.corX = x
        self.corY = y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255),
                         (self.corX - Alien.size[0] / 2, self.corY - Alien.size[1] / 2, Alien.size[0],
                          Alien.size[1]))

    def moveRight(self):
        self.corX += Alien.speed * Stats.DELTATIME

    def moveLeft(self):
        self.corX -= Alien.speed * Stats.DELTATIME

    def moveDown(self):
        self.corY += Stats.WIDTH / 40
