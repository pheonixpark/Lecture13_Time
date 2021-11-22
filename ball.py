import random

from pico2d import *
import random
import game_framework
import game_world

pixelpermeter=(20.0/3)
Bspeed=1000.0
Bkphm=20.0
Bmpm=(Bkphm*1000.0/60.0)
Bmps=(Bmpm/60.0)
Bpps=(Bmps*pixelpermeter)


class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = Bpps):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

class Fallball:
    image = None
    def __init__(self):
        if Fallball.image==None:
            Fallball.image = load_image('ball21x21.png')
        self.x, self.y=random.randint(0,1600-1), random.randint(300,500)
        self.fallspeed=350

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fallspeed * game_framework.frame_time

    def stop(self):
        self.fallspeed=0




