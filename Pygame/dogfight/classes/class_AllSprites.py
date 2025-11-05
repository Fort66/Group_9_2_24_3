from pygame.sprite import Group


class AllSprites(Group):
    __instalce = None
    def __new__(cls):
        if cls.__instalce is None:
            cls.__instalce = super().__new__(cls)
        return cls.__instalce

    def update(self, *args, **kwargs):
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite._layer):
            sprite.update(*args, **kwargs)

all_sprites = AllSprites()