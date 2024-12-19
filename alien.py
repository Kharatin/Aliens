import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Класс который представляет одного пришельца с флота. """
    def __init__(self, ai_game):
        """ Инициировать пришельца и задать его начальное место расположение. """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Возращяет исина если пришелец находится на краю экрана. """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    def update(self):
        """ Сместить пришельца в право или лево. """
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x