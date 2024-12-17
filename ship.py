import  pygame   # pixabay.com сайт всяких картинок

class Ship:
    """ Класс для управления кораблём. """
    def __init__(self, ai_game):
        """ Инициация корабля и задать стартовую позицию. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загрузить изображение корабля и получить его rect
        self.image =pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Создавать каждый новый корабль внизу экрана и по центру.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """ Нарисовать корабль в его нынешнем рарположении. """
        self.screen.blit(self.image, self.rect)