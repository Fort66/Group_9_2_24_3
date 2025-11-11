from pygame.image import load
from pygame.transform import scale_by

from pygame.sprite import Sprite, Group

from random import uniform

from ..screens.class_Screen import scr
from ..groups.class_AllSprites import all_sprites
from ..groups.class_SpritesGroups import groups


class Enemyes(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.scr = scr.screen
        self.image = scale_by(load('images/shutter.png').convert_alpha(), .15)
        self.generator()
        self.speed = uniform(5, 10)
        self._layer = 2
        groups.emenyes_group.add(self)
        all_sprites.add(self)

    def move(self):
        self.rect.move_ip(-self.speed, 0)

    def generator(self):
        self.rect = self.image.get_rect(center=(
        uniform(self.scr.get_width(), self.scr.get_width() + 500),
        uniform(0, self.scr.get_height())
        ))

    def check_position(self):
        if self.rect.left <= -100:
            self.generator()

    def update(self):
        self.move()
        self.check_position()
        self.scr.blit(self.image, self.rect)
