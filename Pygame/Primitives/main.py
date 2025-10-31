import pygame as pg

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, RESIZABLE, FULLSCREEN, MOUSEMOTION
from pygame.display import set_mode, set_caption

from random import choice

from math import pi

pg.init()

# width = 1024
# height = 768

size = [1024, 768]

scr = set_mode(size)
set_caption('MyGame')

colors = ['DarkOliveGreen', 'SteelBlue', 'DarkRed', 'Indigo']

loop = True

while loop:
    # scr.fill('DarkOliveGreen')

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                scr.fill(choice(colors))
                print(event.pos)
                



    # pg.draw.rect(scr,'red', [100, 100, 100, 100], 1)
    # pg.draw.line(scr, 'blue', [50, 50], [250, 250], 1)
    # pg.draw.aaline(scr, 'green', [250, 50], [50, 250])

    # pg.draw.lines(scr, 'yellow', True, [[300, 250], [250, 50], [250, 250]], 1)
    # # pg.draw.aalines(scr, 'white', True, [[300, 250], [250, 50], [250, 250]])

    # pg.draw.circle(scr, 'purple', [500, 500], 50, 1)
    # pg.draw.ellipse(scr, 'white', [700, 500, 50, 100], 1)

    # pg.draw.arc(scr, 'magenta', [600, 500, 100, 100], pi/2, pi, 1)

    # pg.draw.polygon(scr, 'cyan', [[800, 500], [850, 500], [825, 550]], 1)

    pg.display.update()
pg.quit()