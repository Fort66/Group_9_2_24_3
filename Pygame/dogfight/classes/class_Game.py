import pygame as pg
pg.init()

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from .class_Screen import Screen
from .class_Player import Player
from .class_Enemies import Enemyes
from .class_AllSprites import all_sprites
from .class_Clouds import Clouds

scr = Screen()

player = Player()
enemies = [Enemyes() for _ in range(15)]
clouds = [Clouds() for _ in range(15)]

class Game:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.fps = 60
        self.loop = True

    def run(self):
        while self.loop:
            scr.screen.fill('SkyBlue')

            for event in pg.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.loop = False

            all_sprites.update()


            pg.display.update()
            self.clock.tick(self.fps)
