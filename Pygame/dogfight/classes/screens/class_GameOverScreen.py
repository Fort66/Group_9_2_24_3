from pygame.image import load
from pygame.transform import scale


from .class_Screen import win
from ..ui.buttons.class_ButtonText import ButtonText
from ..logic.class_CreateObjects import create_objects
from ..logic.class_Signals import signals

class GameOverScreen:
    __instalce = None

    def __new__(cls):
        if cls.__instalce is None:
            cls.__instalce = super().__new__(cls)
        return cls.__instalce

    def __init__(self):
        self.image = scale(load('images/screens/game_over.jpeg').convert(), win.screen.get_size())
        self.rect = self.image.get_rect()

        self.btn = ButtonText(
            surface=self.image,
            pos = (
                self.rect[2] // 2,
                self.rect[3] - 200
            ),
            size = (800, 50),
            text='Разбился и сгорел!!! Начать игру снова? Esc - выйти',
            rounding=20,
            on_click=lambda: self.change_game_over()
        )

    def change_game_over(self):
        signals.change_signal('game_over')
        if self.btn.is_clicked:
            signals.change_signal('start')

    def update(self):
        win.screen.blit(self.image, self.rect)
        self.btn.update()

game_over_screen = GameOverScreen()