import sys

import  pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Общий класс который упровляет ресурсами и поведением игры. """

    def __init__(self):
        """ Инициализация игры, создать ресурсы игры. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """ Начять главный цикл игры. """
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
    def _check_events(self):
        """ Реагировать на нажатие клавиш и движение мыши. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Переместить корабль в право.
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    def _update_screen(self):
        """ Обновить изображение на экране и переключить на новый экран. """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # показать последний нарисованный экран
        pygame.display.flip()

if __name__ == '__main__':
    # создать экземпляр игры и запустить её.
    ai = AlienInvasion()
    ai.run_game()

