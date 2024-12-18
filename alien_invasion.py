import sys

import  pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """ Общий класс который упровляет ресурсами и поведением игры. """

    def __init__(self):
        """ Инициализация игры, создать ресурсы игры. """
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    def run_game(self):
        """ Начять главный цикл игры. """
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self.bullets.update()
    def _check_events(self):
        """ Реагировать на нажатие клавиш и движение мыши. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Реагировать на нажатие клавиши. """
        if event.key == pygame.K_RIGHT:
            # Переместить корабль в право.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """ Реагировать, когда клавиша не нажата. """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Создать пулю и добавить к группе пуль."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """ Обновить изображение на экране и переключить на новый экран. """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # показать последний нарисованный экран
        pygame.display.flip()

if __name__ == '__main__':
    # создать экземпляр игры и запустить её.
    ai = AlienInvasion()
    ai.run_game()

