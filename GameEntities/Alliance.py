from GameEntities.Alien import Alien
from GameEntities.AlienGun import AlienGun
from GameEntities.Cannon import Cannonball
from gamestats import Stats
import random

class Alliance:
    def __init__(self):
        self.allies = []
        for i in range(5):
            self.allies.append(list())
            for j in range(11):
                self.allies[i].append(Alien( (j + 2) * Stats.WIDTH / 16 + Alien.size[0] / 2,
                                          i * Stats.HEIGHT / 8 + Alien.size[1] / 2))
        self.direction = 1
        self.counter = 190
        self.gun = None

    def draw(self, screen, ball, cannon):
        res = ball
        resCan = cannon
        downFlag = False
        self.counter += Stats.DELTATIME
        print (float(Stats.DELTATIME))
        if self.counter >= 3000 and self.gun is None:
            self.counter = 0
            al = None
            while True:
                if al is not None:
                    break
                al = self.allies[random.randint(0, 4)][random.randint(0, 10)]
            self.gun = AlienGun(al.corX,al.corY)#RANDOM CREATE

        if self.gun is not None:
            res, resCan = self.gun.draw(screen, ball, cannon)
            if self.gun.cor[1] >= Stats.HEIGHT:
                self.gun = None

        for i in range(5):
            for j in range(11):
                if self.allies[i][j] is not None:
                    if self.allies[i][j].corX + self.allies[i][j].size[0] / 2 >= Stats.WIDTH:
                        self.direction = -1
                        downFlag = True
                    elif  self.allies[i][j].corX - self.allies[i][j].size[0] / 2 <= 0:
                        self.direction = 1
                        downFlag = True

        if downFlag:
            for i in range(5):
                for j in range(11):
                    if self.allies[i][j] is not None:
                        self.allies[i][j].moveDown()

        for i in range(5):
            for j in range(11):
                if self.allies[i][j] is not None:

                    if self.direction == 1:
                        self.allies[i][j].moveRight()
                    else:
                        self.allies[i][j].moveLeft()

                    self.allies[i][j].draw(screen)
                    if res is not None and \
                           res.corX - Cannonball.size[0] / 2 <= self.allies[i][j].corX + self.allies[i][j].size[0] / 2\
                            and res.corX + Cannonball.size[0] / 2 >= self.allies[i][j].corX - self.allies[i][j].size[0] / 2\
                            and res.corY + Cannonball.size[1] / 2 >= self.allies[i][j].corY - self.allies[i][j].size[1] / 2\
                            and res.corY - Cannonball.size[1] / 2 <= self.allies[i][j].corY + self.allies[i][j].size[1] / 2:
                        self.allies[i][j] = None
                        res = None
        return res, resCan

  #  res    al
  #  AAAA   bbbb
  #  A  A   B  B
  #  aaaa   BBBB
# Benim solum A'nin sagini geçmediyse : Benim solum < A'nin sagi
# A'nın solu benim sağımı geçmediyse: Benim sağim > A'nın solu
# Benim altım A'nın üstünü geçmediyse: A'nın üstü < B'nin altı
# A'nın altı benim üstümü geçmediyse: A'nın altı > B'nin üstü