import pygame as pg

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, RESIZABLE, FULLSCREEN, K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.display import set_mode, set_caption

from icecream import ic

from random import uniform

from classes.class_Player import Player
from classes.class_Enemies import Enemyes

pg.init()


size = [1920, 1080]

scr = set_mode(size)
set_caption('MyGame')

clock = pg.time.Clock()
fps = 60






player = Player(scr)

enemies = [Enemyes(scr) for _ in range(15)]


loop = True

while loop:
    scr.fill('SkyBlue')

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False



    player.update()

    for enemy in enemies:
        enemy.update()



    pg.display.update()
    clock.tick(fps)
pg.quit()