import pygame
from pygame.locals import *
from gamestats import Stats

class Alien:
    size = [Stats.WIDTH / 20, Stats.HEIGHT / 20]
    speed = 0.05

    def __init__(self, x, y):
        self.corX = x
        self.corY = y
        self.alienImg1frame0 = pygame.image.load('alien1-frame0.png')
        self.alienImg1frame1 = pygame.image.load('alien1-frame1.png')

    def draw(self, screen):
        screen.blit(self.alienImg1frame0,(self.corX, self.corY))

    def draw2(self, screen):
        screen.blit(self.alienImg1frame1, (self.corX, self.corY))
        #pygame.draw.rect(screen, (255, 255, 255),
         #                (self.corX - Alien.size[0] / 2, self.corY - Alien.size[1] / 2, Alien.size[0],
          #                Alien.size[1]))

    def moveRight(self):
        self.corX += Alien.speed * Stats.DELTATIME

    def moveLeft(self):
        self.corX -= Alien.speed * Stats.DELTATIME

    def moveDown(self):
        self.corY += Stats.WIDTH / 40
