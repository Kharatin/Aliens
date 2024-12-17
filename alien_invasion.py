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
            # следить за действиями мыши и клавиатуры.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # занава перерисовать экран на каждой итерации цикла.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # показать последний нарисованный экран
            pygame.display.flip()

if __name__ == '__main__':
    # создать экземпляр игры и запустить её.
    ai = AlienInvasion()
    ai.run_game()

