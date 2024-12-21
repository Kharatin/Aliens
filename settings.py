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
        #self.ship_speed = 1.5
        self.ship_limit = 3

        # Настройка пули
        #self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельца
        #self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction 1 означает направление движения в право, -1 -- в лево.
        #self.fleet_direction = 1

        # Как быстро игра должна ускорятся.
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Инициализация переменных настроек. """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleed_direction 1 прудставляет направление в право , -1 -- в лево.
        self.fleet_direction = 1

    def increase_speed(self):
        """ Увеличение настроек скорости. """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale