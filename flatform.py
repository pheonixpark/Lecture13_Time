from pico2d import *
import random
class Flatfrom:
    def __init__(self):
        self.x, self.y= random.randint(200,1400), random.randint(100,400)
        self.image = load_image('grass.png')

    def update(self):
        self.x+=1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 400, self.y - 35, self.x + 400, self.y + 35
