from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_c
from pygame.key import get_pressed
from pygame.image import load
from pygame.transform import scale_by

from pygame.sprite import Sprite, Group, groupcollide

from ..screens.class_Screen import scr
from ..groups.class_AllSprites import all_sprites
from .class_PlayerShots import PlayerShoots
from .class_Explosions import Explosions
from ..groups.class_SpritesGroups import groups

from time import time

from icecream import ic

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.scr = scr.screen
        self.image = scale_by(load('images/su-33.png').convert_alpha(), .2)
        self.rect = self.image.get_rect(center=(
            self.scr.get_width() // 2,
            self.scr.get_height() // 2
        ))
        self.speed = 5
        self._layer = 2
        self.permission_shots = .5
        self.shoot_time = 1
        groups.player_group.add(self)
        all_sprites.add(self)

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

        if keys[K_c]:
            if not self.shoot_time:
                self.shoot_time = time()
            if time() - self.shoot_time >= self.permission_shots:
                shoots = PlayerShoots(pos=(self.rect.centerx - 46, self.rect.centery + 15), speed=10)
                groups.player_rockets_group.add(shoots)
                all_sprites.add(shoots)
                self.shoot_time = time()

    def check_position(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.scr.get_width():
            self.rect.right = self.scr.get_width()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.scr.get_height():
            self.rect.bottom = self.scr.get_height()

    def collision(self):
        rockets_collide = groupcollide(groups.emenyes_group, groups.player_rockets_group, True, True)
        if rockets_collide:
            hits = list(rockets_collide.keys())[0]
            self.explosion_rocket = Explosions(hits.rect.center, 1)
            self.explosion_rocket.speed = self.speed * -1

    def update(self):
        self.move()
        self.check_position()
        self.collision()
        self.scr.blit(self.image, self.rect)
