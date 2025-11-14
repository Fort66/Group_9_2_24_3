import gif_pygame as gif
from gif_pygame import load
from gif_pygame.transform import scale_by

from pygame.sprite import Sprite

from ..groups.class_AllSprites import all_sprites
from ..screens.class_Screen import win


class Explosions(Sprite):
    def __init__(self, pos, types):
        Sprite.__init__(self)
        self._layer = 2
        self.speed = 0

        if types == 1:
            self.create_explosion('images/explosions/rocket_explosion.gif', .5, 0)

        if types == 2:
            self.create_explosion('images/explosions/plane_explosion.gif', 1.7, 0)

        self.rect = self.image.get_rect(center=pos)
        all_sprites.add(self)

    def create_explosion(self, path, scale_value, loops):
         self.image = scale_by(load(path, loops=loops), scale_value, new_gif=True)

    def move(self):
        self.rect.move_ip(self.speed, 0)

    def update(self):
        if not self.image._ended:
            self.image.render(win.screen, self.rect)
        else:
            self.kill()
        self.move()