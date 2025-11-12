class Signals:
    __instalce = None

    __signals = {
        'start': True,
        'pause': False,
        'game_over': False
    }

    def __new__(cls):
        if cls.__instalce is None:
            cls.__instalce = super().__new__(cls)
        return cls.__instalce

    def __init__(self):
        self.__dict__ = self.__signals


    def change_signal(self, signal):
        self.__dict__[signal] = not self.__dict__[signal]



signals = Signals()