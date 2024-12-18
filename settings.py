class Settings:
    """ Класс для сохранения всех настоек игры. """

    def __init__(self):
        """ Инициировать настройки игры. """
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230) # светло серый.
        # (255,0,0) - red, (0,255,0)- green, (0,0,255) - blue.

        # Настройки корабля.
        self.ship_speed = 1.5