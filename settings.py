class Settings:
    """ Класс для сохранения всех настоек игры. """

    def __init__(self):
        """ Инициировать настройки игры. """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) # светло серый.
        # (255,0,0) - red, (0,255,0)- green, (0,0,255) - blue.

        # Настройки корабля.
        self.ship_speed = 1.5

        # Настройка пули
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)