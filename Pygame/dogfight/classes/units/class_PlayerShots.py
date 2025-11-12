from pygame.image import load
from pygame.transform import scale_by, flip

from pygame.sprite import Sprite

from ..screens.class_Screen import win



class PlayerShoots(Sprite):
    def __init__(self, pos, speed):
        Sprite.__init__(self)
        self.pos = pos
        self.image = flip(scale_by(load('images/shutter.png').convert_alpha(), .15), True, False)
        self.generator()
        self.speed = speed
        self._layer = 2

    def move(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right >= win.screen.get_width() + 200:
            self.kill()

    def generator(self):
        self.rect = self.image.get_rect(center=self.pos)

    def check_position(self):
        if self.rect.left <= -100:
            self.generator()

    def update(self):
        self.move()
        win.screen.blit(self.image, self.rect)