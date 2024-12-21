import sys
from time import sleep

import  pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """ Общий класс который упровляет ресурсами и поведением игры. """

    def __init__(self):
        """ Инициализация игры, создать ресурсы игры. """
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("AlienInvasion")

        # Создать экземпляр для сохранения игровой статистики
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Создать кнопку Play.
        self.play_button = Button(self, "Play")
    def run_game(self):
        """ Начять главный цикл игры. """
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _ship_hit(self):
        """ Реагировать на столкновение пришельца с ккораблём. """
        if self.stats.ship_left > 0:
            # Уменьшить ships_left.
            self.stats.ship_left -= 1

            # Избавится от лишних кораблей и пуль.
            self.aliens.empty()
            self.bullets.empty()

            # Создать новый флот и вернуть корабль на стартовую позицыю.
            self._create_fleet()
            self.ship.center_ship()

            # Пауза.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_bullets(self):
        """ Обновить позицию пули и избавится от старых пуль. """
        # Обновить позиции пуль.
        self.bullets.update()

        # Избавится от пуль которые исчезли.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """ Реакция на столкновение пуль с пришельцами. """
        # Удалить все пули и пришельцев которые столкнулись.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Удалить пули и создать новый флот.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _update_aliens(self):
        """ Проверить находится ли флот на краю.
         Обновить позиции пришельцев. """
        self._check_fleet_edges()
        self.aliens.update()

        # Искать столкновение корабля с пришельцем.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Искать может кто из пришельцев достиг нижнего края экрана.
        self._check_aliens_buttom()

    def _check_events(self):
        """ Реагировать на нажатие клавиш и движение мыши. """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """ Начять новую игру когда пользователь нажмёт на кнопку Play. """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Анулировать игровую статистику.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True


            # Удалить излишки пуль и пришельцев.
            self.aliens.empty()
            self.bullets.empty()

            # Создать новый флот и вернуть корабль на стартовую позицию.
            self._create_fleet()
            self.ship.center_ship()

            # Спрятать курсор мыши.
            pygame.mouse.set_visible(False)


    def _check_aliens_buttom(self):
        """ Проверить не достиг ли кто-то низа экрана. """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Среагировать так как будто был подбит карабль.
                self._ship_hit()
                break

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
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """ Создать флот пришельцев. """
        # Создание пришельцев и вычесление колличество пришельцев в ряде.
        # Расстояние между пришельцами ровно ширине пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Расчитать какое колличество рядов пришельцев помещяется на экран.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Создать полный флот пришельцев.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """ Создать пришельца и постатить его в ряд. """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """
        Реагирует на то достиг ли кто то из
         пришельцев края экрана.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Спуск всего флота и изменение направления движения. """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """ Обновить изображение на экране и переключить на новый экран. """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #исовать информайию о счёте.
        self.sb.show_score()

        # Нарисовать кнопку Play если игра не активна.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # показать последний нарисованный экран
        pygame.display.flip()

if __name__ == '__main__':
    # создать экземпляр игры и запустить её.
    ai = AlienInvasion()
    ai.run_game()

