import pygame
import sys
from gamestats import Stats
from pygame.locals import *
from GameEntities.Cannon import Cannon, Cannonball
from GameEntities.Alliance import Alliance
from GameEntities.Cover import Cover

FPS = 30
fpsClock = pygame.time.Clock()


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Stats.WIDTH, Stats.HEIGHT))
        pygame.display.set_caption("Space Invaders")

        self.cannon = Cannon()
        self.alliance = Alliance()
        self.ball = None
        self.covers = []
        self.covers.append(Cover(Stats.WIDTH * 3 / 40, Stats.HEIGHT * 0.66))
        self.covers.append(Cover(Stats.WIDTH * 13 / 40, Stats.HEIGHT * 0.66))
        self.covers.append(Cover(Stats.WIDTH * 23 / 40, Stats.HEIGHT * 0.66))
        self.covers.append(Cover(Stats.WIDTH * 33 / 40, Stats.HEIGHT * 0.66))
        self.leftK = False
        self.rightK = False
        self.spaceK = False
        Stats.LASTTIME = pygame.time.get_ticks()

    def run(self):
        while True:
            if Stats.LASTTIME - Stats.FRAMETIME >= 500:
                Stats.FRAMETIME = Stats.LASTTIME
                Alliance.frameFlag = not(Alliance.frameFlag)
            Stats.DELTATIME = pygame.time.get_ticks() - Stats.LASTTIME
            Stats.LASTTIME = pygame.time.get_ticks()

            self.screen.fill((0, 0, 0))

            self.cannon.draw(self.screen)

            self.ball, self.cannon = self.alliance.draw(self.screen, self.ball, self.cannon)

            for i in range(4):
                self.ball, self.alliance.gun = self.covers[i].draw(self.screen, self.ball, self.alliance.gun)

            self.checkBall()

            if self.ball is not None:
                self.ball.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                self.handleEvent(event)

            self.cannon.move(self.leftK, self.rightK)

            pygame.display.update()
            fpsClock.tick(FPS)

    def handleEvent(self, event):

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.leftK = True
            elif event.key == K_RIGHT:
                self.rightK = True
            elif event.key == K_SPACE:
                self.spaceK = True

        elif event.type == KEYUP:
            if event.key == K_LEFT:
                self.leftK = False
            elif event.key == K_RIGHT:
                self.rightK = False
            elif event.key == K_SPACE:
                self.spaceK = False

    def checkBall(self):
        if self.ball is not None:
            if self.ball.corY + self.ball.size[1] <= 0:
                self.ball = None
        if self.ball is None and self.spaceK:
            self.ball = Cannonball(self.cannon.canX + self.cannon.size[0] / 2, self.cannon.canY + self.cannon.size[1] / 2)
