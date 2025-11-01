from pygame.image import load
from pygame.transform import scale_by

from random import uniform


class Enemyes:
    def __init__(self, screen):
        self.scr = screen
        self.image = scale_by(load('images/shutter.png').convert_alpha(), .15)
        self.generator()
        self.speed = uniform(5, 15)

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
