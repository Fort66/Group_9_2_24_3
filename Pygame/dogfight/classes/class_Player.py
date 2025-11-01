from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from pygame.key import get_pressed
from pygame.image import load
from pygame.transform import scale_by

class Player:
    def __init__(self, screen):
        self.scr = screen
        self.image = scale_by(load('images/su-33.png').convert_alpha(), .2)
        self.rect = self.image.get_rect(center=(
            self.scr.get_width() // 2,
            self.scr.get_height() // 2
        ))
        self.speed = 5

    def move(self):
        keys = get_pressed()

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
        if self.rect.right >= self.scr.get_width():
            self.rect.right = self.scr.get_width()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.scr.get_height():
            self.rect.bottom = self.scr.get_height()

    def update(self):
        self.move()
        self.check_position()
        self.scr.blit(self.image, self.rect)
