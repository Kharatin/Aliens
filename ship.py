import  pygame   # pixabay.com сайт всяких картинок

class Ship:
    """ Класс для управления кораблём. """
    def __init__(self, ai_game):
        """ Инициация корабля и задать стартовую позицию. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Загрузить изображение корабля и получить его rect
        self.image =pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Создавать каждый новый корабль внизу экрана и по центру.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранить десятичное значение для позиции корабля по горизонтали.
        self.x = float(self.rect.x)

        # индикатор движения.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Обновить текущуу позицию корабля на основе
        индикатора движения.
        """
        # Обновить значение ship.x а не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Обновить объект rect с self.x.
        self.rect.x = self.x

    def blitme(self):
        """ Нарисовать корабль в его нынешнем рарположении. """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ Отцентровать корабль на экране. """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)