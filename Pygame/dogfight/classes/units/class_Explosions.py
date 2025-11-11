import gif_pygame as gif

from pygame.sprite import Sprite

from ..groups.class_AllSprites import all_sprites
from ..screens.class_Screen import scr


class Explosions(Sprite):
    def __init__(self, pos, types):
        Sprite.__init__(self)
        self._layer = 2
        self.speed = None

        if types == 1:
            self.image = gif.load('images/rocket_explosion.gif', loops=0)
            self.image = gif.transform.scale_by(self.image, .5, new_gif=True)

        self.rect = self.image.get_rect(center=pos)
        all_sprites.add(self)

    def move(self):
        self.rect.move_ip(self.speed, 0)

    def update(self):
        if not self.image._ended:
            self.image.render(scr.screen, self.rect)
        else:
            self.kill()
        self.move()