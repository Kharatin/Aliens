class GameStats:
    """  Отслеживание статистики игры. """

    def __init__(self, ai_game):
        """ Инициализация статистики. """
        self.settings = ai_game.settings
        self.reset_stats()
        # Начять игру в активном положении.
        self.game_active = True

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """ Инициализация статистики которая может менятся во время игры. """
        self.ship_left = self.settings.ship_limit
        self.score = 0