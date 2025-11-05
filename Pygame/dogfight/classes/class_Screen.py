from pygame.display import set_mode, set_caption
from pygame.locals import DOUBLEBUF


class Screen:
    __inistance = None

    def __new__(cls):
        if cls.__inistance is None:
            cls.__inistance = super().__new__(cls)
        return cls.__inistance

    def __init__(self):
        self.screen = set_mode([1920, 1080], DOUBLEBUF)
        self.caption = set_caption('My Game')
