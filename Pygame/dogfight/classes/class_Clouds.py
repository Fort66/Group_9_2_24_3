from pygame.image import load
from pygame.transform import scale_by

from pygame.sprite import Sprite, Group

from random import uniform, choice, randint

from .class_Screen import Screen
from .class_AllSprites import all_sprites

scr = Screen()
clouds_group = Group()

clouds_list = [
    'images/cloud2.png',
    'images/cloud3.png',
    'images/cloud4.png',
    'images/cloud5.png'
]


class Clouds(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self._layer = randint(1, 3)
        self.scr = scr.screen
        match self._layer:
            case 1:
                self.scale_value = .4
            case 2:
                self.scale_value = .6
            case 3:
                self.scale_value = .8
        self.image = scale_by(load(choice(clouds_list)).convert_alpha(), self.scale_value)
        self.generator()
        self.speed = uniform(2, 4)
        clouds_group.add(self)
        all_sprites.add(self)

    def move(self):
        self.rect.move_ip(-self.speed, 0)

        if self.rect.left < -2000:
            self.generator()

    def generator(self):
        self.rect = self.image.get_rect(center=(
        uniform(self.scr.get_width() + 1000, self.scr.get_width() + 2000),
        uniform(0, self.scr.get_height())
        ))

    def update(self):
        self.move()
        self.scr.blit(self.image, self.rect)