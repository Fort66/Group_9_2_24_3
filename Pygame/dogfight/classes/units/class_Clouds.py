from pygame.image import load
from pygame.transform import scale_by

from pygame.sprite import Sprite, Group

from random import uniform, choice, randint

from ..screens.class_Screen import win
from ..groups.class_AllSprites import all_sprites

# clouds_group = Group()


class Clouds(Sprite):
    def __init__(self, path):
        Sprite.__init__(self)
        self._layer = randint(1, 3)
        match self._layer:
            case 1:
                self.scale_value = .4
            case 2:
                self.scale_value = .6
            case 3:
                self.scale_value = .8
        self.image = scale_by(load(path).convert_alpha(), self.scale_value)
        self.generator()
        self.speed = uniform(2, 4)
        # clouds_group.add(self)
        all_sprites.add(self)

    def move(self):
        self.rect.move_ip(-self.speed, 0)

        if self.rect.left < -2000:
            self.generator()

    def generator(self):
        self.rect = self.image.get_rect(center=(
        uniform(win.screen.get_width() + 1000, win.screen.get_width() + 5000),
        uniform(0, win.screen.get_height())
        ))

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)