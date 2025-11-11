import pygame as pg
pg.init()

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE

from ..screens.class_Screen import scr
from ..groups.class_AllSprites import all_sprites
from .class_CreateObjects import create_objects

create_objects.create()

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
