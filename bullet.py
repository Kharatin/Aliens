import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """  Класс для управления пулями, выпущенными из корабля. """

    def __init__(self, ai_game):
        """ Создать объект bullet в нынешней позиции корабля. """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Создать rect в (0, 0) и задать правильную позицию.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Сохранять позицию пули как десятичное значение.
        self.y = float(self.rect.y)

    def update(self):
        """ Сместить пулю вверх экрана. """
        # Обновить десятичную позицию пули.
        self.y -= self.settings.bullet_speed
        # Обновить позицию rect.
        self.rect.y = self.y

    def draw_bullet(self):
        """  нарисовать пулю на экране. """
        pygame.draw.rect(self.screen, self.color, self.rect)