import pygame as pg

from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, RESIZABLE, FULLSCREEN, K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.display import set_mode, set_caption

from icecream import ic

from random import uniform

pg.init()


size = [1024, 768]

scr = set_mode(size)
set_caption('MyGame')

clock = pg.time.Clock()
fps = 60

class Player:
    def __init__(self):
        self.image = pg.Surface((50, 50))
        self.image.fill('SteelBlue')
        self.rect = self.image.get_rect(center=(
            scr.get_width() // 2,
            scr.get_height() // 2
        ))
        self.speed = 5

    def move(self):
        keys = pg.key.get_pressed()

        if keys[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if keys[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= scr.get_width():
            self.rect.right = scr.get_width()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= scr.get_height():
            self.rect.bottom = scr.get_height()

    def update(self):
        self.move()
        self.check_position()
        scr.blit(self.image, self.rect)


class Enemyes:
    def __init__(self):
        self.image = pg.Surface((25, 5))
        self.image.fill('DarkRed')
        self.generator()
        self.speed = uniform(5, 10)

    def move(self):
        self.rect.move_ip(-self.speed, 0)

    def generator(self):
        self.rect = self.image.get_rect(center=(
        uniform(scr.get_width(), scr.get_width() + 500),
        uniform(0, scr.get_height())
        ))

    def check_position(self):
        if self.rect.left <= -100:
            self.generator()

    def update(self):
        self.move()
        self.check_position()
        scr.blit(self.image, self.rect)


player = Player()

enemies = [Enemyes() for _ in range(15)]


loop = True

while loop:
    scr.fill('black')

    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            loop = False



    player.update()

    for enemy in enemies:
        enemy.update()



    pg.display.update()
    clock.tick(fps)
pg.quit()