import pygame.font

class Scoreboard:
    """ Класс который выводит счёт. """

    def __init__(self, ai_game):
        """" Инициализация атрибутов связанных со счётом. """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Настройки шрифта для отображения счёта.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Подготовить изображение с начальным счётом.
        self.prep_score()

    def prep_score(self):
        """ Превритить счёт в изображение. """
        #score_str = str(self.stats.score)
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        # Показать счёт в верхнем правом углу экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """ оказать счёт на экране. """
        self.screen.blit(self.score_image, self.score_rect)
