import sys

import  pygame

class AlienInvasion:
    """ Общий класс который упровляет ресурсами и поведением игры. """

    def __init__(self):
       """ Инициализация игры, создать ресурсы игры. """
       pygame.init()

       self.screen = pygame.display.set_mode((1200, 800))
       pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ Начять главный цикл игры. """
        while True:
            # следить за действиями мыши и клавиатуры.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # показать последний нарисованный экран
            pygame.display.flip()

if __name__ == '__main__':
    # создать экземпляр игры и запустить её.
    ai = AlienInvasion()
    ai.run_game()

